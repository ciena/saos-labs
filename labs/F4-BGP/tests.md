Deploy `F4-BGP`, then run the following validation checks.

## G1: Task 2 — Establish authenticated iBGP

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

## G2: Task 3 — Enable multiprotocol BGP

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

## G3: Task 4 — Redistribute a policy-controlled loopback

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
