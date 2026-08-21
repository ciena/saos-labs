# F4 — Border Gateway Protocol (BGP)

## Goals

Add BGP after the primary F3 SR-MPLS transport is operational. This lab does
not add LDP. By the end of this lab you will be able to:

- Configure loopback-sourced iBGP with MD5 authentication
- Enable the IPv4, VPNv4, EVPN, and labeled-unicast address families
- Redistribute a loopback into BGP with a policy that sets a community
- Verify the BGP session, advertised routes, and applied policy

## Topology

![topology](./topo.clab.svg)

![topology detail](./topo.detail.svg)

PE_1 and PE_2 retain the F3 SR-MPLS underlay on port 1. BGP peers use the
`lb1` loopbacks as stable endpoints.

### BGP addressing and session parameters

| Parameter | PE_1 | PE_2 |
| --- | --- | --- |
| ASN | 65032 | 65032 |
| Router ID / peer source | 172.16.0.1 | 172.16.0.2 |
| Redistribution loopback | 10.65.0.32/32 | 10.65.0.33/32 |
| Community | 65032:100 | 65032:100 |

## Prerequisites

- Complete F1 through F3, or deploy this lab with its included F3 baseline.
- Confirm `show isis segment-routing` reports `Bootcamp` as enabled.
- Make the SAOS 10x image `vrnetlab/ciena_saos:10-12-00-0228` (release 10.12.00.0228) available to Containerlab.
- Activate the built-in trial license after deployment.

## Startup Configs

The checkpoint baseline each node boots from. If you are assembling the lab by hand, create a `configs/` folder next to `topo.clab.yml` and copy each file into it before you deploy.

- [PE_1.cfg.partial](./configs/PE_1.cfg.partial)
- [PE_2.cfg.partial](./configs/PE_2.cfg.partial)
- [PE_3.cfg.partial](./configs/PE_3.cfg.partial)
- [CE1.cfg.partial](./configs/CE1.cfg.partial)
- [CE2.cfg.partial](./configs/CE2.cfg.partial)

## Deploy

### Start from checkpoint

```bash
LAB=F4-BGP
cd labs/${LAB}            # from the repo root, or cd into the unpacked directory
containerlab deploy -t topo.clab.yml
```

Equivalent invocation from the repo root:

```bash
containerlab deploy -t "labs/${LAB}/topo.clab.yml"
```

The lab topology (`topo.clab.yml`):

```yaml
name: F4-BGP
topology:
  defaults:
    kind: ciena_saos
    image: vrnetlab/ciena_saos:10-12-00-0228
    labels:
      lab-mode: hands-on
  nodes:
    PE_1:
      type: '5162'
      startup-config: configs/PE_1.cfg.partial
    PE_2:
      type: '5162'
      startup-config: configs/PE_2.cfg.partial
    PE_3:
      type: '5162'
      labels:
        lab-state: unused
      startup-config: configs/PE_3.cfg.partial
    CE1:
      type: '3984'
      labels:
        lab-state: unused
      startup-config: configs/CE1.cfg.partial
    CE2:
      type: '3984'
      labels:
        lab-state: unused
      startup-config: configs/CE2.cfg.partial
  links:
  - endpoints: [ "PE_1:1", "PE_2:1" ]
  - endpoints: [ "PE_1:2", "CE1:1" ]
  - endpoints: [ "PE_2:2", "CE2:1" ]
  - endpoints: [ "PE_2:4", "PE_3:1" ]
  - endpoints: [ "PE_1:4", "PE_3:3" ]
  - endpoints: [ "CE2:2", "PE_3:2" ]
```

Connect to the active PEs:

```bash
ssh diag@clab-F4-BGP-PE_1
ssh diag@clab-F4-BGP-PE_2
```

Default credentials: `diag` / `ciena123`

## Instructions

<!-- task-index -->
- [Task 1: Create the BGP instances](#task-1)
- [Task 2: Establish authenticated iBGP](#task-2)
- [Task 3: Enable multiprotocol BGP](#task-3)
- [Task 4: Redistribute a policy-controlled loopback](#task-4)
- [Task 5: Verify BGP over SR-MPLS](#task-5)

<a id="task-1"></a>
### Task 1: Create the BGP instances
<a href="#task-1" title="Direct link to this task (right-click to copy)">🔗</a>

<!-- prose: in-depth -->

**Summary** — On each PE, create the BGP instance for AS `65032` and give it
its own `lb1` address as router-id. That is the entire task — no address
families, no peers yet.

**Background** — Every BGP router needs two identities before it can do
anything: an autonomous system number and a router-id. An autonomous system
is one network under a single administrative and routing policy — one
operator's domain — and its number is how BGP tells inside from outside.
Here both PEs join the same AS, `65032` — the instance number in SAOS 10x
*is* the local AS — which is what will make the next task's session iBGP
rather than eBGP.

**Implementation** — A single instance is built per PE: instance `65032`
with the router-id set explicitly to each node's `lb1` address (`172.16.0.1`
on `PE_1`, `172.16.0.2` on `PE_2`); tying it to the loopback keeps the
router's BGP identity stable no matter which physical links come and go.

**Configure** (config mode) on **PE_1**:

```saos-config
bgp instance 65032 router-id 172.16.0.1
```

**Configure** (config mode) on **PE_2**:

```saos-config
bgp instance 65032 router-id 172.16.0.2
```

<!-- verify-prose -->

There are no checks for this task, and that is expected: `show bgp` renders
an empty table until at least one address-family or peer exists, so a
correct Task 1 configuration produces nothing visible yet. Don't mistake the
empty output for failure — the instance and router-id will surface in the
next task's first check.

Teaching question: why might a platform choose to show nothing rather than a
half-configured instance?

<a id="task-2"></a>
### Task 2: Establish authenticated iBGP
<a href="#task-2" title="Direct link to this task (right-click to copy)">🔗</a>

<!-- prose: in-depth -->

**Summary** — Now bring up the iBGP session — but between loopbacks, not
link addresses. Each PE peers with the other's `lb1` (`172.16.0.2` from
`PE_1`, `172.16.0.1` from `PE_2`) with remote-as `65032`, the same AS as the
local instance, and the session is authenticated with an MD5 password.

**Background** — Sourcing matters: the session's TCP packets must come
*from* `lb1`, or the far end will reject them as arriving from an unknown
neighbor. Setting the update source to `lb1` gives you a session that rides
the IGP — the preloaded IS-IS instance `Bootcamp` already advertises both
/32 loopbacks, so as long as *any* path exists the session survives
individual link events. The MD5 password (`ciena123` on both sides) protects
the TCP layer: segments that fail the digest are silently discarded, so a
mismatch never even reaches BGP.

**Implementation** — On each PE: define the `ipv4 unicast` address family
under the instance, create the peer with the remote loopback and remote-as,
activate `ipv4 unicast` for it with inbound soft-reconfiguration (so
received routes are retained pre-policy for inspection), set the
update-source interface to `lb1`, and set the password.

**Configure** (config mode) on **PE_1**:

```saos-config
bgp instance 65032 address-family ipv4 unicast
    exit
  exit
exit
bgp instance 65032 peer 172.16.0.2 remote-as 65032
bgp instance 65032 peer 172.16.0.2 address-family ipv4 unicast activate true soft-reconfiguration-inbound true
bgp instance 65032 peer 172.16.0.2 update-source-interface lb1
bgp instance 65032 peer 172.16.0.2 password ciena123
```

**Configure** (config mode) on **PE_2**:

```saos-config
bgp instance 65032 address-family ipv4 unicast
    exit
  exit
exit
bgp instance 65032 peer 172.16.0.1 remote-as 65032
bgp instance 65032 peer 172.16.0.1 address-family ipv4 unicast activate true soft-reconfiguration-inbound true
bgp instance 65032 peer 172.16.0.1 update-source-interface lb1
bgp instance 65032 peer 172.16.0.1 password ciena123
```

<!-- verify-prose -->

`show bgp` should now render a real table containing AS `65032` and the
local router-id — this retroactively proves Task 1 as well. The peer view
should show the remote loopback in state `Established`, and the per-peer
detail should confirm the update source is `lb1`. `Established` is doing
double duty here: it is the *only* proof of the MD5 configuration, because a
password mismatch simply keeps TCP from completing, leaving the peer stuck
below Established. Allow some time; the checks retry for up to 180 seconds.

Teaching question: if only one side had set the password, what state would
you expect the session to sit in — and would either side log a BGP-level
error, or nothing at all?

<!-- retry: 90s -->
**Verify** (show mode) on **PE_1**:

```saos-show
show bgp
```

Pass: Output contains `65032` and `172.16.0.1`

<details><summary>Example output</summary>

```
+------------------- BGP --------------------+
| Name                          | Value      |
+-------------------------------+------------+
| AS                            | 65032      |
| IPv4 Prefix Count             | 2          |
| IPv6 Prefix Count             | 0          |
| Router ID                     | 172.16.0.1 |
| Route Selection Options       |            |
|  AIGP-Ignore                  | False      |
| AIGP Threshold                | 0          |
| Graceful Restart              |            |
|  Enable                       | False      |
|  Stalepath Time (s)           | 360        |
|  Restart Time (s)             | 120        |
|  Deferral Time (s)            | 120        |
| Table version                 |            |
|  IPv4 Unicast                 | 3          |
|  IPv4 Labeled Unicast         | 3          |
|  IPv4 MVPN                    | -          |
|  IPv6 Unicast                 | -          |
|  IPv6 Labeled Unicast         | -          |
|  VPNv4 Unicast                | 1          |
|  VPNv6 Unicast                | 1          |
|  L2VPN EVPN                   | 1          |
|  L2VPN VPLS                   | -          |
|  RTfilter UNICAST             | -          |
| MPLS Resolution               | False      |
| Add Path Select Diverse Count |            |
|  IPv4 Labeled Unicast         | -          |
|  VPNv4 Unicast                | -          |
|  VPNv6 Unicast                | -          |
| Add Path Diverse Advertise    |            |
|  IPv4 Labeled Unicast         | False      |
|  VPNv4 Unicast                | False      |
|  VPNv6 Unicast                | False      |
| Update Error handling         |            |
|  Enable                       | False      |
|  Malformed Route Limit        | 1000       |
|  Malformed Log Interval       | 300        |
|  Malformed Route Stored       | -          |
+-------------------------------+------------+
```

</details>

<!-- retry: 90s -->
**Verify** (show mode) on **PE_2**:

```saos-show
show bgp
```

Pass: Output contains `65032` and `172.16.0.2`

<details><summary>Example output</summary>

```
+------------------- BGP --------------------+
| Name                          | Value      |
+-------------------------------+------------+
| AS                            | 65032      |
| IPv4 Prefix Count             | 2          |
| IPv6 Prefix Count             | 0          |
| Router ID                     | 172.16.0.2 |
| Route Selection Options       |            |
|  AIGP-Ignore                  | False      |
| AIGP Threshold                | 0          |
| Graceful Restart              |            |
|  Enable                       | False      |
|  Stalepath Time (s)           | 360        |
|  Restart Time (s)             | 120        |
|  Deferral Time (s)            | 120        |
| Table version                 |            |
|  IPv4 Unicast                 | 3          |
|  IPv4 Labeled Unicast         | 3          |
|  IPv4 MVPN                    | -          |
|  IPv6 Unicast                 | -          |
|  IPv6 Labeled Unicast         | -          |
|  VPNv4 Unicast                | 1          |
|  VPNv6 Unicast                | 1          |
|  L2VPN EVPN                   | 1          |
|  L2VPN VPLS                   | -          |
|  RTfilter UNICAST             | -          |
| MPLS Resolution               | False      |
| Add Path Select Diverse Count |            |
|  IPv4 Labeled Unicast         | -          |
|  VPNv4 Unicast                | -          |
|  VPNv6 Unicast                | -          |
| Add Path Diverse Advertise    |            |
|  IPv4 Labeled Unicast         | False      |
|  VPNv4 Unicast                | False      |
|  VPNv6 Unicast                | False      |
| Update Error handling         |            |
|  Enable                       | False      |
|  Malformed Route Limit        | 1000       |
|  Malformed Log Interval       | 300        |
|  Malformed Route Stored       | -          |
+-------------------------------+------------+
```

</details>

<!-- retry: 180s -->
**Verify** (show mode) on **PE_1**:

```saos-show
show bgp peers
```

Pass: Output contains `172.16.0.2` and `Established`

<details><summary>Example output</summary>

```
+-------------------------------------------------------------------------- BGP PEERS --------------------------------------------------------------------------+
|                                             |        |          | Up         | Peer    | Received | Advertised | Last       | Received | Sent   |             |
|                                             | Remote | Peer     | Time       | Table   | Pkt      | Pkt        | Reset      | Prefix   | Prefix |             |
| Peer                                        | AS     | Type     | (hh:mm:ss) | Version | Count    | Count      | (hh:mm:ss) | Count    | Count  | State       |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
| 172.16.0.2                                  | 65032  | internal | 00:00:21   | 2       | 5        | 5          | 00:00:21   | 1        | 1      | Established |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
```

</details>

<!-- retry: 180s -->
**Verify** (show mode) on **PE_1**:

```saos-show
show bgp peers peer 172.16.0.2
```

Pass: Output contains `Established` and `Update Source` and `lb1`

<details><summary>Example output</summary>

```
+------------------------------------------ BGP PEER ------------------------------------------+
| Name                                  | Value                                                |
+---------------------------------------+------------------------------------------------------+
| Peer                                  | 172.16.0.2                                           |
| Remote AS                             | 65032                                                |
| Remote Router ID                      | 172.16.0.2                                           |
| Received Pkt Count                    | 5                                                    |
| Advertised Pkt Count                  | 5                                                    |
| Next Hop                              | 172.16.0.1                                           |
| Next Hop Global                       | fc00::1                                              |
| Next Hop Local                        | ::                                                   |
| Remote Port                           | 44183                                                |
| Remote Address                        | 172.16.0.2                                           |
| Local Port                            | 179                                                  |
| Connections Established               | 2                                                    |
| Connections Dropped                   | 1                                                    |
| Open Msg Received                     | 1                                                    |
| Open Msg Sent                         | 1                                                    |
| Update Msg Received                   | 4                                                    |
| Update Msg Sent                       | 4                                                    |
| Last Reset (hh:mm:ss)                 | 00:00:21                                             |
| Connection                            | non shared network                                   |
| Up Time (hh:mm:ss)                    | 00:00:21                                             |
| Read Time (hh:mm:ss)                  | 00:00:21                                             |
| Peer Type                             | internal                                             |
| Notifications Sent                    | 1                                                    |
| Notification Direction                | sent                                                 |
| Last Notification Error Message       | (Cease/Other Configuration Change.)                  |
| Configured Hold Time (s)              | 180                                                  |
| Configured Keepalive Interval (s)     | 60                                                   |
| Oper Hold Time (s)                    | 180                                                  |
| Oper Keepalive Interval (s)           | 60                                                   |
| Update Source                         | lb1                                                  |
| Minimum Advertisement Interval        | 0                                                    |
| IPv4 Unicast Support                  | advertised and received                              |
| IPv6 Unicast Support                  | -                                                    |
| VPNv4 Unicast Support                 | advertised and received                              |
| VPNv6 Unicast Support                 | -                                                    |
| L2VPN EVPN Unicast Support            | advertised and received                              |
| L2VPN VPLS Unicast Support            | -                                                    |
| RTFilter Unicast Support              | -                                                    |
| State                                 | Established                                          |
| Shutdown                              | False                                                |
| Peer Flap Counter                     | 1                                                    |
| Peer Restart Time (s)                 | 0                                                    |
| Peer Restarting                       | false                                                |
| Connect Retry Interval (s)            | 120                                                  |
| Last Reset Information                |                                                      |
| Last Update Read (s)                  | 11                                                   |
| Last Update Read Before Reset (s)     | 0                                                    |
| Last Write (s)                        | 11                                                   |
| Last Written (bytes)                  | 23                                                   |
| Second Last Write (s)                 | 11                                                   |
| Second Last Written (bytes)           | 56                                                   |
| Last Write Before Reset (s)           | 21                                                   |
| Second Last Write Before Reset (s)    | 32                                                   |
| Current Holdtimer Reset (s)           | 11                                                   |
| Last Holdtimer Reset (s)              | 0                                                    |
| Lockout                               | Disabled                                             |
| Local AS                              | -                                                    |
| Last MD5 Failure Reason               | -                                                    |
| Last MD5 Failure Time (hh:mm:ss)      | -                                                    |
| Address Family 1                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 1                                                    |
|  Sent Prefix Count                    | 1                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | True                                                 |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_3                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 2                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | labeled-unicast                                      |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_5                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 3                      |                                                      |
|  AFI                                  | vpnv4                                                |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_7                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 4                      |                                                      |
|  AFI                                  | l2vpn                                                |
|  SAFI                                 | evpn                                                 |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | false                                                |
|  GR Capability Advertised             | false                                                |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | false                                                |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_9                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| BGP BFD Configuration                 | Disabled                                             |
| EBGP Multi-Hop Operational            | Disabled                                             |
+---------------------------------------+------------------------------------------------------+
```

</details>

<!-- retry: 180s -->
**Verify** (show mode) on **PE_2**:

```saos-show
show bgp peers
```

Pass: Output contains `172.16.0.1` and `Established`

<details><summary>Example output</summary>

```
+-------------------------------------------------------------------------- BGP PEERS --------------------------------------------------------------------------+
|                                             |        |          | Up         | Peer    | Received | Advertised | Last       | Received | Sent   |             |
|                                             | Remote | Peer     | Time       | Table   | Pkt      | Pkt        | Reset      | Prefix   | Prefix |             |
| Peer                                        | AS     | Type     | (hh:mm:ss) | Version | Count    | Count      | (hh:mm:ss) | Count    | Count  | State       |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
| 172.16.0.1                                  | 65032  | internal | 00:00:22   | 2       | 6        | 6          | 00:00:27   | 1        | 1      | Established |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
```

</details>

<!-- retry: 180s -->
**Verify** (show mode) on **PE_2**:

```saos-show
show bgp peers peer 172.16.0.1
```

Pass: Output contains `Established` and `Update Source` and `lb1`

<details><summary>Example output</summary>

```
+------------------------------------------ BGP PEER ------------------------------------------+
| Name                                  | Value                                                |
+---------------------------------------+------------------------------------------------------+
| Peer                                  | 172.16.0.1                                           |
| Remote AS                             | 65032                                                |
| Remote Router ID                      | 172.16.0.1                                           |
| Received Pkt Count                    | 6                                                    |
| Advertised Pkt Count                  | 6                                                    |
| Next Hop                              | 172.16.0.2                                           |
| Next Hop Global                       | fc00::2                                              |
| Next Hop Local                        | ::                                                   |
| Remote Port                           | 179                                                  |
| Remote Address                        | 172.16.0.1                                           |
| Local Port                            | 44183                                                |
| Connections Established               | 2                                                    |
| Connections Dropped                   | 1                                                    |
| Open Msg Received                     | 1                                                    |
| Open Msg Sent                         | 1                                                    |
| Update Msg Received                   | 4                                                    |
| Update Msg Sent                       | 4                                                    |
| Keepalives Received                   | 1                                                    |
| Keepalives Sent                       | 1                                                    |
| Last Reset (hh:mm:ss)                 | 00:00:27                                             |
| Connection                            | non shared network                                   |
| Up Time (hh:mm:ss)                    | 00:00:22                                             |
| Read Time (hh:mm:ss)                  | 00:00:22                                             |
| Peer Type                             | internal                                             |
| Notifications Received                | 1                                                    |
| Notification Direction                | received                                             |
| Last Notification Error Message       | (Cease/Other Configuration Change.)                  |
| Configured Hold Time (s)              | 180                                                  |
| Configured Keepalive Interval (s)     | 60                                                   |
| Oper Hold Time (s)                    | 180                                                  |
| Oper Keepalive Interval (s)           | 60                                                   |
| Update Source                         | lb1                                                  |
| Minimum Advertisement Interval        | 0                                                    |
| IPv4 Unicast Support                  | advertised and received                              |
| IPv6 Unicast Support                  | -                                                    |
| VPNv4 Unicast Support                 | advertised and received                              |
| VPNv6 Unicast Support                 | -                                                    |
| L2VPN EVPN Unicast Support            | advertised and received                              |
| L2VPN VPLS Unicast Support            | -                                                    |
| RTFilter Unicast Support              | -                                                    |
| State                                 | Established                                          |
| Shutdown                              | False                                                |
| Peer Flap Counter                     | 1                                                    |
| Peer Restart Time (s)                 | 0                                                    |
| Peer Restarting                       | false                                                |
| Connect Retry Interval (s)            | 120                                                  |
| Last Reset Information                |                                                      |
| Last Update Read (s)                  | 12                                                   |
| Last Update Read Before Reset (s)     | 27                                                   |
| Last Write (s)                        | 12                                                   |
| Last Written (bytes)                  | 23                                                   |
| Second Last Write (s)                 | 12                                                   |
| Second Last Written (bytes)           | 56                                                   |
| Last Write Before Reset (s)           | 34                                                   |
| Second Last Write Before Reset (s)    | 0                                                    |
| Current Holdtimer Reset (s)           | 12                                                   |
| Last Holdtimer Reset (s)              | 27                                                   |
| Lockout                               | Disabled                                             |
| Local AS                              | -                                                    |
| Last MD5 Failure Reason               | -                                                    |
| Last MD5 Failure Time (hh:mm:ss)      | -                                                    |
| Address Family 1                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 1                                                    |
|  Sent Prefix Count                    | 1                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | True                                                 |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_3                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 2                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | labeled-unicast                                      |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_5                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 3                      |                                                      |
|  AFI                                  | vpnv4                                                |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_7                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 4                      |                                                      |
|  AFI                                  | l2vpn                                                |
|  SAFI                                 | evpn                                                 |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | false                                                |
|  GR Capability Advertised             | false                                                |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | false                                                |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_9                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| BGP BFD Configuration                 | Disabled                                             |
| EBGP Multi-Hop Operational            | Disabled                                             |
+---------------------------------------+------------------------------------------------------+
```

</details>

<a id="task-3"></a>
### Task 3: Enable multiprotocol BGP
<a href="#task-3" title="Direct link to this task (right-click to copy)">🔗</a>

<!-- prose: in-depth -->

**Summary** — Here you add three families to the instance and activate each
for the peer: `vpnv4 unicast`, `l2vpn evpn`, and `ipv4 labeled-unicast`.
Nothing new is advertised yet — these are empty pipes — but they are the
control planes the later service labs depend on.

**Background** — One BGP session can carry many kinds of reachability.
Multiprotocol BGP negotiates *capabilities* per session: at open time each
side lists the address families it has activated, and only the families both
sides agree on are exchanged. vpnv4 carries L3VPN routes, EVPN carries the
routes behind VPWS/ELAN services, and labeled-unicast lets BGP itself
distribute MPLS labels with prefixes.

**Implementation** — On each PE, define the three address families under
instance `65032`, then activate each of them on the existing peer. Both ends
must activate a family for it to be negotiated.

**Configure** (config mode) on **PE_1**:

```saos-config
bgp instance 65032 address-family vpnv4 unicast
    exit
  exit
exit
bgp instance 65032 address-family l2vpn evpn
    exit
  exit
exit
bgp instance 65032 address-family ipv4 labeled-unicast
    exit
  exit
exit
bgp instance 65032 peer 172.16.0.2 address-family vpnv4 unicast activate true
bgp instance 65032 peer 172.16.0.2 address-family l2vpn evpn activate true
bgp instance 65032 peer 172.16.0.2 address-family ipv4 labeled-unicast activate true
```

**Configure** (config mode) on **PE_2**:

```saos-config
bgp instance 65032 address-family vpnv4 unicast
    exit
  exit
exit
bgp instance 65032 address-family l2vpn evpn
    exit
  exit
exit
bgp instance 65032 address-family ipv4 labeled-unicast
    exit
  exit
exit
bgp instance 65032 peer 172.16.0.1 address-family vpnv4 unicast activate true
bgp instance 65032 peer 172.16.0.1 address-family l2vpn evpn activate true
bgp instance 65032 peer 172.16.0.1 address-family ipv4 labeled-unicast activate true
```

<!-- verify-prose -->

The per-peer detail should now list `vpnv4`, `evpn`, and `labeled-unicast`
as negotiated for the session — that listing is the negotiation result,
proving *both* sides activated them, not just the local config. Expect that
activating new families may bounce the session so capabilities can be
renegotiated in a fresh OPEN — the checks retry for up to 180 seconds to
ride this out. Did you observe a flap?

Teaching question: if you had activated `l2vpn evpn` on `PE_1` only, what
would the peer detail show on each side?

<!-- retry: 180s -->
**Verify** (show mode) on **PE_1**:

```saos-show
show bgp peers peer 172.16.0.2
```

Pass: Output contains `vpnv4` and `evpn` and `labeled-unicast`

<details><summary>Example output</summary>

```
+------------------------------------------ BGP PEER ------------------------------------------+
| Name                                  | Value                                                |
+---------------------------------------+------------------------------------------------------+
| Peer                                  | 172.16.0.2                                           |
| Remote AS                             | 65032                                                |
| Remote Router ID                      | 172.16.0.2                                           |
| Received Pkt Count                    | 5                                                    |
| Advertised Pkt Count                  | 5                                                    |
| Next Hop                              | 172.16.0.1                                           |
| Next Hop Global                       | fc00::1                                              |
| Next Hop Local                        | ::                                                   |
| Remote Port                           | 44183                                                |
| Remote Address                        | 172.16.0.2                                           |
| Local Port                            | 179                                                  |
| Connections Established               | 2                                                    |
| Connections Dropped                   | 1                                                    |
| Open Msg Received                     | 1                                                    |
| Open Msg Sent                         | 1                                                    |
| Update Msg Received                   | 4                                                    |
| Update Msg Sent                       | 4                                                    |
| Last Reset (hh:mm:ss)                 | 00:00:24                                             |
| Connection                            | non shared network                                   |
| Up Time (hh:mm:ss)                    | 00:00:24                                             |
| Read Time (hh:mm:ss)                  | 00:00:24                                             |
| Peer Type                             | internal                                             |
| Notifications Sent                    | 1                                                    |
| Notification Direction                | sent                                                 |
| Last Notification Error Message       | (Cease/Other Configuration Change.)                  |
| Configured Hold Time (s)              | 180                                                  |
| Configured Keepalive Interval (s)     | 60                                                   |
| Oper Hold Time (s)                    | 180                                                  |
| Oper Keepalive Interval (s)           | 60                                                   |
| Update Source                         | lb1                                                  |
| Minimum Advertisement Interval        | 0                                                    |
| IPv4 Unicast Support                  | advertised and received                              |
| IPv6 Unicast Support                  | -                                                    |
| VPNv4 Unicast Support                 | advertised and received                              |
| VPNv6 Unicast Support                 | -                                                    |
| L2VPN EVPN Unicast Support            | advertised and received                              |
| L2VPN VPLS Unicast Support            | -                                                    |
| RTFilter Unicast Support              | -                                                    |
| State                                 | Established                                          |
| Shutdown                              | False                                                |
| Peer Flap Counter                     | 1                                                    |
| Peer Restart Time (s)                 | 0                                                    |
| Peer Restarting                       | false                                                |
| Connect Retry Interval (s)            | 120                                                  |
| Last Reset Information                |                                                      |
| Last Update Read (s)                  | 14                                                   |
| Last Update Read Before Reset (s)     | 0                                                    |
| Last Write (s)                        | 14                                                   |
| Last Written (bytes)                  | 23                                                   |
| Second Last Write (s)                 | 14                                                   |
| Second Last Written (bytes)           | 56                                                   |
| Last Write Before Reset (s)           | 24                                                   |
| Second Last Write Before Reset (s)    | 35                                                   |
| Current Holdtimer Reset (s)           | 14                                                   |
| Last Holdtimer Reset (s)              | 0                                                    |
| Lockout                               | Disabled                                             |
| Local AS                              | -                                                    |
| Last MD5 Failure Reason               | -                                                    |
| Last MD5 Failure Time (hh:mm:ss)      | -                                                    |
| Address Family 1                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 1                                                    |
|  Sent Prefix Count                    | 1                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | True                                                 |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_3                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 2                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | labeled-unicast                                      |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_5                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 3                      |                                                      |
|  AFI                                  | vpnv4                                                |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_7                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 4                      |                                                      |
|  AFI                                  | l2vpn                                                |
|  SAFI                                 | evpn                                                 |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | false                                                |
|  GR Capability Advertised             | false                                                |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | false                                                |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_9                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| BGP BFD Configuration                 | Disabled                                             |
| EBGP Multi-Hop Operational            | Disabled                                             |
+---------------------------------------+------------------------------------------------------+
```

</details>

<!-- retry: 180s -->
**Verify** (show mode) on **PE_2**:

```saos-show
show bgp peers peer 172.16.0.1
```

Pass: Output contains `vpnv4` and `evpn` and `labeled-unicast`

<details><summary>Example output</summary>

```
+------------------------------------------ BGP PEER ------------------------------------------+
| Name                                  | Value                                                |
+---------------------------------------+------------------------------------------------------+
| Peer                                  | 172.16.0.1                                           |
| Remote AS                             | 65032                                                |
| Remote Router ID                      | 172.16.0.1                                           |
| Received Pkt Count                    | 6                                                    |
| Advertised Pkt Count                  | 6                                                    |
| Next Hop                              | 172.16.0.2                                           |
| Next Hop Global                       | fc00::2                                              |
| Next Hop Local                        | ::                                                   |
| Remote Port                           | 179                                                  |
| Remote Address                        | 172.16.0.1                                           |
| Local Port                            | 44183                                                |
| Connections Established               | 2                                                    |
| Connections Dropped                   | 1                                                    |
| Open Msg Received                     | 1                                                    |
| Open Msg Sent                         | 1                                                    |
| Update Msg Received                   | 4                                                    |
| Update Msg Sent                       | 4                                                    |
| Keepalives Received                   | 1                                                    |
| Keepalives Sent                       | 1                                                    |
| Last Reset (hh:mm:ss)                 | 00:00:30                                             |
| Connection                            | non shared network                                   |
| Up Time (hh:mm:ss)                    | 00:00:25                                             |
| Read Time (hh:mm:ss)                  | 00:00:25                                             |
| Peer Type                             | internal                                             |
| Notifications Received                | 1                                                    |
| Notification Direction                | received                                             |
| Last Notification Error Message       | (Cease/Other Configuration Change.)                  |
| Configured Hold Time (s)              | 180                                                  |
| Configured Keepalive Interval (s)     | 60                                                   |
| Oper Hold Time (s)                    | 180                                                  |
| Oper Keepalive Interval (s)           | 60                                                   |
| Update Source                         | lb1                                                  |
| Minimum Advertisement Interval        | 0                                                    |
| IPv4 Unicast Support                  | advertised and received                              |
| IPv6 Unicast Support                  | -                                                    |
| VPNv4 Unicast Support                 | advertised and received                              |
| VPNv6 Unicast Support                 | -                                                    |
| L2VPN EVPN Unicast Support            | advertised and received                              |
| L2VPN VPLS Unicast Support            | -                                                    |
| RTFilter Unicast Support              | -                                                    |
| State                                 | Established                                          |
| Shutdown                              | False                                                |
| Peer Flap Counter                     | 1                                                    |
| Peer Restart Time (s)                 | 0                                                    |
| Peer Restarting                       | false                                                |
| Connect Retry Interval (s)            | 120                                                  |
| Last Reset Information                |                                                      |
| Last Update Read (s)                  | 15                                                   |
| Last Update Read Before Reset (s)     | 30                                                   |
| Last Write (s)                        | 15                                                   |
| Last Written (bytes)                  | 23                                                   |
| Second Last Write (s)                 | 15                                                   |
| Second Last Written (bytes)           | 56                                                   |
| Last Write Before Reset (s)           | 37                                                   |
| Second Last Write Before Reset (s)    | 0                                                    |
| Current Holdtimer Reset (s)           | 15                                                   |
| Last Holdtimer Reset (s)              | 30                                                   |
| Lockout                               | Disabled                                             |
| Local AS                              | -                                                    |
| Last MD5 Failure Reason               | -                                                    |
| Last MD5 Failure Time (hh:mm:ss)      | -                                                    |
| Address Family 1                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 1                                                    |
|  Sent Prefix Count                    | 1                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | True                                                 |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_3                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 2                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | labeled-unicast                                      |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_5                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 3                      |                                                      |
|  AFI                                  | vpnv4                                                |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_7                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 4                      |                                                      |
|  AFI                                  | l2vpn                                                |
|  SAFI                                 | evpn                                                 |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | false                                                |
|  GR Capability Advertised             | false                                                |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | false                                                |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_9                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| BGP BFD Configuration                 | Disabled                                             |
| EBGP Multi-Hop Operational            | Disabled                                             |
+---------------------------------------+------------------------------------------------------+
```

</details>

<a id="task-4"></a>
### Task 4: Redistribute a policy-controlled loopback
<a href="#task-4" title="Direct link to this task (right-click to copy)">🔗</a>

<!-- prose: in-depth -->

**Summary** — BGP is only useful once it carries routes. This task
originates one prefix per PE — a new loopback `lb10` (`10.65.0.32/32` on
`PE_1`, `10.65.0.33/32` on `PE_2`) — by redistributing connected routes into
`ipv4 unicast`, gated by a route policy that also tags the route with a
community.

**Background** — Bare "redistribute connected" would leak everything
connected: `lb1`'s /32 and the core link included, which is why the policy
gate matters. The community is a tag riding with the route — any downstream
policy can later match `65032:100` instead of maintaining prefix lists; it
is the standard way intent travels with a route.

**Implementation** — On each PE: create loopback `lb10` with its /32, then
build the policy chain — a prefix-list matches exactly the new /32; the
policy's first statement permits routes matching that list and appends
standard community `65032:100`; its second statement is an explicit deny
that stops every other connected route — and attach the policy to
connected-route redistribution under the `ipv4 unicast` family.

**Configure** (config mode) on **PE_1**:

```saos-config
oc-if:interfaces interface lb10 config name lb10 type loopback
oc-if:interfaces interface lb10 ipv4 addresses address 10.65.0.32 config ip 10.65.0.32 prefix-length 32
routing-policy prefix-lists prefix-list lb10 mode ipv4 sequence 1 action permit ip-prefix 10.65.0.32/32
routing-policy policies policy lb10 statement 1 action permit
routing-policy policies policy lb10 statement 1 match route-entry lb10
routing-policy policies policy lb10 statement 1 set community append standard 65032:100
routing-policy policies policy lb10 statement 2 action deny
bgp instance 65032 address-family ipv4 unicast redistribute connected policy lb10
```

**Configure** (config mode) on **PE_2**:

```saos-config
oc-if:interfaces interface lb10 config name lb10 type loopback
oc-if:interfaces interface lb10 ipv4 addresses address 10.65.0.33 config ip 10.65.0.33 prefix-length 32
routing-policy prefix-lists prefix-list lb10 mode ipv4 sequence 1 action permit ip-prefix 10.65.0.33/32
routing-policy policies policy lb10 statement 1 action permit
routing-policy policies policy lb10 statement 1 match route-entry lb10
routing-policy policies policy lb10 statement 1 set community append standard 65032:100
routing-policy policies policy lb10 statement 2 action deny
bgp instance 65032 address-family ipv4 unicast redistribute connected policy lb10
```

<!-- verify-prose -->

Three layers of proof here. First, the routing table: the local /32 should
appear as a connected route on `lb10`. Second, the BGP route table on *each*
PE must contain both `10.65.0.32` and `10.65.0.33` — seeing the *remote*
PE's loopback is the key evidence, because a learned route can only come
through the Established session; it is real protocol behavior, not an echo
of your own config. Third, filtering the BGP table by community `65032:100`
must still return the redistributed prefix, proving the policy stamped the
community during redistribution rather than merely existing in config.

Teaching question: remove the explicit-deny statement mentally — which extra
prefixes would enter BGP, and why could redistributing the `172.16.0.x`
loopbacks alongside the IGP's copies be a problem?

**Verify** (show mode) on **PE_1**:

```saos-show
show ip routes route 10.65.0.32/32
```

Pass: Output contains `10.65.0.32` and `lb10`

<details><summary>Example output</summary>

```
+---------------------------------------------------------------------------------------+
| Codes: K - kernel, C - connected, S - static, B - BGP, O - OSPF, IA - OSPF inter area |
|        E1 - OSPF external type 1, E2 - OSPF external type 2                           |
|        I - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area       |
|        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2                 |
|        M - MPLS                                                                       |
|        > - selected route, * - FIB route, ~ - Anycast Prefix                          |
|        S/T - Sub Type, RP/M - Route Preference/Metric                                 |
+---------------------------------------------------------------------------------------+
+------------------------------------------------------------------------------- RIB STATE: default -------------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
| *>    |  C   |  -  | -                | 10.65.0.32/32      | [0/0]     | -               | lb10                      | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

**Verify** (show mode) on **PE_2**:

```saos-show
show ip routes route 10.65.0.33/32
```

Pass: Output contains `10.65.0.33` and `lb10`

<details><summary>Example output</summary>

```
+---------------------------------------------------------------------------------------+
| Codes: K - kernel, C - connected, S - static, B - BGP, O - OSPF, IA - OSPF inter area |
|        E1 - OSPF external type 1, E2 - OSPF external type 2                           |
|        I - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area       |
|        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2                 |
|        M - MPLS                                                                       |
|        > - selected route, * - FIB route, ~ - Anycast Prefix                          |
|        S/T - Sub Type, RP/M - Route Preference/Metric                                 |
+---------------------------------------------------------------------------------------+
+------------------------------------------------------------------------------- RIB STATE: default -------------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
| *>    |  C   |  -  | -                | 10.65.0.33/32      | [0/0]     | -               | lb10                      | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 120s -->
**Verify** (show mode) on **PE_1**:

```saos-show
show bgp routes
```

Pass: Output contains `10.65.0.32` and `10.65.0.33`

<details><summary>Example output</summary>

```
+----------------------------------------------------------------------------------+
| Status codes: s suppressed, d damped, h history, a add-path,                     |
|               * valid, > best, i - internal, l - labeled, S Stale                |
|               m - multipath candidate, t - evpn route type 5, D add-path-diverse |
|               M - malformed                                                      |
| Origin codes: i - IGP, e - EGP, ? - incomplete                                   |
+----------------------------------------------------------------------------------+
+------------------------------------------------------- BGP IPV4 ROUTES -------------------------------------------------------+
|          | Table   |                    |                 |     |             |                  |        |         | AS Path |
| Flags    | Version | Network            | Next Hop        | MED | iBGP Metric | Local Preference | Weight | AS Path | Origin  |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
| *>       | 2       | 10.65.0.32/32      | 0.0.0.0         | 0   | 0           | 100              | 32768  | Local   | ?       |
| *>i      | 3       | 10.65.0.33/32      | 172.16.0.2      | 0   | 20          | 100              | 0      | Local   | ?       |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
```

</details>

<!-- retry: 90s -->
**Verify** (show mode) on **PE_1**:

```saos-show
show bgp routes ipv4 unicast community 65032:100
```

Pass: Output contains `10.65.0.32`

<details><summary>Example output</summary>

```
+----------------------------------------------------------------------------------+
| Status codes: s suppressed, d damped, h history, a add-path,                     |
|               * valid, > best, i - internal, l - labeled, S Stale                |
|               m - multipath candidate, t - evpn route type 5, D add-path-diverse |
|               M - malformed                                                      |
| Origin codes: i - IGP, e - EGP, ? - incomplete                                   |
+----------------------------------------------------------------------------------+
+------------------------------------------------------- BGP IPV4 ROUTES -------------------------------------------------------+
|          | Table   |                    |                 |     |             |                  |        |         | AS Path |
| Flags    | Version | Network            | Next Hop        | MED | iBGP Metric | Local Preference | Weight | AS Path | Origin  |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
| *>       | 2       | 10.65.0.32/32      | 0.0.0.0         | 0   | 0           | 100              | 32768  | Local   | ?       |
| *>i      | 3       | 10.65.0.33/32      | 172.16.0.2      | 0   | 20          | 100              | 0      | Local   | ?       |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
```

</details>

<!-- retry: 120s -->
**Verify** (show mode) on **PE_2**:

```saos-show
show bgp routes
```

Pass: Output contains `10.65.0.33` and `10.65.0.32`

<details><summary>Example output</summary>

```
+----------------------------------------------------------------------------------+
| Status codes: s suppressed, d damped, h history, a add-path,                     |
|               * valid, > best, i - internal, l - labeled, S Stale                |
|               m - multipath candidate, t - evpn route type 5, D add-path-diverse |
|               M - malformed                                                      |
| Origin codes: i - IGP, e - EGP, ? - incomplete                                   |
+----------------------------------------------------------------------------------+
+------------------------------------------------------- BGP IPV4 ROUTES -------------------------------------------------------+
|          | Table   |                    |                 |     |             |                  |        |         | AS Path |
| Flags    | Version | Network            | Next Hop        | MED | iBGP Metric | Local Preference | Weight | AS Path | Origin  |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
| *>i      | 3       | 10.65.0.32/32      | 172.16.0.1      | 0   | 20          | 100              | 0      | Local   | ?       |
| *>       | 2       | 10.65.0.33/32      | 0.0.0.0         | 0   | 0           | 100              | 32768  | Local   | ?       |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
```

</details>

<!-- retry: 90s -->
**Verify** (show mode) on **PE_2**:

```saos-show
show bgp routes ipv4 unicast community 65032:100
```

Pass: Output contains `10.65.0.33`

<details><summary>Example output</summary>

```
+----------------------------------------------------------------------------------+
| Status codes: s suppressed, d damped, h history, a add-path,                     |
|               * valid, > best, i - internal, l - labeled, S Stale                |
|               m - multipath candidate, t - evpn route type 5, D add-path-diverse |
|               M - malformed                                                      |
| Origin codes: i - IGP, e - EGP, ? - incomplete                                   |
+----------------------------------------------------------------------------------+
+------------------------------------------------------- BGP IPV4 ROUTES -------------------------------------------------------+
|          | Table   |                    |                 |     |             |                  |        |         | AS Path |
| Flags    | Version | Network            | Next Hop        | MED | iBGP Metric | Local Preference | Weight | AS Path | Origin  |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
| *>i      | 3       | 10.65.0.32/32      | 172.16.0.1      | 0   | 20          | 100              | 0      | Local   | ?       |
| *>       | 2       | 10.65.0.33/32      | 0.0.0.0         | 0   | 0           | 100              | 32768  | Local   | ?       |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
```

</details>

<a id="task-5"></a>
### Task 5: Verify BGP over SR-MPLS
<a href="#task-5" title="Direct link to this task (right-click to copy)">🔗</a>

<!-- prose: detailed -->

**Summary** — Nothing new is configured in this task — it closes the loop on
what the preloaded underlay has been doing for you all along. Your iBGP
session is loopback-to-loopback, so every BGP packet — and every packet
toward a BGP-learned route whose next hop is the remote `lb1` — resolves
through the SR-MPLS underlay. The point of this task is to *see* that
resolution.

**Implementation** — Nothing to build: the startup partials carry a full
SR-MPLS underlay — IS-IS instance `Bootcamp` with segment routing enabled,
SRGB `16000`–`23999`, prefix-SIDs index `1` and `2` mapped to the two `lb1`
/32s, and label switching on `PE_1-PE_2-if` and `lb1` — so inspect the
route to the remote loopback, the segment-routing and MPLS forwarding
state, and how the BGP-learned routes resolve through them.

<!-- verify-prose -->

Walk the resolution chain and check each expectation. The route to the
remote `lb1` /32 should be an IS-IS route, not connected or static — that is
what "the session rides the IGP" means concretely. The BGP-learned `lb10`
prefixes should recurse onto that same IS-IS next hop. With SRGB base
`16000` and prefix-SID indexes `1` and `2`, what label would you expect each
PE to use toward the other's loopback? Inspect the MPLS forwarding and
segment-routing state and confirm the arithmetic. Expect a ping sourced from
the local `lb1` to the remote `lb1` to succeed — the same path the BGP
session's TCP stream takes.

Teaching question: if the `PE_1`–`PE_2` link failed but another IGP path
existed, which of these would change — the BGP session state, the BGP
routes, the labels in use?

## Tests

Deploy `F4-BGP`, then run the following validation checks.

### G1: Task 2 — Establish authenticated iBGP

<!-- retry: 90s -->
On **PE_1**, run:

```saos
show bgp
```

Pass: Output contains `65032` and `172.16.0.1`

<details><summary>Example output</summary>

```
+------------------- BGP --------------------+
| Name                          | Value      |
+-------------------------------+------------+
| AS                            | 65032      |
| IPv4 Prefix Count             | 2          |
| IPv6 Prefix Count             | 0          |
| Router ID                     | 172.16.0.1 |
| Route Selection Options       |            |
|  AIGP-Ignore                  | False      |
| AIGP Threshold                | 0          |
| Graceful Restart              |            |
|  Enable                       | False      |
|  Stalepath Time (s)           | 360        |
|  Restart Time (s)             | 120        |
|  Deferral Time (s)            | 120        |
| Table version                 |            |
|  IPv4 Unicast                 | 3          |
|  IPv4 Labeled Unicast         | 3          |
|  IPv4 MVPN                    | -          |
|  IPv6 Unicast                 | -          |
|  IPv6 Labeled Unicast         | -          |
|  VPNv4 Unicast                | 1          |
|  VPNv6 Unicast                | 1          |
|  L2VPN EVPN                   | 1          |
|  L2VPN VPLS                   | -          |
|  RTfilter UNICAST             | -          |
| MPLS Resolution               | False      |
| Add Path Select Diverse Count |            |
|  IPv4 Labeled Unicast         | -          |
|  VPNv4 Unicast                | -          |
|  VPNv6 Unicast                | -          |
| Add Path Diverse Advertise    |            |
|  IPv4 Labeled Unicast         | False      |
|  VPNv4 Unicast                | False      |
|  VPNv6 Unicast                | False      |
| Update Error handling         |            |
|  Enable                       | False      |
|  Malformed Route Limit        | 1000       |
|  Malformed Log Interval       | 300        |
|  Malformed Route Stored       | -          |
+-------------------------------+------------+
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
show bgp
```

Pass: Output contains `65032` and `172.16.0.2`

<details><summary>Example output</summary>

```
+------------------- BGP --------------------+
| Name                          | Value      |
+-------------------------------+------------+
| AS                            | 65032      |
| IPv4 Prefix Count             | 2          |
| IPv6 Prefix Count             | 0          |
| Router ID                     | 172.16.0.2 |
| Route Selection Options       |            |
|  AIGP-Ignore                  | False      |
| AIGP Threshold                | 0          |
| Graceful Restart              |            |
|  Enable                       | False      |
|  Stalepath Time (s)           | 360        |
|  Restart Time (s)             | 120        |
|  Deferral Time (s)            | 120        |
| Table version                 |            |
|  IPv4 Unicast                 | 3          |
|  IPv4 Labeled Unicast         | 3          |
|  IPv4 MVPN                    | -          |
|  IPv6 Unicast                 | -          |
|  IPv6 Labeled Unicast         | -          |
|  VPNv4 Unicast                | 1          |
|  VPNv6 Unicast                | 1          |
|  L2VPN EVPN                   | 1          |
|  L2VPN VPLS                   | -          |
|  RTfilter UNICAST             | -          |
| MPLS Resolution               | False      |
| Add Path Select Diverse Count |            |
|  IPv4 Labeled Unicast         | -          |
|  VPNv4 Unicast                | -          |
|  VPNv6 Unicast                | -          |
| Add Path Diverse Advertise    |            |
|  IPv4 Labeled Unicast         | False      |
|  VPNv4 Unicast                | False      |
|  VPNv6 Unicast                | False      |
| Update Error handling         |            |
|  Enable                       | False      |
|  Malformed Route Limit        | 1000       |
|  Malformed Log Interval       | 300        |
|  Malformed Route Stored       | -          |
+-------------------------------+------------+
```

</details>

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show bgp peers
```

Pass: Output contains `172.16.0.2` and `Established`

<details><summary>Example output</summary>

```
+-------------------------------------------------------------------------- BGP PEERS --------------------------------------------------------------------------+
|                                             |        |          | Up         | Peer    | Received | Advertised | Last       | Received | Sent   |             |
|                                             | Remote | Peer     | Time       | Table   | Pkt      | Pkt        | Reset      | Prefix   | Prefix |             |
| Peer                                        | AS     | Type     | (hh:mm:ss) | Version | Count    | Count      | (hh:mm:ss) | Count    | Count  | State       |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
| 172.16.0.2                                  | 65032  | internal | 00:00:21   | 2       | 5        | 5          | 00:00:21   | 1        | 1      | Established |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show bgp peers peer 172.16.0.2
```

Pass: Output contains `Established` and `Update Source` and `lb1`

<details><summary>Example output</summary>

```
+------------------------------------------ BGP PEER ------------------------------------------+
| Name                                  | Value                                                |
+---------------------------------------+------------------------------------------------------+
| Peer                                  | 172.16.0.2                                           |
| Remote AS                             | 65032                                                |
| Remote Router ID                      | 172.16.0.2                                           |
| Received Pkt Count                    | 5                                                    |
| Advertised Pkt Count                  | 5                                                    |
| Next Hop                              | 172.16.0.1                                           |
| Next Hop Global                       | fc00::1                                              |
| Next Hop Local                        | ::                                                   |
| Remote Port                           | 44183                                                |
| Remote Address                        | 172.16.0.2                                           |
| Local Port                            | 179                                                  |
| Connections Established               | 2                                                    |
| Connections Dropped                   | 1                                                    |
| Open Msg Received                     | 1                                                    |
| Open Msg Sent                         | 1                                                    |
| Update Msg Received                   | 4                                                    |
| Update Msg Sent                       | 4                                                    |
| Last Reset (hh:mm:ss)                 | 00:00:21                                             |
| Connection                            | non shared network                                   |
| Up Time (hh:mm:ss)                    | 00:00:21                                             |
| Read Time (hh:mm:ss)                  | 00:00:21                                             |
| Peer Type                             | internal                                             |
| Notifications Sent                    | 1                                                    |
| Notification Direction                | sent                                                 |
| Last Notification Error Message       | (Cease/Other Configuration Change.)                  |
| Configured Hold Time (s)              | 180                                                  |
| Configured Keepalive Interval (s)     | 60                                                   |
| Oper Hold Time (s)                    | 180                                                  |
| Oper Keepalive Interval (s)           | 60                                                   |
| Update Source                         | lb1                                                  |
| Minimum Advertisement Interval        | 0                                                    |
| IPv4 Unicast Support                  | advertised and received                              |
| IPv6 Unicast Support                  | -                                                    |
| VPNv4 Unicast Support                 | advertised and received                              |
| VPNv6 Unicast Support                 | -                                                    |
| L2VPN EVPN Unicast Support            | advertised and received                              |
| L2VPN VPLS Unicast Support            | -                                                    |
| RTFilter Unicast Support              | -                                                    |
| State                                 | Established                                          |
| Shutdown                              | False                                                |
| Peer Flap Counter                     | 1                                                    |
| Peer Restart Time (s)                 | 0                                                    |
| Peer Restarting                       | false                                                |
| Connect Retry Interval (s)            | 120                                                  |
| Last Reset Information                |                                                      |
| Last Update Read (s)                  | 11                                                   |
| Last Update Read Before Reset (s)     | 0                                                    |
| Last Write (s)                        | 11                                                   |
| Last Written (bytes)                  | 23                                                   |
| Second Last Write (s)                 | 11                                                   |
| Second Last Written (bytes)           | 56                                                   |
| Last Write Before Reset (s)           | 21                                                   |
| Second Last Write Before Reset (s)    | 32                                                   |
| Current Holdtimer Reset (s)           | 11                                                   |
| Last Holdtimer Reset (s)              | 0                                                    |
| Lockout                               | Disabled                                             |
| Local AS                              | -                                                    |
| Last MD5 Failure Reason               | -                                                    |
| Last MD5 Failure Time (hh:mm:ss)      | -                                                    |
| Address Family 1                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 1                                                    |
|  Sent Prefix Count                    | 1                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | True                                                 |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_3                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 2                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | labeled-unicast                                      |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_5                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 3                      |                                                      |
|  AFI                                  | vpnv4                                                |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_7                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 4                      |                                                      |
|  AFI                                  | l2vpn                                                |
|  SAFI                                 | evpn                                                 |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | false                                                |
|  GR Capability Advertised             | false                                                |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | false                                                |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_9                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| BGP BFD Configuration                 | Disabled                                             |
| EBGP Multi-Hop Operational            | Disabled                                             |
+---------------------------------------+------------------------------------------------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show bgp peers
```

Pass: Output contains `172.16.0.1` and `Established`

<details><summary>Example output</summary>

```
+-------------------------------------------------------------------------- BGP PEERS --------------------------------------------------------------------------+
|                                             |        |          | Up         | Peer    | Received | Advertised | Last       | Received | Sent   |             |
|                                             | Remote | Peer     | Time       | Table   | Pkt      | Pkt        | Reset      | Prefix   | Prefix |             |
| Peer                                        | AS     | Type     | (hh:mm:ss) | Version | Count    | Count      | (hh:mm:ss) | Count    | Count  | State       |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
| 172.16.0.1                                  | 65032  | internal | 00:00:22   | 2       | 6        | 6          | 00:00:27   | 1        | 1      | Established |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show bgp peers peer 172.16.0.1
```

Pass: Output contains `Established` and `Update Source` and `lb1`

<details><summary>Example output</summary>

```
+------------------------------------------ BGP PEER ------------------------------------------+
| Name                                  | Value                                                |
+---------------------------------------+------------------------------------------------------+
| Peer                                  | 172.16.0.1                                           |
| Remote AS                             | 65032                                                |
| Remote Router ID                      | 172.16.0.1                                           |
| Received Pkt Count                    | 6                                                    |
| Advertised Pkt Count                  | 6                                                    |
| Next Hop                              | 172.16.0.2                                           |
| Next Hop Global                       | fc00::2                                              |
| Next Hop Local                        | ::                                                   |
| Remote Port                           | 179                                                  |
| Remote Address                        | 172.16.0.1                                           |
| Local Port                            | 44183                                                |
| Connections Established               | 2                                                    |
| Connections Dropped                   | 1                                                    |
| Open Msg Received                     | 1                                                    |
| Open Msg Sent                         | 1                                                    |
| Update Msg Received                   | 4                                                    |
| Update Msg Sent                       | 4                                                    |
| Keepalives Received                   | 1                                                    |
| Keepalives Sent                       | 1                                                    |
| Last Reset (hh:mm:ss)                 | 00:00:27                                             |
| Connection                            | non shared network                                   |
| Up Time (hh:mm:ss)                    | 00:00:22                                             |
| Read Time (hh:mm:ss)                  | 00:00:22                                             |
| Peer Type                             | internal                                             |
| Notifications Received                | 1                                                    |
| Notification Direction                | received                                             |
| Last Notification Error Message       | (Cease/Other Configuration Change.)                  |
| Configured Hold Time (s)              | 180                                                  |
| Configured Keepalive Interval (s)     | 60                                                   |
| Oper Hold Time (s)                    | 180                                                  |
| Oper Keepalive Interval (s)           | 60                                                   |
| Update Source                         | lb1                                                  |
| Minimum Advertisement Interval        | 0                                                    |
| IPv4 Unicast Support                  | advertised and received                              |
| IPv6 Unicast Support                  | -                                                    |
| VPNv4 Unicast Support                 | advertised and received                              |
| VPNv6 Unicast Support                 | -                                                    |
| L2VPN EVPN Unicast Support            | advertised and received                              |
| L2VPN VPLS Unicast Support            | -                                                    |
| RTFilter Unicast Support              | -                                                    |
| State                                 | Established                                          |
| Shutdown                              | False                                                |
| Peer Flap Counter                     | 1                                                    |
| Peer Restart Time (s)                 | 0                                                    |
| Peer Restarting                       | false                                                |
| Connect Retry Interval (s)            | 120                                                  |
| Last Reset Information                |                                                      |
| Last Update Read (s)                  | 12                                                   |
| Last Update Read Before Reset (s)     | 27                                                   |
| Last Write (s)                        | 12                                                   |
| Last Written (bytes)                  | 23                                                   |
| Second Last Write (s)                 | 12                                                   |
| Second Last Written (bytes)           | 56                                                   |
| Last Write Before Reset (s)           | 34                                                   |
| Second Last Write Before Reset (s)    | 0                                                    |
| Current Holdtimer Reset (s)           | 12                                                   |
| Last Holdtimer Reset (s)              | 27                                                   |
| Lockout                               | Disabled                                             |
| Local AS                              | -                                                    |
| Last MD5 Failure Reason               | -                                                    |
| Last MD5 Failure Time (hh:mm:ss)      | -                                                    |
| Address Family 1                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 1                                                    |
|  Sent Prefix Count                    | 1                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | True                                                 |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_3                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 2                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | labeled-unicast                                      |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_5                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 3                      |                                                      |
|  AFI                                  | vpnv4                                                |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_7                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 4                      |                                                      |
|  AFI                                  | l2vpn                                                |
|  SAFI                                 | evpn                                                 |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | false                                                |
|  GR Capability Advertised             | false                                                |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | false                                                |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_9                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| BGP BFD Configuration                 | Disabled                                             |
| EBGP Multi-Hop Operational            | Disabled                                             |
+---------------------------------------+------------------------------------------------------+
```

</details>

### G2: Task 3 — Enable multiprotocol BGP

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show bgp peers peer 172.16.0.2
```

Pass: Output contains `vpnv4` and `evpn` and `labeled-unicast`

<details><summary>Example output</summary>

```
+------------------------------------------ BGP PEER ------------------------------------------+
| Name                                  | Value                                                |
+---------------------------------------+------------------------------------------------------+
| Peer                                  | 172.16.0.2                                           |
| Remote AS                             | 65032                                                |
| Remote Router ID                      | 172.16.0.2                                           |
| Received Pkt Count                    | 5                                                    |
| Advertised Pkt Count                  | 5                                                    |
| Next Hop                              | 172.16.0.1                                           |
| Next Hop Global                       | fc00::1                                              |
| Next Hop Local                        | ::                                                   |
| Remote Port                           | 44183                                                |
| Remote Address                        | 172.16.0.2                                           |
| Local Port                            | 179                                                  |
| Connections Established               | 2                                                    |
| Connections Dropped                   | 1                                                    |
| Open Msg Received                     | 1                                                    |
| Open Msg Sent                         | 1                                                    |
| Update Msg Received                   | 4                                                    |
| Update Msg Sent                       | 4                                                    |
| Last Reset (hh:mm:ss)                 | 00:00:24                                             |
| Connection                            | non shared network                                   |
| Up Time (hh:mm:ss)                    | 00:00:24                                             |
| Read Time (hh:mm:ss)                  | 00:00:24                                             |
| Peer Type                             | internal                                             |
| Notifications Sent                    | 1                                                    |
| Notification Direction                | sent                                                 |
| Last Notification Error Message       | (Cease/Other Configuration Change.)                  |
| Configured Hold Time (s)              | 180                                                  |
| Configured Keepalive Interval (s)     | 60                                                   |
| Oper Hold Time (s)                    | 180                                                  |
| Oper Keepalive Interval (s)           | 60                                                   |
| Update Source                         | lb1                                                  |
| Minimum Advertisement Interval        | 0                                                    |
| IPv4 Unicast Support                  | advertised and received                              |
| IPv6 Unicast Support                  | -                                                    |
| VPNv4 Unicast Support                 | advertised and received                              |
| VPNv6 Unicast Support                 | -                                                    |
| L2VPN EVPN Unicast Support            | advertised and received                              |
| L2VPN VPLS Unicast Support            | -                                                    |
| RTFilter Unicast Support              | -                                                    |
| State                                 | Established                                          |
| Shutdown                              | False                                                |
| Peer Flap Counter                     | 1                                                    |
| Peer Restart Time (s)                 | 0                                                    |
| Peer Restarting                       | false                                                |
| Connect Retry Interval (s)            | 120                                                  |
| Last Reset Information                |                                                      |
| Last Update Read (s)                  | 14                                                   |
| Last Update Read Before Reset (s)     | 0                                                    |
| Last Write (s)                        | 14                                                   |
| Last Written (bytes)                  | 23                                                   |
| Second Last Write (s)                 | 14                                                   |
| Second Last Written (bytes)           | 56                                                   |
| Last Write Before Reset (s)           | 24                                                   |
| Second Last Write Before Reset (s)    | 35                                                   |
| Current Holdtimer Reset (s)           | 14                                                   |
| Last Holdtimer Reset (s)              | 0                                                    |
| Lockout                               | Disabled                                             |
| Local AS                              | -                                                    |
| Last MD5 Failure Reason               | -                                                    |
| Last MD5 Failure Time (hh:mm:ss)      | -                                                    |
| Address Family 1                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 1                                                    |
|  Sent Prefix Count                    | 1                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | True                                                 |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_3                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 2                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | labeled-unicast                                      |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_5                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 3                      |                                                      |
|  AFI                                  | vpnv4                                                |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_7                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 4                      |                                                      |
|  AFI                                  | l2vpn                                                |
|  SAFI                                 | evpn                                                 |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | false                                                |
|  GR Capability Advertised             | false                                                |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | false                                                |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_9                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| BGP BFD Configuration                 | Disabled                                             |
| EBGP Multi-Hop Operational            | Disabled                                             |
+---------------------------------------+------------------------------------------------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show bgp peers peer 172.16.0.1
```

Pass: Output contains `vpnv4` and `evpn` and `labeled-unicast`

<details><summary>Example output</summary>

```
+------------------------------------------ BGP PEER ------------------------------------------+
| Name                                  | Value                                                |
+---------------------------------------+------------------------------------------------------+
| Peer                                  | 172.16.0.1                                           |
| Remote AS                             | 65032                                                |
| Remote Router ID                      | 172.16.0.1                                           |
| Received Pkt Count                    | 6                                                    |
| Advertised Pkt Count                  | 6                                                    |
| Next Hop                              | 172.16.0.2                                           |
| Next Hop Global                       | fc00::2                                              |
| Next Hop Local                        | ::                                                   |
| Remote Port                           | 179                                                  |
| Remote Address                        | 172.16.0.1                                           |
| Local Port                            | 44183                                                |
| Connections Established               | 2                                                    |
| Connections Dropped                   | 1                                                    |
| Open Msg Received                     | 1                                                    |
| Open Msg Sent                         | 1                                                    |
| Update Msg Received                   | 4                                                    |
| Update Msg Sent                       | 4                                                    |
| Keepalives Received                   | 1                                                    |
| Keepalives Sent                       | 1                                                    |
| Last Reset (hh:mm:ss)                 | 00:00:30                                             |
| Connection                            | non shared network                                   |
| Up Time (hh:mm:ss)                    | 00:00:25                                             |
| Read Time (hh:mm:ss)                  | 00:00:25                                             |
| Peer Type                             | internal                                             |
| Notifications Received                | 1                                                    |
| Notification Direction                | received                                             |
| Last Notification Error Message       | (Cease/Other Configuration Change.)                  |
| Configured Hold Time (s)              | 180                                                  |
| Configured Keepalive Interval (s)     | 60                                                   |
| Oper Hold Time (s)                    | 180                                                  |
| Oper Keepalive Interval (s)           | 60                                                   |
| Update Source                         | lb1                                                  |
| Minimum Advertisement Interval        | 0                                                    |
| IPv4 Unicast Support                  | advertised and received                              |
| IPv6 Unicast Support                  | -                                                    |
| VPNv4 Unicast Support                 | advertised and received                              |
| VPNv6 Unicast Support                 | -                                                    |
| L2VPN EVPN Unicast Support            | advertised and received                              |
| L2VPN VPLS Unicast Support            | -                                                    |
| RTFilter Unicast Support              | -                                                    |
| State                                 | Established                                          |
| Shutdown                              | False                                                |
| Peer Flap Counter                     | 1                                                    |
| Peer Restart Time (s)                 | 0                                                    |
| Peer Restarting                       | false                                                |
| Connect Retry Interval (s)            | 120                                                  |
| Last Reset Information                |                                                      |
| Last Update Read (s)                  | 15                                                   |
| Last Update Read Before Reset (s)     | 30                                                   |
| Last Write (s)                        | 15                                                   |
| Last Written (bytes)                  | 23                                                   |
| Second Last Write (s)                 | 15                                                   |
| Second Last Written (bytes)           | 56                                                   |
| Last Write Before Reset (s)           | 37                                                   |
| Second Last Write Before Reset (s)    | 0                                                    |
| Current Holdtimer Reset (s)           | 15                                                   |
| Last Holdtimer Reset (s)              | 30                                                   |
| Lockout                               | Disabled                                             |
| Local AS                              | -                                                    |
| Last MD5 Failure Reason               | -                                                    |
| Last MD5 Failure Time (hh:mm:ss)      | -                                                    |
| Address Family 1                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 1                                                    |
|  Sent Prefix Count                    | 1                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | True                                                 |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_3                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 2                      |                                                      |
|  AFI                                  | ipv4                                                 |
|  SAFI                                 | labeled-unicast                                      |
|  Peer Table Version                   | 2                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 3                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_5                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 3                      |                                                      |
|  AFI                                  | vpnv4                                                |
|  SAFI                                 | unicast                                              |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | true                                                 |
|  GR Capability Advertised             | true                                                 |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | true                                                 |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_7                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Default Originate                    | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| Address Family 4                      |                                                      |
|  AFI                                  | l2vpn                                                |
|  SAFI                                 | evpn                                                 |
|  Peer Table Version                   | 1                                                    |
|  Ebgp Allow SR                        | disable                                              |
|  Community Count                      | 1                                                    |
|  BGP Table Version                    | 1                                                    |
|  Index                                | 1                                                    |
|  Offset                               | 0                                                    |
|  Received Prefix Count                | 0                                                    |
|  Sent Prefix Count                    | 0                                                    |
|  Packets in Queue                     | 0                                                    |
|  Graceful Restart Helper              | -                                                    |
|  Soft Reconfiguration Inbound         | False                                                |
|  Route Target Filter Sent             | 0                                                    |
|  Route Target Filter Received         | 0                                                    |
|  Route Reflection                     | Disabled                                             |
|  Refresh Capability                   | Route refresh: advertised and received (old and new) |
|  GR Capability Received               | false                                                |
|  GR Capability Advertised             | false                                                |
|  Forwarding State Preserved Received  | false                                                |
|  End Of RIB Marker Received           | false                                                |
|  Count Of Flushed Stalepath           | 0                                                    |
|  Reason Of Flushed Stalepath          | no-fault                                             |
|  Additional Capability Sent           | -                                                    |
|  Additional Capability Received       | -                                                    |
|  Update Group ID                      | __auto_ug_9                                          |
|  AIGP Enable                          | true                                                 |
|  Default Route Target Filter Sent     | false                                                |
|  Default Route Target Filter Received | false                                                |
|  Route Reflector Client Operational   | false                                                |
|  Next Hop Self Operational            | false                                                |
|  Additional Path Operational          | Enabled                                              |
|     select-all                        | False                                                |
|     Advertise Diverse Path            | False                                                |
| BGP BFD Configuration                 | Disabled                                             |
| EBGP Multi-Hop Operational            | Disabled                                             |
+---------------------------------------+------------------------------------------------------+
```

</details>

### G3: Task 4 — Redistribute a policy-controlled loopback

On **PE_1**, run:

```saos
show ip routes route 10.65.0.32/32
```

Pass: Output contains `10.65.0.32` and `lb10`

<details><summary>Example output</summary>

```
+---------------------------------------------------------------------------------------+
| Codes: K - kernel, C - connected, S - static, B - BGP, O - OSPF, IA - OSPF inter area |
|        E1 - OSPF external type 1, E2 - OSPF external type 2                           |
|        I - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area       |
|        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2                 |
|        M - MPLS                                                                       |
|        > - selected route, * - FIB route, ~ - Anycast Prefix                          |
|        S/T - Sub Type, RP/M - Route Preference/Metric                                 |
+---------------------------------------------------------------------------------------+
+------------------------------------------------------------------------------- RIB STATE: default -------------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
| *>    |  C   |  -  | -                | 10.65.0.32/32      | [0/0]     | -               | lb10                      | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

On **PE_2**, run:

```saos
show ip routes route 10.65.0.33/32
```

Pass: Output contains `10.65.0.33` and `lb10`

<details><summary>Example output</summary>

```
+---------------------------------------------------------------------------------------+
| Codes: K - kernel, C - connected, S - static, B - BGP, O - OSPF, IA - OSPF inter area |
|        E1 - OSPF external type 1, E2 - OSPF external type 2                           |
|        I - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area       |
|        N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2                 |
|        M - MPLS                                                                       |
|        > - selected route, * - FIB route, ~ - Anycast Prefix                          |
|        S/T - Sub Type, RP/M - Route Preference/Metric                                 |
+---------------------------------------------------------------------------------------+
+------------------------------------------------------------------------------- RIB STATE: default -------------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
| *>    |  C   |  -  | -                | 10.65.0.33/32      | [0/0]     | -               | lb10                      | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show bgp routes
```

Pass: Output contains `10.65.0.32` and `10.65.0.33`

<details><summary>Example output</summary>

```
+----------------------------------------------------------------------------------+
| Status codes: s suppressed, d damped, h history, a add-path,                     |
|               * valid, > best, i - internal, l - labeled, S Stale                |
|               m - multipath candidate, t - evpn route type 5, D add-path-diverse |
|               M - malformed                                                      |
| Origin codes: i - IGP, e - EGP, ? - incomplete                                   |
+----------------------------------------------------------------------------------+
+------------------------------------------------------- BGP IPV4 ROUTES -------------------------------------------------------+
|          | Table   |                    |                 |     |             |                  |        |         | AS Path |
| Flags    | Version | Network            | Next Hop        | MED | iBGP Metric | Local Preference | Weight | AS Path | Origin  |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
| *>       | 2       | 10.65.0.32/32      | 0.0.0.0         | 0   | 0           | 100              | 32768  | Local   | ?       |
| *>i      | 3       | 10.65.0.33/32      | 172.16.0.2      | 0   | 20          | 100              | 0      | Local   | ?       |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
```

</details>

<!-- retry: 90s -->
On **PE_1**, run:

```saos
show bgp routes ipv4 unicast community 65032:100
```

Pass: Output contains `10.65.0.32`

<details><summary>Example output</summary>

```
+----------------------------------------------------------------------------------+
| Status codes: s suppressed, d damped, h history, a add-path,                     |
|               * valid, > best, i - internal, l - labeled, S Stale                |
|               m - multipath candidate, t - evpn route type 5, D add-path-diverse |
|               M - malformed                                                      |
| Origin codes: i - IGP, e - EGP, ? - incomplete                                   |
+----------------------------------------------------------------------------------+
+------------------------------------------------------- BGP IPV4 ROUTES -------------------------------------------------------+
|          | Table   |                    |                 |     |             |                  |        |         | AS Path |
| Flags    | Version | Network            | Next Hop        | MED | iBGP Metric | Local Preference | Weight | AS Path | Origin  |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
| *>       | 2       | 10.65.0.32/32      | 0.0.0.0         | 0   | 0           | 100              | 32768  | Local   | ?       |
| *>i      | 3       | 10.65.0.33/32      | 172.16.0.2      | 0   | 20          | 100              | 0      | Local   | ?       |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
show bgp routes
```

Pass: Output contains `10.65.0.33` and `10.65.0.32`

<details><summary>Example output</summary>

```
+----------------------------------------------------------------------------------+
| Status codes: s suppressed, d damped, h history, a add-path,                     |
|               * valid, > best, i - internal, l - labeled, S Stale                |
|               m - multipath candidate, t - evpn route type 5, D add-path-diverse |
|               M - malformed                                                      |
| Origin codes: i - IGP, e - EGP, ? - incomplete                                   |
+----------------------------------------------------------------------------------+
+------------------------------------------------------- BGP IPV4 ROUTES -------------------------------------------------------+
|          | Table   |                    |                 |     |             |                  |        |         | AS Path |
| Flags    | Version | Network            | Next Hop        | MED | iBGP Metric | Local Preference | Weight | AS Path | Origin  |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
| *>i      | 3       | 10.65.0.32/32      | 172.16.0.1      | 0   | 20          | 100              | 0      | Local   | ?       |
| *>       | 2       | 10.65.0.33/32      | 0.0.0.0         | 0   | 0           | 100              | 32768  | Local   | ?       |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
show bgp routes ipv4 unicast community 65032:100
```

Pass: Output contains `10.65.0.33`

<details><summary>Example output</summary>

```
+----------------------------------------------------------------------------------+
| Status codes: s suppressed, d damped, h history, a add-path,                     |
|               * valid, > best, i - internal, l - labeled, S Stale                |
|               m - multipath candidate, t - evpn route type 5, D add-path-diverse |
|               M - malformed                                                      |
| Origin codes: i - IGP, e - EGP, ? - incomplete                                   |
+----------------------------------------------------------------------------------+
+------------------------------------------------------- BGP IPV4 ROUTES -------------------------------------------------------+
|          | Table   |                    |                 |     |             |                  |        |         | AS Path |
| Flags    | Version | Network            | Next Hop        | MED | iBGP Metric | Local Preference | Weight | AS Path | Origin  |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
| *>i      | 3       | 10.65.0.32/32      | 172.16.0.1      | 0   | 20          | 100              | 0      | Local   | ?       |
| *>       | 2       | 10.65.0.33/32      | 0.0.0.0         | 0   | 0           | 100              | 32768  | Local   | ?       |
+----------+---------+--------------------+-----------------+-----+-------------+------------------+--------+---------+---------+
```

</details>

## Solutions

Use the preloaded baseline for context, then apply the learner solution blocks in task order.

### Preloaded baseline

#### PE_1

```saos
# Preloaded start
system config hostname PE_1
fds fd PE_1-PE_2-FD mode vpls
oc-if:interfaces interface lb1 config name lb1 type loopback
oc-if:interfaces interface lb1 ipv4 addresses address 172.16.0.1 config ip 172.16.0.1 prefix-length 32
oc-if:interfaces interface lb1 ipv6 addresses address FC00::1 config ip FC00::1 prefix-length 128
oc-if:interfaces interface PE_1-PE_2-if config mtu 1500 name PE_1-PE_2-if type ip
oc-if:interfaces interface PE_1-PE_2-if config underlay-binding config fd PE_1-PE_2-FD
oc-if:interfaces interface PE_1-PE_2-if ipv4 addresses address 172.16.1.1 config ip 172.16.1.1 prefix-length 30
oc-if:interfaces interface PE_1-PE_2-if ipv6 addresses address FC00::600 config ip FC00::600 prefix-length 127
classifiers classifier CLASSIFIER-UNTAGGED filter-entry vtag-stack untagged-exclude-priority-tagged false
fps fp PE_1-PE_2-FP classifier-list-precedence 7 fd-name PE_1-PE_2-FD logical-port 1 mtu-size 2000 stats-collection on classifier-list CLASSIFIER-UNTAGGED
isis instance Bootcamp level-type level-1 net 49.0001.0172.0016.0001.00
isis instance Bootcamp interfaces interface lb1 interface-type point-to-point
isis instance Bootcamp interfaces interface lb1 address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if interface-type point-to-point level-type level-1
isis instance Bootcamp interfaces interface PE_1-PE_2-if address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if level-1 password ciena123
mpls interfaces interface PE_1-PE_2-if label-switching true
mpls interfaces interface lb1 label-switching true
segment-routing connected-prefix-sid-map 172.16.0.1/32 interface lb1 start-sid 1 value-type index
isis instance Bootcamp cspf-flag true
isis instance Bootcamp mpls-te level-type level-1 router-id 172.16.0.1
isis instance Bootcamp segment-routing enabled true srgb 16000 23999
isis instance Bootcamp segment-routing bindings advertise true receive true
# Preloaded end
```

#### PE_2

```saos
# Preloaded start
system config hostname PE_2
fds fd PE_1-PE_2-FD mode vpls
oc-if:interfaces interface lb1 config name lb1 type loopback
oc-if:interfaces interface lb1 ipv4 addresses address 172.16.0.2 config ip 172.16.0.2 prefix-length 32
oc-if:interfaces interface lb1 ipv6 addresses address FC00::2 config ip FC00::2 prefix-length 128
oc-if:interfaces interface PE_1-PE_2-if config mtu 1500 name PE_1-PE_2-if type ip
oc-if:interfaces interface PE_1-PE_2-if config underlay-binding config fd PE_1-PE_2-FD
oc-if:interfaces interface PE_1-PE_2-if ipv4 addresses address 172.16.1.2 config ip 172.16.1.2 prefix-length 30
oc-if:interfaces interface PE_1-PE_2-if ipv6 addresses address FC00::601 config ip FC00::601 prefix-length 127
classifiers classifier CLASSIFIER-UNTAGGED filter-entry vtag-stack untagged-exclude-priority-tagged false
fps fp PE_1-PE_2-FP classifier-list-precedence 7 fd-name PE_1-PE_2-FD logical-port 1 mtu-size 2000 stats-collection on classifier-list CLASSIFIER-UNTAGGED
isis instance Bootcamp level-type level-1 net 49.0001.0172.0016.0002.00
isis instance Bootcamp interfaces interface lb1 interface-type point-to-point
isis instance Bootcamp interfaces interface lb1 address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if interface-type point-to-point level-type level-1
isis instance Bootcamp interfaces interface PE_1-PE_2-if address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if level-1 password ciena123
mpls interfaces interface PE_1-PE_2-if label-switching true
mpls interfaces interface lb1 label-switching true
segment-routing connected-prefix-sid-map 172.16.0.2/32 interface lb1 start-sid 2 value-type index
isis instance Bootcamp cspf-flag true
isis instance Bootcamp mpls-te level-type level-1 router-id 172.16.0.2
isis instance Bootcamp segment-routing enabled true srgb 16000 23999
isis instance Bootcamp segment-routing bindings advertise true receive true
# Preloaded end
```

#### PE_3

```saos
# Preloaded start
system config hostname PE_3
# Preloaded end
```

#### CE1

```saos
# Preloaded start
system config hostname CE1
# Preloaded end
```

#### CE2

```saos
# Preloaded start
system config hostname CE2
# Preloaded end
```

### Solution for Task 1

#### PE_1

```saos
# Task 1 start
bgp instance 65032 router-id 172.16.0.1
# Task 1 end
```

#### PE_2

```saos
# Task 1 start
bgp instance 65032 router-id 172.16.0.2
# Task 1 end
```

### Solution for Task 2

#### PE_1

```saos
# Task 2 start
bgp instance 65032 address-family ipv4 unicast
    exit
  exit
exit
bgp instance 65032 peer 172.16.0.2 remote-as 65032
bgp instance 65032 peer 172.16.0.2 address-family ipv4 unicast activate true soft-reconfiguration-inbound true
bgp instance 65032 peer 172.16.0.2 update-source-interface lb1
bgp instance 65032 peer 172.16.0.2 password ciena123
# Task 2 end
```

#### PE_2

```saos
# Task 2 start
bgp instance 65032 address-family ipv4 unicast
    exit
  exit
exit
bgp instance 65032 peer 172.16.0.1 remote-as 65032
bgp instance 65032 peer 172.16.0.1 address-family ipv4 unicast activate true soft-reconfiguration-inbound true
bgp instance 65032 peer 172.16.0.1 update-source-interface lb1
bgp instance 65032 peer 172.16.0.1 password ciena123
# Task 2 end
```

### Solution for Task 3

#### PE_1

```saos
# Task 3 start
bgp instance 65032 address-family vpnv4 unicast
    exit
  exit
exit
bgp instance 65032 address-family l2vpn evpn
    exit
  exit
exit
bgp instance 65032 address-family ipv4 labeled-unicast
    exit
  exit
exit
bgp instance 65032 peer 172.16.0.2 address-family vpnv4 unicast activate true
bgp instance 65032 peer 172.16.0.2 address-family l2vpn evpn activate true
bgp instance 65032 peer 172.16.0.2 address-family ipv4 labeled-unicast activate true
# Task 3 end
```

#### PE_2

```saos
# Task 3 start
bgp instance 65032 address-family vpnv4 unicast
    exit
  exit
exit
bgp instance 65032 address-family l2vpn evpn
    exit
  exit
exit
bgp instance 65032 address-family ipv4 labeled-unicast
    exit
  exit
exit
bgp instance 65032 peer 172.16.0.1 address-family vpnv4 unicast activate true
bgp instance 65032 peer 172.16.0.1 address-family l2vpn evpn activate true
bgp instance 65032 peer 172.16.0.1 address-family ipv4 labeled-unicast activate true
# Task 3 end
```

### Solution for Task 4

#### PE_1

```saos
# Task 4 start
oc-if:interfaces interface lb10 config name lb10 type loopback
oc-if:interfaces interface lb10 ipv4 addresses address 10.65.0.32 config ip 10.65.0.32 prefix-length 32
routing-policy prefix-lists prefix-list lb10 mode ipv4 sequence 1 action permit ip-prefix 10.65.0.32/32
routing-policy policies policy lb10 statement 1 action permit
routing-policy policies policy lb10 statement 1 match route-entry lb10
routing-policy policies policy lb10 statement 1 set community append standard 65032:100
routing-policy policies policy lb10 statement 2 action deny
bgp instance 65032 address-family ipv4 unicast redistribute connected policy lb10
# Task 4 end
```

#### PE_2

```saos
# Task 4 start
oc-if:interfaces interface lb10 config name lb10 type loopback
oc-if:interfaces interface lb10 ipv4 addresses address 10.65.0.33 config ip 10.65.0.33 prefix-length 32
routing-policy prefix-lists prefix-list lb10 mode ipv4 sequence 1 action permit ip-prefix 10.65.0.33/32
routing-policy policies policy lb10 statement 1 action permit
routing-policy policies policy lb10 statement 1 match route-entry lb10
routing-policy policies policy lb10 statement 1 set community append standard 65032:100
routing-policy policies policy lb10 statement 2 action deny
bgp instance 65032 address-family ipv4 unicast redistribute connected policy lb10
# Task 4 end
```

### Solution for Task 5

No configuration commands; this is a verification-only task.
