# Security Policy

**Last updated:** 2025-09-24
**Scope:** This repository hosts *public* configuration guides, examples, and helper assets for Ciena Route/Switch (RSP) products. It is intentionally free of confidential or production data.

---

## 1) Our security posture (what to expect)

- Examples may show **RFC1918** lab IPv4 addresses (10/8, 172.16/12, 192.168/16) and **IPv6 documentation prefix** addresses (**2001:db8::/32**) for clarity and reproducibility.
- Examples may reference **publicly documented device default credentials** *only* to illustrate first-login flows.
  > **IMPORTANT:** Defaults are for isolated lab illustration. **Change all credentials before any deployment** and follow your organization’s password policy.

---

## 2) Hard rules for content (must / must-not)

### The files in this repo **MUST**:
- Use **only** RFC1918 (IPv4) or **2001:db8::/32** (IPv6) in examples.
- Use **generic hostnames** in prose (e.g., `router-a`, `router-b`); keep literal IPs inside code blocks.
- Sanitize screenshots (titles, prompts, banners, hostnames, ticket numbers).

### The files in this repo **MUST NOT** include:
- Any **public IP addresses**
  - i.e. Typical "public" IP addresses (such as the well-known public DNS loopbacks) must be replaced with RFC1918 or 2001:db8::/32 equivalents.
- Any **business system** IPs/hostnames, or real **internal DNS names**.
- **Non-default** or environment-specific secrets: passwords, API keys, tokens, SNMP communities, TACACS/RADIUS shared secrets, certificate private keys, JWTs, SSH private keys, etc.
- **Customer** data of any kind: configs, logs, support bundles, PCAPs, inventory lists, topologies, ticket numbers, names, or emails.
- Architecture diagrams or text that reveal **sensitive internal topology** (links, sites, VRFs, ASNs) tied to a real environment.
- Personal phone numbers or personal emails. If an email must appear, use company addresses with contributor consent or a team alias (see §6).

> If in doubt, leave it out and ask in your PR.

---

## 3) Example style (allowed patterns)

```bash
# Allowed: RFC1918 IPv4 in a code block, generic hostnames in prose
ssh diag@10.92.44.10   # router-a (lab)
ssh diag@10.92.44.11   # router-b (lab)
```

> **IMPORTANT:** Default credentials shown in this guide are for an **isolated lab**.
> **Change all passwords/keys** and disable defaults before any field or production use.

---

## 4) Review & governance

- **Automated scanning:**
  - GitHub Secret Scanning / Push Protection (if available) must be enabled.
  - CI must run a secret scanner (e.g., gitleaks or trufflehog).
  - Configure scanners to **block real secrets** and **allow** RFC1918/2001:db8 addresses.
- **Branch protection:** Require passing checks and at least one Security reviewer approval on protected branches.

---

## 5) Pull Request security checklist

Add the following to every PR description and check all that apply:

- [ ] Only **RFC1918** (IPv4) and/or **2001:db8::/32** (IPv6) addresses appear.
- [ ] **No public IPs**, **no internal DNS/hostnames**, **no site names**.
- [ ] **No non-default credentials, tokens, keys, or secrets** of any kind.
- [ ] If a default credential is shown, an **IMPORTANT** callout instructs users to **change it**.
- [ ] **No customer/business data** (configs, logs, PCAPs, inventory, names, tickets).
- [ ] Screenshots/images are **sanitized**.
- [ ] CI secret scanning **passed**.
- [ ] I confirm this content reflects **lab-only** examples and is not copied from a real environment.

---

## 6) Contact & coordinated disclosure

If you believe you have found a security issue in this repository or accidentally committed sensitive data:

1. **Do not** open a public issue.
2. Open a **private Security Advisory** (GitHub → *Security* → *Advisories* → *Report a vulnerability*), **or** email the maintainers at:
   **📧 jgroom@ciena.com**.
3. If a credential was exposed, **rotate/disable it immediately**.
4. A maintainer will acknowledge within **2 business days** and work with you on next steps.

---

## 7) Incident handling & history cleanup

If sensitive material lands in the repo:
- **Immediate containment:** remove the content in a follow-up commit, rotate impacted credentials, and open a private advisory (§6).
- **History:** maintainers will coordinate history cleanup (e.g., `git filter-repo`/BFG) *if necessary*; note that cleanup does **not** replace rotation.
- **Post-mortem:** summarize root cause (missed checklist item, scanner gap, etc.) and update docs/automation accordingly.

---

## 8) Attribution & contributor privacy

- Contributors must consent to using their **company email** in commit metadata; otherwise, use a **team alias** or GitHub **noreply** address.
- Do not include personal phone numbers or other PII in documentation or commit messages.

---

## 9) Out-of-scope

- This repository does **not** publish security fixes for products; product security advisories are handled via official Ciena channels.
- The examples herein are **not production hardening guides**. Follow your organization’s policies for password rotation, RBAC, AAA, logging, and encryption.

---

## 10) Changes to this policy

Proposed edits to **SECURITY.md** require approval from Security reviewers (via PR) and will be versioned in Git history.
