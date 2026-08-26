Deploy `S1-L3VPN`, then run the following validation checks.

## G1: Task 1 — Verify the deployed topology

On **CE_1**, run:

```saos
show forwarding-domains
```

Pass: Output contains `CE_1-PE_1-FD` and `vpls`

<details><summary>Example output</summary>

```
+ FORWARDING DOMAIN -+
| Name        | Mode |
+-------------+------+
| CE_1-PE_1-FD | vpls |
| remote-fd   | vpls |
+-------------+------+
```

</details>

On **CE_2**, run:

```saos
show forwarding-domains
```

Pass: Output contains `CE_2-PE_2-FD` and `vpls`

<details><summary>Example output</summary>

```
+ FORWARDING DOMAIN -+
| Name        | Mode |
+-------------+------+
| CE_2-PE_2-FD | vpls |
| remote-fd   | vpls |
+-------------+------+
```

</details>

On **CE_1**, run:

```saos
show ip interfaces
```

Pass: Output contains `CE_1-PE_1-if` and `172.16.103.2` and `30`

<details><summary>Example output</summary>

```
+-------------------------------------------------- IP INTERFACES STATE ---------------------------------------------------+
| Name                                       | Value                                                                       |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | mgmtbr0                                                                     |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | system                                                                      |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| DHCP IPv4 Client                           | True                                                                        |
| DHCP IPv4 Address                          | 10.0.0.15                                                                   |
| DHCP IPv4 Prefix                           | 24                                                                          |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::200:8bff:fea9:5b00                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 20                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:8b:a9:5b:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 24510                                                                       |
|   Input Packets                            | 376                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 85744                                                                       |
|   Output Packets                           | 409                                                                         |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | remote                                                                      |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:8bff:fea9:5af6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:8b:a9:5a:f6                                                           |
| Last Changed                               | Aug 06 2026 20:50:02 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Enabled                                                                     |
| Unsolicited Neighbor Advertisement         | Enabled                                                                     |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | remote-fd                                                                   |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | remote-fp1, remote-fp2, remote-fp3, remote-fp4, remote-fp5, remote-fp6      |
| Logical Port(s)                            | 1, 2, 3, 4, 5, 6                                                            |
| Classifier(s)                              | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127                                            |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb1                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:8bff:fea9:5af5                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735925                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 10.1.1.1                                                                    |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | CE_1-PE_1-if                                                                 |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:8bff:fea9:5af5                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:8b:a9:5a:f5                                                           |
| Last Changed                               | Aug 06 2026 20:55:22 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | CE_1-PE_1-FD                                                                 |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 1712                                                                        |
|   Input Packets                            | 20                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 23                                                                          |
|   Output Octets                            | 9271                                                                        |
|   Output Packets                           | 66                                                                          |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 2                                                                           |
|   Input Router Solicitation Octets         | 32                                                                          |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.103.2                                                                |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | CE_1-PE_1-FP                                                                 |
| Logical Port(s)                            | 1                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
```

</details>

On **CE_2**, run:

```saos
show ip interfaces
```

Pass: Output contains `CE_2-PE_2-if` and `172.16.103.34` and `30`

<details><summary>Example output</summary>

```
+-------------------------------------------------- IP INTERFACES STATE ---------------------------------------------------+
| Name                                       | Value                                                                       |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | mgmtbr0                                                                     |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | system                                                                      |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| DHCP IPv4 Client                           | True                                                                        |
| DHCP IPv4 Address                          | 10.0.0.15                                                                   |
| DHCP IPv4 Prefix                           | 24                                                                          |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::200:80ff:fea2:a00                                                     |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 20                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:80:a2:0a:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 24926                                                                       |
|   Input Packets                            | 373                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 85939                                                                       |
|   Output Packets                           | 403                                                                         |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | remote                                                                      |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:80ff:fea2:9f6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:80:a2:09:f6                                                           |
| Last Changed                               | Aug 06 2026 20:50:15 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Enabled                                                                     |
| Unsolicited Neighbor Advertisement         | Enabled                                                                     |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | remote-fd                                                                   |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | remote-fp1, remote-fp2, remote-fp3, remote-fp4, remote-fp5, remote-fp6      |
| Logical Port(s)                            | 1, 2, 3, 4, 5, 6                                                            |
| Classifier(s)                              | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127                                            |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb1                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:80ff:fea2:9f5                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735925                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 10.2.2.2                                                                    |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | CE_2-PE_2-if                                                                 |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:80ff:fea2:9f5                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:80:a2:09:f5                                                           |
| Last Changed                               | Aug 06 2026 20:55:35 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | CE_2-PE_2-FD                                                                 |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 1976                                                                        |
|   Input Packets                            | 22                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 19                                                                          |
|   Output Octets                            | 8182                                                                        |
|   Output Packets                           | 56                                                                          |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 1                                                                           |
|   Input Router Solicitation Octets         | 16                                                                          |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.103.34                                                               |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | CE_2-PE_2-FP                                                                 |
| Logical Port(s)                            | 1                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
```

</details>

On **CE_1**, run:

```saos
show classifiers
```

Pass: Output contains `CLASSIFIER-UNTAGGED`

<details><summary>Example output</summary>

```
+---------------------- CLASSIFIER ---------------------+
| Name                | Filter Parameter                |
+---------------------+---------------------------------+
| CLASSIFIER-UNTAGGED | ciena-mef-classifier:vtag-stack |
| default-vid-127     | Classifier:single-tagged        |
+---------------------+---------------------------------+
```

</details>

On **CE_2**, run:

```saos
show classifiers
```

Pass: Output contains `CLASSIFIER-UNTAGGED`

<details><summary>Example output</summary>

```
+---------------------- CLASSIFIER ---------------------+
| Name                | Filter Parameter                |
+---------------------+---------------------------------+
| CLASSIFIER-UNTAGGED | ciena-mef-classifier:vtag-stack |
| default-vid-127     | Classifier:single-tagged        |
+---------------------+---------------------------------+
```

</details>

On **CE_1**, run:

```saos
show flow-points
```

Pass: Output contains `CE_1-PE_1-FP`

<details><summary>Example output</summary>

```
+--------------------------------------- FLOW POINT --------------------------------------+
| Name        | Forwarding Domain Name | Logical Port | Admin State | Classifier List     |
+-------------+------------------------+--------------+-------------+---------------------+
| CE_1-PE_1-FP | CE_1-PE_1-FD            | 1            | enabled     | CLASSIFIER-UNTAGGED |
| remote-fp1  | remote-fd              | 1            | enabled     | default-vid-127     |
| remote-fp2  | remote-fd              | 2            | enabled     | default-vid-127     |
| remote-fp3  | remote-fd              | 3            | enabled     | default-vid-127     |
| remote-fp4  | remote-fd              | 4            | enabled     | default-vid-127     |
| remote-fp5  | remote-fd              | 5            | enabled     | default-vid-127     |
| remote-fp6  | remote-fd              | 6            | enabled     | default-vid-127     |
+-------------+------------------------+--------------+-------------+---------------------+
+------------------------------------ FLOW POINT STATISTICS ------------------------------------+
| Name        | Rx Accepted Frames | Tx Forwarded Frames | Rx Yellow Frames | Rx Dropped Frames |
+-------------+--------------------+---------------------+------------------+-------------------+
| CE_1-PE_1-FP | 63                 | 67                  | 0                | 0                 |
| remote-fp1  | -                  | -                   | -                | -                 |
| remote-fp2  | -                  | -                   | -                | -                 |
| remote-fp3  | -                  | -                   | -                | -                 |
| remote-fp4  | -                  | -                   | -                | -                 |
| remote-fp5  | -                  | -                   | -                | -                 |
| remote-fp6  | -                  | -                   | -                | -                 |
+-------------+--------------------+---------------------+------------------+-------------------+
+------------------------------------------------- FLOW POINT STATE -------------------------------------------------+
| Name        | PFG Operational State | EVPN FXC Locally Switched | Oper State | Oper Up Time     | Forwarding State |
+-------------+-----------------------+---------------------------+------------+------------------+------------------+
| CE_1-PE_1-FP | -                     | -                         | up         | 0 days,0h:4m:14s | -                |
| remote-fp1  | leaf                  | -                         | up         | 0 days,0h:9m:34s | -                |
| remote-fp2  | leaf                  | -                         | up         | 0 days,0h:9m:34s | -                |
| remote-fp3  | leaf                  | -                         | up         | 0 days,0h:9m:34s | -                |
| remote-fp4  | leaf                  | -                         | up         | 0 days,0h:9m:34s | -                |
| remote-fp5  | leaf                  | -                         | up         | 0 days,0h:9m:33s | -                |
| remote-fp6  | leaf                  | -                         | up         | 0 days,0h:9m:33s | -                |
+-------------+-----------------------+---------------------------+------------+------------------+------------------+
```

</details>

On **CE_2**, run:

```saos
show flow-points
```

Pass: Output contains `CE_2-PE_2-FP`

<details><summary>Example output</summary>

```
+--------------------------------------- FLOW POINT --------------------------------------+
| Name        | Forwarding Domain Name | Logical Port | Admin State | Classifier List     |
+-------------+------------------------+--------------+-------------+---------------------+
| CE_2-PE_2-FP | CE_2-PE_2-FD            | 1            | enabled     | CLASSIFIER-UNTAGGED |
| remote-fp1  | remote-fd              | 1            | enabled     | default-vid-127     |
| remote-fp2  | remote-fd              | 2            | enabled     | default-vid-127     |
| remote-fp3  | remote-fd              | 3            | enabled     | default-vid-127     |
| remote-fp4  | remote-fd              | 4            | enabled     | default-vid-127     |
| remote-fp5  | remote-fd              | 5            | enabled     | default-vid-127     |
| remote-fp6  | remote-fd              | 6            | enabled     | default-vid-127     |
+-------------+------------------------+--------------+-------------+---------------------+
+------------------------------------ FLOW POINT STATISTICS ------------------------------------+
| Name        | Rx Accepted Frames | Tx Forwarded Frames | Rx Yellow Frames | Rx Dropped Frames |
+-------------+--------------------+---------------------+------------------+-------------------+
| CE_2-PE_2-FP | 59                 | 56                  | 0                | 0                 |
| remote-fp1  | -                  | -                   | -                | -                 |
| remote-fp2  | -                  | -                   | -                | -                 |
| remote-fp3  | -                  | -                   | -                | -                 |
| remote-fp4  | -                  | -                   | -                | -                 |
| remote-fp5  | -                  | -                   | -                | -                 |
| remote-fp6  | -                  | -                   | -                | -                 |
+-------------+--------------------+---------------------+------------------+-------------------+
+------------------------------------------------- FLOW POINT STATE -------------------------------------------------+
| Name        | PFG Operational State | EVPN FXC Locally Switched | Oper State | Oper Up Time     | Forwarding State |
+-------------+-----------------------+---------------------------+------------+------------------+------------------+
| CE_2-PE_2-FP | -                     | -                         | up         | 0 days,0h:4m:1s  | -                |
| remote-fp1  | leaf                  | -                         | up         | 0 days,0h:9m:21s | -                |
| remote-fp2  | leaf                  | -                         | up         | 0 days,0h:9m:20s | -                |
| remote-fp3  | leaf                  | -                         | up         | 0 days,0h:9m:20s | -                |
| remote-fp4  | leaf                  | -                         | up         | 0 days,0h:9m:20s | -                |
| remote-fp5  | leaf                  | -                         | up         | 0 days,0h:9m:20s | -                |
| remote-fp6  | leaf                  | -                         | up         | 0 days,0h:9m:19s | -                |
+-------------+-----------------------+---------------------------+------------+------------------+------------------+
```

</details>

## G2: Task 2 — Create the L3VPN_2-vrf VRF and its in-VRF loopback on PE_1 and PE_2

<!-- retry: 90s -->
On **PE_1**, run:

```saos
show ip routes vrf L3VPN_1-vrf
```

Pass: Output contains `L3VPN_1-vrf` and `CE_1-PE_1-if`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_1-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
| *>    |  C   |  -  | -                | 172.16.103.0/30    | [0/0]     | -               | CE_1-PE_1-if               | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.103.32/30   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:31    |
|  >    |  B   |  M  | -                | 172.16.104.33/32   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:18    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
show ip routes vrf L3VPN_1-vrf
```

Pass: Output contains `L3VPN_1-vrf` and `CE_2-PE_2-if`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_1-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.0/30    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:32    |
| *>    |  C   |  -  | -                | 172.16.103.32/30   | [0/0]     | -               | CE_2-PE_2-if               | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.104.1/32    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:19    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

On **PE_1**, run:

```saos
show forwarding-domains
```

Pass: Output contains `CE_1-PE_1-FD` and `vpls`

<details><summary>Example output</summary>

```
+- FORWARDING DOMAIN -+
| Name         | Mode |
+--------------+------+
| CE_1-PE_1-FD  | vpls |
| PE_1-PE_2-FD | vpls |
| remote-fd    | vpls |
+--------------+------+
```

</details>

On **PE_2**, run:

```saos
show forwarding-domains
```

Pass: Output contains `CE_2-PE_2-FD` and `vpls`

<details><summary>Example output</summary>

```
+- FORWARDING DOMAIN -+
| Name         | Mode |
+--------------+------+
| CE_2-PE_2-FD  | vpls |
| PE_1-PE_2-FD | vpls |
| remote-fd    | vpls |
+--------------+------+
```

</details>

On **PE_1**, run:

```saos
show ip interfaces
```

Pass: Output contains `CE_1-PE_1-if` and `172.16.103.1` and `30`

<details><summary>Example output</summary>

```
+-------------------------------------------------- IP INTERFACES STATE ---------------------------------------------------+
| Name                                       | Value                                                                       |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | mgmtbr0                                                                     |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | system                                                                      |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| DHCP IPv4 Client                           | True                                                                        |
| DHCP IPv4 Address                          | 10.0.0.15                                                                   |
| DHCP IPv4 Prefix                           | 24                                                                          |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::200:e6ff:fe1e:5400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:e6:1e:54:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 78410                                                                       |
|   Input Packets                            | 1500                                                                        |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 288728                                                                      |
|   Output Packets                           | 1535                                                                        |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | remote                                                                      |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:e6:1e:53:f7                                                           |
| Last Changed                               | Aug 06 2026 20:52:04 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Enabled                                                                     |
| Unsolicited Neighbor Advertisement         | Enabled                                                                     |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | remote-fd                                                                   |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | remote-fp1, remote-fp2, remote-fp3, remote-fp4, remote-fp5, remote-fp6,     |
|                                            | remote-fp7, remote-fp8, remote-fp9, remote-fp10, remote-fp11, remote-fp12,  |
|                                            | remote-fp13, remote-fp14, remote-fp15, remote-fp16, remote-fp17,            |
|                                            | remote-fp18, remote-fp19, remote-fp20, remote-fp21, remote-fp22,            |
|                                            | remote-fp23, remote-fp24, remote-fp25, remote-fp26, remote-fp27,            |
|                                            | remote-fp28, remote-fp29, remote-fp30, remote-fp31, remote-fp32,            |
|                                            | remote-fp33, remote-fp34, remote-fp35, remote-fp36, remote-fp37,            |
|                                            | remote-fp38, remote-fp39, remote-fp40, remote-fp41, remote-fp42             |
| Logical Port(s)                            | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,  |
|                                            | 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, |
|                                            |  41, 42                                                                     |
| Classifier(s)                              | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127                                            |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb1                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735925                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.0.1                                                                  |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| IPv6 Addresses                             |                                                                             |
|   IP                                       | fc00:0000:0000:0000:0000:0000:0000:0001                                     |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | STATIC                                                                      |
|   Address Status                           | preferred                                                                   |
|   Secondary IP                             |                                                                             |
|       Preferred                            | -                                                                           |
|       Duplicate                            | -                                                                           |
|       Tentative                            | -                                                                           |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | PE_1-PE_2-if                                                                |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:e6:1e:53:f6                                                           |
| Last Changed                               | Aug 06 2026 20:57:39 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | PE_1-PE_2-FD                                                                |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 32281                                                                       |
|   Input Packets                            | 177                                                                         |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 9                                                                           |
|   Output Octets                            | 37632                                                                       |
|   Output Packets                           | 194                                                                         |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.1.1                                                                  |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| IPv6 Addresses                             |                                                                             |
|   IP                                       | fc00:0000:0000:0000:0000:0000:0000:0600                                     |
|   Prefix Length                            | 127                                                                         |
|   Origin                                   | STATIC                                                                      |
|   Address Status                           | preferred                                                                   |
|   Secondary IP                             |                                                                             |
|       Preferred                            | -                                                                           |
|       Duplicate                            | -                                                                           |
|       Tentative                            | -                                                                           |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | PE_1-PE_2-FP                                                                |
| Logical Port(s)                            | 1                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb10                                                                        |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735926                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 10.65.0.32                                                                  |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb2                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | L3VPN_2-vrf                                                                 |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735927                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Last Changed                               | Aug 06 2026 20:58:57 Local                                                  |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.104.1                                                                |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | CE_1-PE_1-if                                                                 |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | L3VPN_1-vrf                                                                 |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731827                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:e6:1e:53:f6                                                           |
| Last Changed                               | Aug 06 2026 20:58:59 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | CE_1-PE_1-FD                                                                 |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 888                                                                         |
|   Input Packets                            | 12                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 5                                                                           |
|   Output Octets                            | 2698                                                                        |
|   Output Packets                           | 24                                                                          |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.103.1                                                                |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | CE_1-PE_1-FP                                                                 |
| Logical Port(s)                            | 2                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
```

</details>

On **PE_2**, run:

```saos
show ip interfaces
```

Pass: Output contains `CE_2-PE_2-if` and `172.16.103.33` and `30`

<details><summary>Example output</summary>

```
+-------------------------------------------------- IP INTERFACES STATE ---------------------------------------------------+
| Name                                       | Value                                                                       |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | mgmtbr0                                                                     |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | system                                                                      |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| DHCP IPv4 Client                           | True                                                                        |
| DHCP IPv4 Address                          | 10.0.0.15                                                                   |
| DHCP IPv4 Prefix                           | 24                                                                          |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::200:7ff:fef3:2f00                                                     |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:07:f3:2f:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 76002                                                                       |
|   Input Packets                            | 1435                                                                        |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 281293                                                                      |
|   Output Packets                           | 1457                                                                        |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | remote                                                                      |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef7                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:07:f3:2e:f7                                                           |
| Last Changed                               | Aug 06 2026 20:52:17 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Enabled                                                                     |
| Unsolicited Neighbor Advertisement         | Enabled                                                                     |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | remote-fd                                                                   |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | remote-fp1, remote-fp2, remote-fp3, remote-fp4, remote-fp5, remote-fp6,     |
|                                            | remote-fp7, remote-fp8, remote-fp9, remote-fp10, remote-fp11, remote-fp12,  |
|                                            | remote-fp13, remote-fp14, remote-fp15, remote-fp16, remote-fp17,            |
|                                            | remote-fp18, remote-fp19, remote-fp20, remote-fp21, remote-fp22,            |
|                                            | remote-fp23, remote-fp24, remote-fp25, remote-fp26, remote-fp27,            |
|                                            | remote-fp28, remote-fp29, remote-fp30, remote-fp31, remote-fp32,            |
|                                            | remote-fp33, remote-fp34, remote-fp35, remote-fp36, remote-fp37,            |
|                                            | remote-fp38, remote-fp39, remote-fp40, remote-fp41, remote-fp42             |
| Logical Port(s)                            | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,  |
|                                            | 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, |
|                                            |  41, 42                                                                     |
| Classifier(s)                              | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127                                            |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb1                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735925                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.0.2                                                                  |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| IPv6 Addresses                             |                                                                             |
|   IP                                       | fc00:0000:0000:0000:0000:0000:0000:0002                                     |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | STATIC                                                                      |
|   Address Status                           | preferred                                                                   |
|   Secondary IP                             |                                                                             |
|       Preferred                            | -                                                                           |
|       Duplicate                            | -                                                                           |
|       Tentative                            | -                                                                           |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | PE_1-PE_2-if                                                                |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:07:f3:2e:f6                                                           |
| Last Changed                               | Aug 06 2026 20:57:49 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | PE_1-PE_2-FD                                                                |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 31931                                                                       |
|   Input Packets                            | 172                                                                         |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 8                                                                           |
|   Output Octets                            | 36815                                                                       |
|   Output Packets                           | 189                                                                         |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.1.2                                                                  |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| IPv6 Addresses                             |                                                                             |
|   IP                                       | fc00:0000:0000:0000:0000:0000:0000:0601                                     |
|   Prefix Length                            | 127                                                                         |
|   Origin                                   | STATIC                                                                      |
|   Address Status                           | preferred                                                                   |
|   Secondary IP                             |                                                                             |
|       Preferred                            | -                                                                           |
|       Duplicate                            | -                                                                           |
|       Tentative                            | -                                                                           |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | PE_1-PE_2-FP                                                                |
| Logical Port(s)                            | 1                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb10                                                                        |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735926                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 10.65.0.33                                                                  |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb2                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | L3VPN_2-vrf                                                                 |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735927                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Last Changed                               | Aug 06 2026 20:59:01 Local                                                  |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.104.33                                                               |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | CE_2-PE_2-if                                                                 |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | L3VPN_1-vrf                                                                 |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731827                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:07:f3:2e:f6                                                           |
| Last Changed                               | Aug 06 2026 20:59:02 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | CE_2-PE_2-FD                                                                 |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 888                                                                         |
|   Input Packets                            | 12                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 1                                                                           |
|   Output Octets                            | 2787                                                                        |
|   Output Packets                           | 25                                                                          |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.103.33                                                               |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | CE_2-PE_2-FP                                                                 |
| Logical Port(s)                            | 2                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
```

</details>

<!-- retry: 90s -->
On **PE_1**, run:

```saos
show ip routes vrf L3VPN_2-vrf
```

Pass: Output contains `L3VPN_2-vrf` and `lb2`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_2-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.32/30   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:20    |
| *>    |  C   |  -  | -                | 172.16.104.1/32    | [0/0]     | -               | lb2                       | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.104.33/32   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:32    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
show ip routes vrf L3VPN_2-vrf
```

Pass: Output contains `L3VPN_2-vrf` and `lb2`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_2-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.0/30    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:21    |
|  >    |  B   |  M  | -                | 172.16.104.1/32    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:33    |
| *>    |  C   |  -  | -                | 172.16.104.33/32   | [0/0]     | -               | lb2                       | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

On **PE_1**, run:

```saos
show ip interfaces
```

Pass: Output contains `lb2` and `172.16.104.1` and `32`

<details><summary>Example output</summary>

```
+-------------------------------------------------- IP INTERFACES STATE ---------------------------------------------------+
| Name                                       | Value                                                                       |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | mgmtbr0                                                                     |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | system                                                                      |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| DHCP IPv4 Client                           | True                                                                        |
| DHCP IPv4 Address                          | 10.0.0.15                                                                   |
| DHCP IPv4 Prefix                           | 24                                                                          |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::200:e6ff:fe1e:5400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:e6:1e:54:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 83826                                                                       |
|   Input Packets                            | 1631                                                                        |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 355060                                                                      |
|   Output Packets                           | 1665                                                                        |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | remote                                                                      |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:e6:1e:53:f7                                                           |
| Last Changed                               | Aug 06 2026 20:52:04 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Enabled                                                                     |
| Unsolicited Neighbor Advertisement         | Enabled                                                                     |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | remote-fd                                                                   |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | remote-fp1, remote-fp2, remote-fp3, remote-fp4, remote-fp5, remote-fp6,     |
|                                            | remote-fp7, remote-fp8, remote-fp9, remote-fp10, remote-fp11, remote-fp12,  |
|                                            | remote-fp13, remote-fp14, remote-fp15, remote-fp16, remote-fp17,            |
|                                            | remote-fp18, remote-fp19, remote-fp20, remote-fp21, remote-fp22,            |
|                                            | remote-fp23, remote-fp24, remote-fp25, remote-fp26, remote-fp27,            |
|                                            | remote-fp28, remote-fp29, remote-fp30, remote-fp31, remote-fp32,            |
|                                            | remote-fp33, remote-fp34, remote-fp35, remote-fp36, remote-fp37,            |
|                                            | remote-fp38, remote-fp39, remote-fp40, remote-fp41, remote-fp42             |
| Logical Port(s)                            | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,  |
|                                            | 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, |
|                                            |  41, 42                                                                     |
| Classifier(s)                              | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127                                            |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb1                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735925                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.0.1                                                                  |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| IPv6 Addresses                             |                                                                             |
|   IP                                       | fc00:0000:0000:0000:0000:0000:0000:0001                                     |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | STATIC                                                                      |
|   Address Status                           | preferred                                                                   |
|   Secondary IP                             |                                                                             |
|       Preferred                            | -                                                                           |
|       Duplicate                            | -                                                                           |
|       Tentative                            | -                                                                           |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | PE_1-PE_2-if                                                                |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:e6:1e:53:f6                                                           |
| Last Changed                               | Aug 06 2026 20:57:39 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | PE_1-PE_2-FD                                                                |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 32281                                                                       |
|   Input Packets                            | 177                                                                         |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 9                                                                           |
|   Output Octets                            | 37632                                                                       |
|   Output Packets                           | 194                                                                         |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.1.1                                                                  |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| IPv6 Addresses                             |                                                                             |
|   IP                                       | fc00:0000:0000:0000:0000:0000:0000:0600                                     |
|   Prefix Length                            | 127                                                                         |
|   Origin                                   | STATIC                                                                      |
|   Address Status                           | preferred                                                                   |
|   Secondary IP                             |                                                                             |
|       Preferred                            | -                                                                           |
|       Duplicate                            | -                                                                           |
|       Tentative                            | -                                                                           |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | PE_1-PE_2-FP                                                                |
| Logical Port(s)                            | 1                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb10                                                                        |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735926                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 10.65.0.32                                                                  |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb2                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | L3VPN_2-vrf                                                                 |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735927                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Last Changed                               | Aug 06 2026 20:58:57 Local                                                  |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.104.1                                                                |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | CE_1-PE_1-if                                                                 |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | L3VPN_1-vrf                                                                 |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:e6ff:fe1e:53f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731827                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:e6:1e:53:f6                                                           |
| Last Changed                               | Aug 06 2026 20:58:59 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | CE_1-PE_1-FD                                                                 |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 888                                                                         |
|   Input Packets                            | 12                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 5                                                                           |
|   Output Octets                            | 2698                                                                        |
|   Output Packets                           | 24                                                                          |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.103.1                                                                |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | CE_1-PE_1-FP                                                                 |
| Logical Port(s)                            | 2                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
```

</details>

On **PE_2**, run:

```saos
show ip interfaces
```

Pass: Output contains `lb2` and `172.16.104.33` and `32`

<details><summary>Example output</summary>

```
+-------------------------------------------------- IP INTERFACES STATE ---------------------------------------------------+
| Name                                       | Value                                                                       |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | mgmtbr0                                                                     |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | system                                                                      |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| DHCP IPv4 Client                           | True                                                                        |
| DHCP IPv4 Address                          | 10.0.0.15                                                                   |
| DHCP IPv4 Prefix                           | 24                                                                          |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::200:7ff:fef3:2f00                                                     |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:07:f3:2f:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 80298                                                                       |
|   Input Packets                            | 1538                                                                        |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 344736                                                                      |
|   Output Packets                           | 1561                                                                        |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | remote                                                                      |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | management                                                                  |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef7                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:07:f3:2e:f7                                                           |
| Last Changed                               | Aug 06 2026 20:52:17 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Enabled                                                                     |
| Unsolicited Neighbor Advertisement         | Enabled                                                                     |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | remote-fd                                                                   |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | -                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | -                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | remote-fp1, remote-fp2, remote-fp3, remote-fp4, remote-fp5, remote-fp6,     |
|                                            | remote-fp7, remote-fp8, remote-fp9, remote-fp10, remote-fp11, remote-fp12,  |
|                                            | remote-fp13, remote-fp14, remote-fp15, remote-fp16, remote-fp17,            |
|                                            | remote-fp18, remote-fp19, remote-fp20, remote-fp21, remote-fp22,            |
|                                            | remote-fp23, remote-fp24, remote-fp25, remote-fp26, remote-fp27,            |
|                                            | remote-fp28, remote-fp29, remote-fp30, remote-fp31, remote-fp32,            |
|                                            | remote-fp33, remote-fp34, remote-fp35, remote-fp36, remote-fp37,            |
|                                            | remote-fp38, remote-fp39, remote-fp40, remote-fp41, remote-fp42             |
| Logical Port(s)                            | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,  |
|                                            | 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, |
|                                            |  41, 42                                                                     |
| Classifier(s)                              | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127, default-vid-127, default-vid-127,         |
|                                            | default-vid-127, default-vid-127                                            |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb1                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735925                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.0.2                                                                  |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| IPv6 Addresses                             |                                                                             |
|   IP                                       | fc00:0000:0000:0000:0000:0000:0000:0002                                     |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | STATIC                                                                      |
|   Address Status                           | preferred                                                                   |
|   Secondary IP                             |                                                                             |
|       Preferred                            | -                                                                           |
|       Duplicate                            | -                                                                           |
|       Tentative                            | -                                                                           |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | PE_1-PE_2-if                                                                |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:07:f3:2e:f6                                                           |
| Last Changed                               | Aug 06 2026 20:57:49 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | PE_1-PE_2-FD                                                                |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 31931                                                                       |
|   Input Packets                            | 172                                                                         |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 8                                                                           |
|   Output Octets                            | 36815                                                                       |
|   Output Packets                           | 189                                                                         |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.1.2                                                                  |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
| IPv6 Addresses                             |                                                                             |
|   IP                                       | fc00:0000:0000:0000:0000:0000:0000:0601                                     |
|   Prefix Length                            | 127                                                                         |
|   Origin                                   | STATIC                                                                      |
|   Address Status                           | preferred                                                                   |
|   Secondary IP                             |                                                                             |
|       Preferred                            | -                                                                           |
|       Duplicate                            | -                                                                           |
|       Tentative                            | -                                                                           |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | PE_1-PE_2-FP                                                                |
| Logical Port(s)                            | 1                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb10                                                                        |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | default                                                                     |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735926                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 10.65.0.33                                                                  |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | lb2                                                                         |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | loopback                                                                    |
| Role                                       | data                                                                        |
| VRF Binding                                | L3VPN_2-vrf                                                                 |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073735927                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| Last Changed                               | Aug 06 2026 20:59:01 Local                                                  |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 0                                                                           |
|   Input Packets                            | 0                                                                           |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 0                                                                           |
|   Output Packets                           | 0                                                                           |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.104.33                                                               |
|   Prefix Length                            | 32                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
| Name                                       | CE_2-PE_2-if                                                                 |
| Oper Status                                | UP                                                                          |
| Admin Status                               | UP                                                                          |
| Type                                       | ip                                                                          |
| Role                                       | data                                                                        |
| VRF Binding                                | L3VPN_1-vrf                                                                 |
| IPv6 Link Local Data                       |                                                                             |
|   Address                                  | fe80::e00:7ff:fef3:2ef6                                                     |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731827                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:07:f3:2e:f6                                                           |
| Last Changed                               | Aug 06 2026 20:59:02 Local                                                  |
| Bandwidth (Mbps)                           | 10000                                                                       |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Underlay Binding                           | CE_2-PE_2-FD                                                                 |
| Underlay Binding Type                      | Forwarding Domain                                                           |
| CoS to Frame Map                           | default-c2f                                                                 |
| Frame to CoS Map                           | default-f2c                                                                 |
| Stats Collection                           | on                                                                          |
| Counters                                   |                                                                             |
|   Input Octets                             | 888                                                                         |
|   Input Packets                            | 12                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 1                                                                           |
|   Output Octets                            | 2787                                                                        |
|   Output Packets                           | 25                                                                          |
|   Output Gratuitous ARP Packets            | 0                                                                           |
|   Output Unsolicited Neighbor Adv. Packets | 0                                                                           |
|   Output Router Adv. Packets               | 0                                                                           |
|   Output Router Adv. Octets                | 0                                                                           |
|   Input Router Solicitation Packets        | 0                                                                           |
|   Input Router Solicitation Octets         | 0                                                                           |
| DSCP Remarking                             |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Enabled                                  | False                                                                       |
| IPv4 Addresses                             |                                                                             |
|   IP                                       | 172.16.103.33                                                               |
|   Prefix Length                            | 30                                                                          |
|   Origin                                   | STATIC                                                                      |
|   Secondary IP                             |                                                                             |
|   Secondary IP                             |                                                                             |
| Duplicate Address Detection                |                                                                             |
|   Status                                   | Enabled                                                                     |
| Flow Point(s)                              | CE_2-PE_2-FP                                                                 |
| Logical Port(s)                            | 2                                                                           |
| Classifier(s)                              | CLASSIFIER-UNTAGGED                                                         |
| IPv4 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
| IPv6 uRPF                                  |                                                                             |
|   Origin                                   | Not Configured                                                              |
|   Mode                                     | -                                                                           |
+--------------------------------------------+-----------------------------------------------------------------------------+
```

</details>

## G3: Task 3 — Configure the BGP VRF instance for L3VPN_2-vrf

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show ip routes vrf L3VPN_1-vrf
```

Pass: Output contains `172.16.103.32` and `172.16.0.2`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_1-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
| *>    |  C   |  -  | -                | 172.16.103.0/30    | [0/0]     | -               | CE_1-PE_1-if               | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.103.32/30   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:35    |
|  >    |  B   |  M  | -                | 172.16.104.33/32   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:22    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show ip routes vrf L3VPN_1-vrf
```

Pass: Output contains `172.16.103.0` and `172.16.0.1`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_1-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.0/30    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:35    |
| *>    |  C   |  -  | -                | 172.16.103.32/30   | [0/0]     | -               | CE_2-PE_2-if               | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.104.1/32    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:22    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show ip routes vrf L3VPN_2-vrf
```

Pass: Output contains `172.16.104.33` and `172.16.0.2`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_2-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.32/30   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:22    |
| *>    |  C   |  -  | -                | 172.16.104.1/32    | [0/0]     | -               | lb2                       | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.104.33/32   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:34    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show ip routes vrf L3VPN_2-vrf
```

Pass: Output contains `172.16.104.1` and `172.16.0.1`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_2-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.0/30    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:22    |
|  >    |  B   |  M  | -                | 172.16.104.1/32    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:34    |
| *>    |  C   |  -  | -                | 172.16.104.33/32   | [0/0]     | -               | lb2                       | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show ip routes vrf L3VPN_1-vrf
```

Pass: Output contains `172.16.103.32/30`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_1-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
| *>    |  C   |  -  | -                | 172.16.103.0/30    | [0/0]     | -               | CE_1-PE_1-if               | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.103.32/30   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:35    |
|  >    |  B   |  M  | -                | 172.16.104.33/32   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:22    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show ip routes vrf L3VPN_1-vrf
```

Pass: Output contains `172.16.103.0/30`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_1-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.0/30    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:36    |
| *>    |  C   |  -  | -                | 172.16.103.32/30   | [0/0]     | -               | CE_2-PE_2-if               | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.104.1/32    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:23    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_1**, run:

```saos
ping ip destination 172.16.103.33 vrf L3VPN_1-vrf repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.103.33, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.35 ms  TTL = 255
! seq_num = 2  RTT = 1.40 ms  TTL = 255
! seq_num = 3  RTT = 1.93 ms  TTL = 255
! seq_num = 4  RTT = 1.65 ms  TTL = 255
! seq_num = 5  RTT = 1.50 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 1.40/1.77/2.35
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
ping ip destination 172.16.103.1 vrf L3VPN_1-vrf repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.103.1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 1.96 ms  TTL = 255
! seq_num = 2  RTT = 2.09 ms  TTL = 255
! seq_num = 3  RTT = 3.15 ms  TTL = 255
! seq_num = 4  RTT = 2.55 ms  TTL = 255
! seq_num = 5  RTT = 2.75 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 1.96/2.50/3.15
```

</details>

## G4: Task 4 — Leak routes between L3VPN_1-vrf and L3VPN_2-vrf

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show ip routes vrf L3VPN_1-vrf
```

Pass: Output contains `172.16.104.33` and `172.16.0.2`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_1-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
| *>    |  C   |  -  | -                | 172.16.103.0/30    | [0/0]     | -               | CE_1-PE_1-if               | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.103.32/30   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:46    |
|  >    |  B   |  M  | -                | 172.16.104.33/32   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:33    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show ip routes vrf L3VPN_1-vrf
```

Pass: Output contains `172.16.104.1` and `172.16.0.1`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_1-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.0/30    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:46    |
| *>    |  C   |  -  | -                | 172.16.103.32/30   | [0/0]     | -               | CE_2-PE_2-if               | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.104.1/32    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:33    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show ip routes vrf L3VPN_2-vrf
```

Pass: Output contains `172.16.103.32/30`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_2-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.32/30   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:33    |
| *>    |  C   |  -  | -                | 172.16.104.1/32    | [0/0]     | -               | lb2                       | -               | -                         | -           |
|  >    |  B   |  M  | -                | 172.16.104.33/32   | [200/0]   | 172.16.0.2      | -                         | -               | -                         | 00:00:45    |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show ip routes vrf L3VPN_2-vrf
```

Pass: Output contains `172.16.103.0/30`

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
+----------------------------------------------------------------------------- RIB STATE: L3VPN_2-vrf -----------------------------------------------------------------------------+
|       |      |     |                  |                    |           |                 |                           | Recursive...                                | Last Update |
| State | Type | S/T | Instance         | Destination        | RP/M      | Next Hop        | Interface                 | Next Hop        | Interface                 | (hh:mm:ss)  |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
|  >    |  B   |  M  | -                | 172.16.103.0/30    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:34    |
|  >    |  B   |  M  | -                | 172.16.104.1/32    | [200/0]   | 172.16.0.1      | -                         | -               | -                         | 00:00:46    |
| *>    |  C   |  -  | -                | 172.16.104.33/32   | [0/0]     | -               | lb2                       | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
ping ip destination 172.16.103.1 vrf L3VPN_2-vrf repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.103.1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.05 ms  TTL = 255
! seq_num = 2  RTT = 1.57 ms  TTL = 255
! seq_num = 3  RTT = 1.45 ms  TTL = 255
! seq_num = 4  RTT = 1.95 ms  TTL = 255
! seq_num = 5  RTT = 1.72 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 1.45/1.75/2.05
```

</details>

## G5: Task 5 — Confirm CE_1 and CE_2 are unaffected

<!-- retry: 120s -->
On **CE_1**, run:

```saos
ping ip destination 172.16.103.1 source 172.16.103.2 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.103.1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 1.68 ms  TTL = 255
! seq_num = 2  RTT = 3.19 ms  TTL = 255
! seq_num = 3  RTT = 1.38 ms  TTL = 255
! seq_num = 4  RTT = 2.72 ms  TTL = 255
! seq_num = 5  RTT = 3.40 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 1.38/2.47/3.40
```

</details>

<!-- retry: 120s -->
On **CE_2**, run:

```saos
ping ip destination 172.16.103.33 source 172.16.103.34 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.103.33, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.57 ms  TTL = 255
! seq_num = 2  RTT = 2.40 ms  TTL = 255
! seq_num = 3  RTT = 1.74 ms  TTL = 255
! seq_num = 4  RTT = 1.98 ms  TTL = 255
! seq_num = 5  RTT = 1.64 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 1.64/2.07/2.57
```

</details>
