Deploy `F1-Loopbacks-and-Interfaces`, then run the following validation checks.

## G1: Task 1 — Verify the deployed topology

On **PE_1**, run:

```saos
show lldp neighbors
```

Pass: Output contains `system-name` and `PE_2`

<details><summary>Example output</summary>

```
+--------------- LLDP NEIGHBORS ---------------+
| Parameter                   | Value          |
+-----------------------------+----------------+
| interface                   | 1              |
| chassis-id                  | 0C00CA51D3F1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 1              |
| port-id                     | 1              |
| port-id-subtype             | interface-name |
| system-capability-supported | bridge         |
| system-capability-enabled   | bridge         |
| system-description          | 5162           |
| system-name                 | PE_2           |
| auto-neg-supported          | True           |
| auto-neg-enabled            | False          |
| oper-mau-type               | 33             |
| port-class                  | p-class-pd     |
| mdi-supported               | False          |
| mdi-enabled                 | False          |
| pair-controlable            | False          |
| agg-status                  | capable        |
| max-frame-size              | 1526           |
| man-address-subtype         | ipv4           |
| man-address                 | 10.0.0.15      |
| if-subtype                  | if-index       |
+-----------------------------+----------------+
| interface                   | 2              |
| chassis-id                  | 0C00C94520F1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 1              |
| port-id                     | 1              |
| port-id-subtype             | interface-name |
| system-capability-supported | bridge         |
| system-capability-enabled   | bridge         |
| system-description          | 3984           |
| system-name                 | CE1            |
| auto-neg-supported          | True           |
| auto-neg-enabled            | False          |
| oper-mau-type               | 33             |
| port-class                  | p-class-pd     |
| mdi-supported               | False          |
| mdi-enabled                 | False          |
| pair-controlable            | False          |
| agg-status                  | capable        |
| max-frame-size              | 1526           |
| man-address-subtype         | ipv4           |
| man-address                 | 10.0.0.15      |
| if-subtype                  | if-index       |
+-----------------------------+----------------+
| interface                   | 4              |
| chassis-id                  | 0C00DC6584F1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 3              |
| port-id                     | 3              |
| port-id-subtype             | interface-name |
| system-capability-supported | bridge         |
| system-capability-enabled   | bridge         |
| system-description          | 5162           |
| system-name                 | PE_3           |
| auto-neg-supported          | True           |
| auto-neg-enabled            | False          |
| oper-mau-type               | 33             |
| port-class                  | p-class-pd     |
| mdi-supported               | False          |
| mdi-enabled                 | False          |
| pair-controlable            | False          |
| agg-status                  | capable        |
| max-frame-size              | 1526           |
| man-address-subtype         | ipv4           |
| man-address                 | 10.0.0.15      |
| if-subtype                  | if-index       |
+-----------------------------+----------------+
```

</details>

On **PE_2**, run:

```saos
show lldp neighbors
```

Pass: Output contains `system-name` and `PE_1`

<details><summary>Example output</summary>

```
+--------------- LLDP NEIGHBORS ---------------+
| Parameter                   | Value          |
+-----------------------------+----------------+
| interface                   | 1              |
| chassis-id                  | 0C00711A13F1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 1              |
| port-id                     | 1              |
| port-id-subtype             | interface-name |
| system-capability-supported | bridge         |
| system-capability-enabled   | bridge         |
| system-description          | 5162           |
| system-name                 | PE_1           |
| auto-neg-supported          | True           |
| auto-neg-enabled            | False          |
| oper-mau-type               | 33             |
| port-class                  | p-class-pd     |
| mdi-supported               | False          |
| mdi-enabled                 | False          |
| pair-controlable            | False          |
| agg-status                  | capable        |
| max-frame-size              | 1526           |
| man-address-subtype         | ipv4           |
| man-address                 | 10.0.0.15      |
| if-subtype                  | if-index       |
+-----------------------------+----------------+
| interface                   | 2              |
| chassis-id                  | 0C000F3EBAF1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 1              |
| port-id                     | 1              |
| port-id-subtype             | interface-name |
| system-capability-supported | bridge         |
| system-capability-enabled   | bridge         |
| system-description          | 3984           |
| system-name                 | CE2            |
| auto-neg-supported          | True           |
| auto-neg-enabled            | False          |
| oper-mau-type               | 33             |
| port-class                  | p-class-pd     |
| mdi-supported               | False          |
| mdi-enabled                 | False          |
| pair-controlable            | False          |
| agg-status                  | capable        |
| max-frame-size              | 1526           |
| man-address-subtype         | ipv4           |
| man-address                 | 10.0.0.15      |
| if-subtype                  | if-index       |
+-----------------------------+----------------+
| interface                   | 4              |
| chassis-id                  | 0C00DC6584F1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 1              |
| port-id                     | 1              |
| port-id-subtype             | interface-name |
| system-capability-supported | bridge         |
| system-capability-enabled   | bridge         |
| system-description          | 5162           |
| system-name                 | PE_3           |
| auto-neg-supported          | True           |
| auto-neg-enabled            | False          |
| oper-mau-type               | 33             |
| port-class                  | p-class-pd     |
| mdi-supported               | False          |
| mdi-enabled                 | False          |
| pair-controlable            | False          |
| agg-status                  | capable        |
| max-frame-size              | 1526           |
| man-address-subtype         | ipv4           |
| man-address                 | 10.0.0.15      |
| if-subtype                  | if-index       |
+-----------------------------+----------------+
```

</details>

## G2: Task 2 — Configure IP address on port 1 of PE_1

On **PE_1**, run:

```saos
show ip interfaces
```

Pass: Output contains `lb1` and `172.16.0.1` and `32`

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
|   Address                                  | fe80::200:71ff:fe1a:1400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:14:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 32254                                                                       |
|   Input Packets                            | 557                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 209399                                                                      |
|   Output Packets                           | 580                                                                         |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:13:f7                                                           |
| Last Changed                               | Aug 06 2026 20:25:27 Local                                                  |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f6                                                    |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:13:f6                                                           |
| Last Changed                               | Aug 06 2026 20:32:02 Local                                                  |
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
|   Input Octets                             | 3844                                                                        |
|   Input Packets                            | 44                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 5                                                                           |
|   Output Octets                            | 3930                                                                        |
|   Output Packets                           | 42                                                                          |
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
```

</details>

On **PE_1**, run:

```saos
show forwarding-domains forwarding-domain PE_1-PE_2-FD
```

Pass: Output contains `PE_1-PE_2-FD` and `vpls`

<details><summary>Example output</summary>

```
+- FORWARDING DOMAIN -+
| KEY  | VALUE        |
+------+--------------+
| Name | PE_1-PE_2-FD |
| Mode | vpls         |
+------+--------------+
```

</details>

On **PE_1**, run:

```saos
show flow-points flow-point PE_1-PE_2-FP
```

Pass: Output contains `PE_1-PE_2-FP` and `PE_1-PE_2-FD` and `CLASSIFIER-UNTAGGED`

<details><summary>Example output</summary>

```
+------------------- FLOW POINT -------------------+
| KEY                        | VALUE               |
+----------------------------+---------------------+
| Name                       | PE_1-PE_2-FP        |
| Forwarding Domain Name     | PE_1-PE_2-FD        |
| Logical Port               | 1                   |
| Statistics Collection      | on                  |
| MTU Size                   | 2000                |
| Admin State                | enabled             |
| Classifier List Precedence | 7                   |
| Classifier List            |                     |
|                            | CLASSIFIER-UNTAGGED |
+----------------------------+---------------------+
+------ FLOW POINT STATISTICS -------+
| KEY                 | VALUE        |
+---------------------+--------------+
| Name                | PE_1-PE_2-FP |
| Rx Accepted Bytes   | 4552         |
| Rx Accepted Frames  | 47           |
| Tx Forwarded Bytes  | 3930         |
| Tx Forwarded Frames | 42           |
| Rx Yellow Bytes     | 0            |
| Rx Yellow Frames    | 0            |
| Rx Dropped Bytes    | 0            |
| Rx Dropped Frames   | 0            |
+---------------------+--------------+
+----------- FLOW POINT STATE -----------+
| KEY                 | VALUE            |
+---------------------+------------------+
| Name                | PE_1-PE_2-FP     |
| Oper State          | up               |
| Oper Up Time        | 0 days,0h:0m:22s |
| Egress L2 Transform | -                |
+---------------------+------------------+
```

</details>

On **PE_1**, run:

```saos
show ip interfaces
```

Pass: Output contains `PE_1-PE_2-if` and `172.16.1.1` and `30`

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
|   Address                                  | fe80::200:71ff:fe1a:1400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:14:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 34982                                                                       |
|   Input Packets                            | 618                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 247859                                                                      |
|   Output Packets                           | 638                                                                         |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:13:f7                                                           |
| Last Changed                               | Aug 06 2026 20:25:27 Local                                                  |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f6                                                    |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:13:f6                                                           |
| Last Changed                               | Aug 06 2026 20:32:02 Local                                                  |
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
|   Input Octets                             | 3844                                                                        |
|   Input Packets                            | 44                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 5                                                                           |
|   Output Octets                            | 4058                                                                        |
|   Output Packets                           | 43                                                                          |
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
```

</details>

On **PE_1**, run:

```saos
show forwarding-domains
```

Pass: Output contains `PE_1-PE_2-FD`

<details><summary>Example output</summary>

```
+- FORWARDING DOMAIN -+
| Name         | Mode |
+--------------+------+
| PE_1-PE_2-FD | vpls |
| remote-fd    | vpls |
+--------------+------+
```

</details>

## G3: Task 3 — Configure IP address on port 1 of PE_2

On **PE_2**, run:

```saos
show ip interfaces
```

Pass: Output contains `lb1` and `172.16.0.2` and `32`

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
|   Address                                  | fe80::200:caff:fe51:d400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d4:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 31830                                                                       |
|   Input Packets                            | 545                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 207181                                                                      |
|   Output Packets                           | 567                                                                         |
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
|   Address                                  | fe80::e00:caff:fe51:d3f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d3:f7                                                           |
| Last Changed                               | Aug 06 2026 20:25:04 Local                                                  |
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
|   Address                                  | fe80::e00:caff:fe51:d3f6                                                    |
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
|   Address                                  | fe80::e00:caff:fe51:d3f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d3:f6                                                           |
| Last Changed                               | Aug 06 2026 20:32:05 Local                                                  |
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
|   Input Octets                             | 3182                                                                        |
|   Input Packets                            | 38                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 4                                                                           |
|   Output Octets                            | 4431                                                                        |
|   Output Packets                           | 46                                                                          |
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
```

</details>

On **PE_2**, run:

```saos
show forwarding-domains forwarding-domain PE_1-PE_2-FD
```

Pass: Output contains `PE_1-PE_2-FD` and `vpls`

<details><summary>Example output</summary>

```
+- FORWARDING DOMAIN -+
| KEY  | VALUE        |
+------+--------------+
| Name | PE_1-PE_2-FD |
| Mode | vpls         |
+------+--------------+
```

</details>

On **PE_2**, run:

```saos
show flow-points flow-point PE_1-PE_2-FP
```

Pass: Output contains `PE_1-PE_2-FP` and `PE_1-PE_2-FD` and `CLASSIFIER-UNTAGGED`

<details><summary>Example output</summary>

```
+------------------- FLOW POINT -------------------+
| KEY                        | VALUE               |
+----------------------------+---------------------+
| Name                       | PE_1-PE_2-FP        |
| Forwarding Domain Name     | PE_1-PE_2-FD        |
| Logical Port               | 1                   |
| Statistics Collection      | on                  |
| MTU Size                   | 2000                |
| Admin State                | enabled             |
| Classifier List Precedence | 7                   |
| Classifier List            |                     |
|                            | CLASSIFIER-UNTAGGED |
+----------------------------+---------------------+
+------ FLOW POINT STATISTICS -------+
| KEY                 | VALUE        |
+---------------------+--------------+
| Name                | PE_1-PE_2-FP |
| Rx Accepted Bytes   | 3562         |
| Rx Accepted Frames  | 39           |
| Tx Forwarded Bytes  | 4431         |
| Tx Forwarded Frames | 46           |
| Rx Yellow Bytes     | 0            |
| Rx Yellow Frames    | 0            |
| Rx Dropped Bytes    | 0            |
| Rx Dropped Frames   | 0            |
+---------------------+--------------+
+----------- FLOW POINT STATE -----------+
| KEY                 | VALUE            |
+---------------------+------------------+
| Name                | PE_1-PE_2-FP     |
| Oper State          | up               |
| Oper Up Time        | 0 days,0h:0m:21s |
| Egress L2 Transform | -                |
+---------------------+------------------+
```

</details>

On **PE_2**, run:

```saos
show ip interfaces
```

Pass: Output contains `PE_1-PE_2-if` and `172.16.1.2` and `30`

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
|   Address                                  | fe80::200:caff:fe51:d400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d4:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 34878                                                                       |
|   Input Packets                            | 614                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 246843                                                                      |
|   Output Packets                           | 636                                                                         |
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
|   Address                                  | fe80::e00:caff:fe51:d3f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d3:f7                                                           |
| Last Changed                               | Aug 06 2026 20:25:04 Local                                                  |
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
|   Address                                  | fe80::e00:caff:fe51:d3f6                                                    |
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
|   Address                                  | fe80::e00:caff:fe51:d3f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d3:f6                                                           |
| Last Changed                               | Aug 06 2026 20:32:05 Local                                                  |
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
|   Input Octets                             | 3182                                                                        |
|   Input Packets                            | 38                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 4                                                                           |
|   Output Octets                            | 4431                                                                        |
|   Output Packets                           | 46                                                                          |
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
```

</details>

On **PE_2**, run:

```saos
show forwarding-domains
```

Pass: Output contains `PE_1-PE_2-FD`

<details><summary>Example output</summary>

```
+- FORWARDING DOMAIN -+
| Name         | Mode |
+--------------+------+
| PE_1-PE_2-FD | vpls |
| remote-fd    | vpls |
+--------------+------+
```

</details>

## G4: Task 4 — Confirm the IP configuration

On **PE_1**, run:

```saos
show ip routes
```

Pass: Output contains `172.16.0.1` and `lb1` and `PE_1-PE_2-if`

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
| *>    |  K   |  -  | -                | 0.0.0.0/0          | [254/0]   | 10.0.0.2        | mgmtbr0                   | -               | -                         | -           |
| *>    |  C   |  -  | -                | 10.0.0.0/24        | [0/0]     | -               | mgmtbr0                   | -               | -                         | -           |
| *>    |  C   |  -  | -                | 172.16.0.1/32      | [0/0]     | -               | lb1                       | -               | -                         | -           |
| *>    |  C   |  -  | -                | 172.16.1.0/30      | [0/0]     | -               | PE_1-PE_2-if              | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

On **PE_2**, run:

```saos
show ip routes
```

Pass: Output contains `172.16.0.2` and `lb1` and `PE_1-PE_2-if`

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
| *>    |  K   |  -  | -                | 0.0.0.0/0          | [254/0]   | 10.0.0.2        | mgmtbr0                   | -               | -                         | -           |
| *>    |  C   |  -  | -                | 10.0.0.0/24        | [0/0]     | -               | mgmtbr0                   | -               | -                         | -           |
| *>    |  C   |  -  | -                | 172.16.0.2/32      | [0/0]     | -               | lb1                       | -               | -                         | -           |
| *>    |  C   |  -  | -                | 172.16.1.0/30      | [0/0]     | -               | PE_1-PE_2-if              | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 60s -->
On **PE_1**, run:

```saos
ping ip destination 172.16.1.2 source 172.16.1.1 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to 172.16.1.2, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.37 ms  TTL = 255
! seq_num = 2  RTT = 2.71 ms  TTL = 255
! seq_num = 3  RTT = 3.51 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 2.37/2.86/3.51
```

</details>

<!-- retry: 60s -->
On **PE_2**, run:

```saos
ping ip destination 172.16.1.1 source 172.16.1.2 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to 172.16.1.1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 3.01 ms  TTL = 255
! seq_num = 2  RTT = 1.84 ms  TTL = 255
! seq_num = 3  RTT = 2.72 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 1.84/2.52/3.01
```

</details>

## G5: Task 5 — Apply IPv6 addresses

On **PE_1**, run:

```saos
show ipv6 interfaces
```

Pass: Output contains `lb1` and `fc00:0000:0000:0000:0000:0000:0000:0001` and `128`

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
|   Address                                  | fe80::200:71ff:fe1a:1400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:14:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 38110                                                                       |
|   Input Packets                            | 687                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 288543                                                                      |
|   Output Packets                           | 704                                                                         |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:13:f7                                                           |
| Last Changed                               | Aug 06 2026 20:25:27 Local                                                  |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f6                                                    |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:13:f6                                                           |
| Last Changed                               | Aug 06 2026 20:32:02 Local                                                  |
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
|   Input Octets                             | 4372                                                                        |
|   Input Packets                            | 50                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 5                                                                           |
|   Output Octets                            | 4791                                                                        |
|   Output Packets                           | 50                                                                          |
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
```

</details>

On **PE_2**, run:

```saos
show ipv6 interfaces
```

Pass: Output contains `lb1` and `fc00:0000:0000:0000:0000:0000:0000:0002` and `128`

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
|   Address                                  | fe80::200:caff:fe51:d400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d4:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 38326                                                                       |
|   Input Packets                            | 691                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 288697                                                                      |
|   Output Packets                           | 713                                                                         |
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
|   Address                                  | fe80::e00:caff:fe51:d3f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d3:f7                                                           |
| Last Changed                               | Aug 06 2026 20:25:04 Local                                                  |
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
|   Address                                  | fe80::e00:caff:fe51:d3f6                                                    |
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
|   Address                                  | fe80::e00:caff:fe51:d3f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d3:f6                                                           |
| Last Changed                               | Aug 06 2026 20:32:05 Local                                                  |
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
|   Input Octets                             | 3710                                                                        |
|   Input Packets                            | 44                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 4                                                                           |
|   Output Octets                            | 5164                                                                        |
|   Output Packets                           | 53                                                                          |
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
```

</details>

On **PE_1**, run:

```saos
show ipv6 interfaces
```

Pass: Output contains `fc00:0000:0000:0000:0000:0000:0000:0600` and `127`

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
|   Address                                  | fe80::200:71ff:fe1a:1400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:14:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 40134                                                                       |
|   Input Packets                            | 734                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 323769                                                                      |
|   Output Packets                           | 751                                                                         |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:13:f7                                                           |
| Last Changed                               | Aug 06 2026 20:25:27 Local                                                  |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f6                                                    |
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
|   Address                                  | fe80::e00:71ff:fe1a:13f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:71:1a:13:f6                                                           |
| Last Changed                               | Aug 06 2026 20:32:02 Local                                                  |
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
|   Input Octets                             | 4372                                                                        |
|   Input Packets                            | 50                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 5                                                                           |
|   Output Octets                            | 5164                                                                        |
|   Output Packets                           | 51                                                                          |
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
```

</details>

On **PE_2**, run:

```saos
show ipv6 interfaces
```

Pass: Output contains `fc00:0000:0000:0000:0000:0000:0000:0601` and `127`

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
|   Address                                  | fe80::200:caff:fe51:d400                                                    |
|   Prefix Length                            | 128                                                                         |
|   Origin                                   | AUTO                                                                        |
| Interface Index                            | 56                                                                          |
| Description                                | bridge interface for out of band management port/local management interface |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d4:00                                                           |
| Bandwidth (Mbps)                           | 0                                                                           |
| Gratuitous ARP                             | Disabled                                                                    |
| Unsolicited Neighbor Advertisement         | Disabled                                                                    |
| Router Advertisement                       | Disabled                                                                    |
| Counters                                   |                                                                             |
|   Input Octets                             | 39950                                                                       |
|   Input Packets                            | 728                                                                         |
|   Input Dropped Octets                     | -                                                                           |
|   Input Dropped Packets                    | 0                                                                           |
|   Output Octets                            | 322839                                                                      |
|   Output Packets                           | 750                                                                         |
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
|   Address                                  | fe80::e00:caff:fe51:d3f7                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731825                                                                  |
| Description                                | in band remote management interface                                         |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d3:f7                                                           |
| Last Changed                               | Aug 06 2026 20:25:04 Local                                                  |
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
|   Address                                  | fe80::e00:caff:fe51:d3f6                                                    |
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
|   Address                                  | fe80::e00:caff:fe51:d3f6                                                    |
|   Prefix Length                            | 64                                                                          |
|   Origin                                   | AUTO                                                                        |
|   Address Status                           | preferred                                                                   |
| Interface Index                            | 1073731826                                                                  |
| Description                                | -                                                                           |
| MTU                                        | 1500                                                                        |
| MAC Address                                | 0c:00:ca:51:d3:f6                                                           |
| Last Changed                               | Aug 06 2026 20:32:05 Local                                                  |
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
|   Input Octets                             | 3710                                                                        |
|   Input Packets                            | 44                                                                          |
|   Input Dropped Octets                     | 0                                                                           |
|   Input Dropped Packets                    | 4                                                                           |
|   Output Octets                            | 5292                                                                        |
|   Output Packets                           | 54                                                                          |
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
```

</details>

## G6: Task 6 — Confirm the IPv6 configuration

<!-- retry: 60s -->
On **PE_1**, run:

```saos
ping ip destination FC00::601 source FC00::600 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to FC00::601, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.43 ms  TTL = 255
! seq_num = 2  RTT = 3.32 ms  TTL = 255
! seq_num = 3  RTT = 2.99 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 2.43/2.91/3.32
```

</details>

<!-- retry: 60s -->
On **PE_2**, run:

```saos
ping ip destination FC00::600 source FC00::601 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to FC00::600, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.96 ms  TTL = 255
! seq_num = 2  RTT = 3.11 ms  TTL = 255
! seq_num = 3  RTT = 2.96 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 2.96/3.01/3.11
```

</details>
