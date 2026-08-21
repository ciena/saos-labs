# Changelog

Release notes for the public **SAOS 10x Lab Program** site. This log tracks what
is published in this repository and is maintained here independently of any
upstream authoring history.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## 2026-08-21

### Fixed
- **F3 no longer configures the same flow point twice.** The lab's startup
  configs and solutions declared the `CLASSIFIER-UNTAGGED` classifier and the
  `PE_1-PE_2-FP` flow point a second time, so the published pages showed a
  two-line block repeated back to back and the nodes were sent those commands
  twice at boot. The repeat was inert — re-applying an identical command
  changes nothing on the device — but it was confusing to read and to copy by
  hand. Each block now appears once.

## 2026-08-19

### Added
- **F3 — Segment Routing over IS-IS (SR-MPLS)** hands-on lab: build the MPLS
  transport layer directly on the F2 IS-IS underlay — enable MPLS forwarding
  with a shared SRGB, turn on segment routing and MPLS-TE under the IS-IS
  instance, and assign a prefix-SID to each provider-edge loopback. Verify the
  resulting SR label bindings and loopback-to-loopback forwarding across the
  core. Neither LDP nor BGP is involved. Published with its rendered lab pages,
  topology diagrams, and startup and solution configs, and added to the site
  nav and search. F0 → F1 → F2 → F3 is now the recommended path.

## 2026-08-18

### Added
- **F2 — IS-IS Routing** hands-on lab: bring up an IS-IS adjacency between the
  two provider-edge nodes (NET/NSAP addressing, MD5 authentication, and the
  IPv6 address family), then verify adjacencies, learned routes, and
  loopback-to-loopback reachability. Published with its rendered lab pages and
  added to the site nav and search. F0 → F1 → F2 is now the complete
  recommended starting path.
- Topology diagrams now carry a **legend** explaining what the colours and line
  styles mean: which nodes are configured in the lab versus present but unused,
  and which links are in use versus reserved for a later lab.
- Topology diagrams now shade a **provider domain** region, so provider-edge
  (PE) routers are visually distinguishable from customer-edge (CE) routers.
  The two were previously drawn identically and could only be told apart from
  the chassis model printed under each node.

### Changed
- Topology diagrams render noticeably larger on the page — the drawings
  reserved far more canvas than they actually used.

### Fixed
- Diagonal links in the topology diagrams did not quite touch the nodes they
  connect, leaving a visible gap at one or both ends. Every link now meets its
  nodes.
- Link labels that were crossed out by their own link line have been moved
  clear, and label text stays readable where a link passes behind it.
- The repository README described the topology diagrams as generated
  automatically. They are hand-authored and maintained directly; the
  description now matches.
- The F1 and F2 resource notes referred to interfaces as `eth1`. The topology
  files name link endpoints by SAOS port number — for example
  `[ "PE_1:1", "PE_2:1" ]` — which is what you actually see when editing them.
- **Edit on GitHub** links now resolve. They pointed at a non-existent
  `edit/master/docs/...` path; they now target `edit/main/labs/<lab>/README.md`.
- Simplified the "Advanced (git)" one-lab fetch to a plain
  `git clone --depth 1` (dropped the `--filter`/`--no-checkout`/sparse-checkout
  ceremony) on the home page and in the repository README.

## 2026-08-17

### Added
- **F1 — Loopbacks and Interfaces** hands-on lab: build loopback and IP
  interfaces on SAOS 10x (classifiers, forwarding domains, flow points, IPv4
  and IPv6 addressing) and verify connectivity between directly-connected
  nodes. Published with its rendered lab pages and added to the site nav and
  search.
- **F0 — SAOS Fundamentals:** new "Advanced CLI" section covering when and why
  to use `apply`, `exit`, and `gotop`, and how SAOS stages sub-mode edits
  versus auto-applying complete one-line commands.

## 2026-08-11

### Added
- Initial public release. **F0 — SAOS Fundamentals** theory guide, published with
  the rendered lab site served via GitHub Pages.
