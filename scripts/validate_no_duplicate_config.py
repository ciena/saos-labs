#!/usr/bin/env python3
"""Static gate: no SAOS config line may appear twice in the same file.

A repeated command is at best dead weight pushed to the device at boot, and at
worst a copy-paste slip hiding a line that was meant to be edited (that is how
F3/F4/F5 each shipped the CLASSIFIER-UNTAGGED + flow-point pair twice). The
rule is whole-file: a command may appear at most once across the
`# Preloaded` block and every `# Task <n>` block, because the preload is always
applied before any task, so re-declaring a preloaded object inside a task is a
no-op.

Checked over configs/*.cfg, configs/*.cfg.partial, and solutions/*.cfg — both
trees matter: the partials are what containerlab pushes via startup-config, and
the solutions are what the published docs embed.

Only byte-identical commands (after whitespace normalization) are reported.
Detecting conflicting re-declarations — the same object named twice with
different attributes — is deliberately out of scope.

Runs in CI without devices, alongside validate_solution_blocks.py.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATH = REPO_ROOT / "labs"
SKIP_DIRS = {"assets"}

# SAOS sub-mode navigation verbs. These legitimately repeat: every sub-mode a
# config enters has to be closed again, so a file can hold dozens of `exit`
# lines (see labs/S1-L3VPN/configs/PE_1.cfg.partial, where each `bgp instance
# ... address-family ...` block is closed by an indented `exit` stack). Only
# `exit` occurs in the labs today; the rest are listed so the gate stays quiet
# if a future config navigates sub-modes another way.
NAVIGATION = {"exit", "apply", "gotop", "top", "return", "end"}


def _display_path(path: Path) -> Path:
  try:
    return path.relative_to(REPO_ROOT)
  except ValueError:
    return path


def validate_config(path: Path) -> list[str]:
  """Return one error per repeated command in a single config file."""
  errors: list[str] = []
  first_seen: dict[str, int] = {}

  for line_number, raw_line in enumerate(path.read_text().splitlines(), start=1):
    # Normalize so indentation and internal spacing cannot hide a duplicate.
    command = " ".join(raw_line.split())
    if not command or command.startswith("#"):
      continue  # blank, or a '# Preloaded'/'# Task <n>' boundary marker
    if command in NAVIGATION:
      continue

    previous = first_seen.get(command)
    if previous is None:
      first_seen[command] = line_number
    else:
      errors.append(
          f"line {line_number}: duplicate of line {previous}: '{command}'")

  return errors


def config_files(paths: list[Path]) -> tuple[list[Path], list[str]]:
  """Resolve CLI paths to config files: .cfg / .cfg.partial under a lab."""
  files: set[Path] = set()
  errors: list[str] = []
  for path in paths:
    if not path.exists():
      errors.append(f"{_display_path(path)}: path does not exist")
    elif path.is_file():
      if path.name.endswith((".cfg", ".cfg.partial")):
        files.add(path)
      else:
        errors.append(
            f"{_display_path(path)}: expected a .cfg or .cfg.partial file")
    else:
      # A lab directory, or a labs/ root holding many of them.
      lab_dirs = [path] + [
          child for child in path.iterdir()
          if child.is_dir() and not child.name.startswith(".")
          and child.name not in SKIP_DIRS
      ]
      for lab_dir in lab_dirs:
        for sub in ("configs", "solutions"):
          files.update(
              cfg for cfg in (lab_dir / sub).glob("*.cfg*")
              if cfg.name.endswith((".cfg", ".cfg.partial")))
  if not files and not errors:
    errors.append("no configs/*.cfg* or solutions/*.cfg files found in the"
                  " requested paths")
  return sorted(files), errors


def main(argv: list[str] | None = None) -> int:
  parser = argparse.ArgumentParser(
      description="Forbid duplicated config lines in lab configs.")
  parser.add_argument(
      "paths",
      nargs="*",
      type=Path,
      help="config files, lab directories, or a labs directory"
           " (default: labs/)",
  )
  args = parser.parse_args(argv)
  files, all_errors = config_files(args.paths or [DEFAULT_PATH])

  for path in files:
    for error in validate_config(path):
      all_errors.append(f"{_display_path(path)}: {error}")

  if all_errors:
    print("Duplicate-config-line validation failed:")
    for error in all_errors:
      print(f" - {error}")
    return 1

  print(f"All {len(files)} config files are free of duplicate lines.")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
