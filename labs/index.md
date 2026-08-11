# SAOS 10x Lab Program

Hands-on containerlab labs for Ciena SAOS 10 SE enablement. All labs are
built and validated against SAOS release 10.12.00.0228 (container image
`vrnetlab/ciena_saos:10-12-00-0228`).

## Getting Started

Set your repo coordinates and target lab, then use either retrieval path
below. Replace the placeholder values with the actual GitHub owner, repo
name, and the lab you want to run.

```bash
GITHUB_OWNER=<your-github-owner>
GITHUB_REPO=<your-repo-name>
REPO_URL="https://github.com/${GITHUB_OWNER}/${GITHUB_REPO}"
LAB=F1-Loopbacks-and-Interfaces   # replace with your target lab
```

### Option A — Shallow git clone (sparse checkout)

Clones only the commit history needed and limits the working tree to the
single lab directory plus top-level files:

```bash
git clone --filter=blob:none --no-checkout "${REPO_URL}.git"
cd "${GITHUB_REPO}"
git sparse-checkout init --cone
git sparse-checkout set "labs/${LAB}"
git checkout
```

Deploy from the repo root:

```bash
containerlab deploy -t "labs/${LAB}/topo.clab.yml"
```

### Option B — Download archive (no git)

Downloads and unpacks only the lab directory you need without cloning the
full repository:

```bash
wget -qO- "${REPO_URL}/archive/refs/heads/main.tar.gz" \
  | tar -xz --strip-components=2 \
       "${GITHUB_REPO}-main/labs/${LAB}"
cd "${LAB}"
containerlab deploy -t topo.clab.yml
```

> **Tip:** Prefer Option A if you plan to iterate on configs or pull future
> updates. Use Option B for a one-shot deployment on a host without git.

## Foundation Track

Start with the F0 theory guide, then follow the recommended F1-F4 sequence.
F5 is an alternative branch from F2 for learners who specifically need LDP.
An OSPF → SR-MPLS → BGP alternative is planned; the `O` identifiers remain
reserved for Operations, so that future branch will use `A` identifiers.

| ID  | Lab                                                            | Topic                                       |
| --- | -------------------------------------------------------------- | ------------------------------------------- |
| F0  | [SAOS Fundamentals](F0-SAOS-Fundamentals/README.md)              | CLI contexts, hierarchy, classifiers, FPs, and FDs |
| F1  | [Loopbacks and Interfaces](F1-Loopbacks-and-Interfaces/README.md) | Classifiers, FDs, FPs, IPv4/IPv6, loopbacks |
| F2  | [IS-IS Routing](F2-IS-IS-Routing/README.md)                       | IS-IS, NET/NSAP, BFD, MD5, IPv6 AF          |
| F3  | [SR-MPLS](F3-SR-MPLS/README.md)                                   | SR prefix-SID, SRGB, IS-IS MPLS-TE/SR, CSPF |
| F4  | [BGP](F4-BGP/README.md)                                           | iBGP, MP-BGP, routing policy over SR-MPLS    |
| F5  | [LDP](F5-LDP/README.md)                                           | Alternative LDP/MPLS transport from F2       |

SR Policy follows the SR-MPLS foundation in the Transport track. Its first
lab will stay introductory and omit color-based policy.

## Services Track

Prerequisites: F1, F2, F3, F4

| ID  | Lab                      | Topic                             |
| --- | ------------------------ | --------------------------------- |
| S1  | [L3VPN](S1-L3VPN/README.md) | VRF, RD, RT, VPNv4, route leaking |
| S2  | [EVPN-VPWS](S2-EVPN-VPWS/README.md) | EVPN instance, VPWS, ESI, all-active multi-homing |

| Lab                            | Topic                      |
| ------------------------------ | -------------------------- |
