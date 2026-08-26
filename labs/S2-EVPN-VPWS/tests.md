Deploy `S2-EVPN-VPWS`, then run the following validation checks.

## G1: Task 1 — Verify the deployed topology

<!-- retry: 60s -->
On **CE_1**, run:

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
| chassis-id                  | 0C009BC6F3F1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 2              |
| port-id                     | 2              |
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
```

</details>

<!-- retry: 60s -->
On **PE_1**, run:

```saos
show lldp neighbors
```

Pass: Output contains `system-name` and `CE_1`

<details><summary>Example output</summary>

```
+--------------- LLDP NEIGHBORS ---------------+
| Parameter                   | Value          |
+-----------------------------+----------------+
| interface                   | 1              |
| chassis-id                  | 0C002FB9EDF1   |
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
| chassis-id                  | 0C0045A10CF1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 1              |
| port-id                     | 1              |
| port-id-subtype             | interface-name |
| system-capability-supported | bridge         |
| system-capability-enabled   | bridge         |
| system-description          | 3984           |
| system-name                 | CE_1            |
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
| chassis-id                  | 0C007EA79BF1   |
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

## G2: Task 2 — Extend the SR-MPLS core to PE_3

<!-- retry: 120s -->
On **PE_3**, run:

```saos
show isis neighbors
```

Pass: Output contains `0172.0016.0001` and `0172.0016.0002` and `Up`

<details><summary>Example output</summary>

```
+-------------------------------------- ISIS NEIGHBOR STATE: Bootcamp ---------------------------------------+
| Neighbor |                        |                  |                |       |   Hold   |      |          |
|   Type   |       System ID        |    Interface     |      SNPA      | State | Time (s) | Type | Protocol |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
|   P2P    |     0172.0016.0002     |   PE_2-PE_3-if   | 0c00.2fb9.edf6 |    Up |       26 |  L1  |  IS-IS   |
|   P2P    |     0172.0016.0001     |   PE_1-PE_3-if   | 0c00.9bc6.f3f6 |    Up |       24 |  L1  |  IS-IS   |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
```

</details>

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show isis neighbors
```

Pass: Output contains `0172.0016.0005` and `Up`

<details><summary>Example output</summary>

```
+-------------------------------------- ISIS NEIGHBOR STATE: Bootcamp ---------------------------------------+
| Neighbor |                        |                  |                |       |   Hold   |      |          |
|   Type   |       System ID        |    Interface     |      SNPA      | State | Time (s) | Type | Protocol |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
|   P2P    |     0172.0016.0002     |   PE_1-PE_2-if   | 0c00.2fb9.edf6 |    Up |       28 |  L1  |  IS-IS   |
|   P2P    |     0172.0016.0005     |   PE_1-PE_3-if   | 0c00.7ea7.9bf6 |    Up |       20 |  L1  |  IS-IS   |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
show isis neighbors
```

Pass: Output contains `0172.0016.0005` and `Up`

<details><summary>Example output</summary>

```
+-------------------------------------- ISIS NEIGHBOR STATE: Bootcamp ---------------------------------------+
| Neighbor |                        |                  |                |       |   Hold   |      |          |
|   Type   |       System ID        |    Interface     |      SNPA      | State | Time (s) | Type | Protocol |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
|   P2P    |     0172.0016.0001     |   PE_1-PE_2-if   | 0c00.9bc6.f3f6 |    Up |       29 |  L1  |  IS-IS   |
|   P2P    |     0172.0016.0005     |   PE_2-PE_3-if   | 0c00.7ea7.9bf6 |    Up |       20 |  L1  |  IS-IS   |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
```

</details>

On **PE_3**, run:

```saos
show segment-routing connected-prefix-sid-map
```

Pass: Output contains `172.16.0.5` and `lb1`

<details><summary>Example output</summary>

```
+----- SEGMENT-ROUTING SID MAP -----+
|  Name             |  Value        |
+-------------------+---------------+
| Prefix            | 172.16.0.5/32 |
| Interface         | lb1           |
| Value Type        | Index         |
| Start SID         | 5             |
| Range             | 1             |
| Algorithm         | SPF           |
| Last Hop Behavior | -             |
+-------------------+---------------+
```

</details>

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show isis segment-routing mapping-table status active
```

Pass: Output contains `172.16.0.5/32`

<details><summary>Example output</summary>

```
+---------- ISIS SEGMENT-ROUTING MAPPING TABLE ACTIVE -----------+
| ISIS Instance |  Entry Prefix | SID Index | Range | Preference |
+---------------+---------------+-----------+-------+------------+
|    Bootcamp   | 172.16.0.1/32 |         1 |     1 |        192 |
|    Bootcamp   | 172.16.0.2/32 |         2 |     1 |        192 |
|    Bootcamp   | 172.16.0.5/32 |         5 |     1 |        192 |
+---------------+---------------+-----------+-------+------------+
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
show isis segment-routing mapping-table status active
```

Pass: Output contains `172.16.0.5/32`

<details><summary>Example output</summary>

```
+---------- ISIS SEGMENT-ROUTING MAPPING TABLE ACTIVE -----------+
| ISIS Instance |  Entry Prefix | SID Index | Range | Preference |
+---------------+---------------+-----------+-------+------------+
|    Bootcamp   | 172.16.0.1/32 |         1 |     1 |        192 |
|    Bootcamp   | 172.16.0.2/32 |         2 |     1 |        192 |
|    Bootcamp   | 172.16.0.5/32 |         5 |     1 |        192 |
+---------------+---------------+-----------+-------+------------+
```

</details>

## G3: Task 3 — Extend the iBGP overlay

<!-- retry: 180s -->
On **PE_3**, run:

```saos
show bgp peers
```

Pass: Output contains `172.16.0.1` and `172.16.0.2` and `Established`

<details><summary>Example output</summary>

```
+-------------------------------------------------------------------------- BGP PEERS --------------------------------------------------------------------------+
|                                             |        |          | Up         | Peer    | Received | Advertised | Last       | Received | Sent   |             |
|                                             | Remote | Peer     | Time       | Table   | Pkt      | Pkt        | Reset      | Prefix   | Prefix |             |
| Peer                                        | AS     | Type     | (hh:mm:ss) | Version | Count    | Count      | (hh:mm:ss) | Count    | Count  | State       |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
| 172.16.0.2                                  | 65032  | internal | 00:00:25   | 3       | 2        | 3          | -          | 0        | 1      | Established |
| 172.16.0.1                                  | 65032  | internal | 00:00:25   | 3       | 3        | 3          | -          | 1        | 1      | Established |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_1**, run:

```saos
show bgp peers
```

Pass: Output contains `172.16.0.5` and `Established`

<details><summary>Example output</summary>

```
+-------------------------------------------------------------------------- BGP PEERS --------------------------------------------------------------------------+
|                                             |        |          | Up         | Peer    | Received | Advertised | Last       | Received | Sent   |             |
|                                             | Remote | Peer     | Time       | Table   | Pkt      | Pkt        | Reset      | Prefix   | Prefix |             |
| Peer                                        | AS     | Type     | (hh:mm:ss) | Version | Count    | Count      | (hh:mm:ss) | Count    | Count  | State       |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
| 172.16.0.5                                  | 65032  | internal | 00:00:25   | 2       | 2        | 2          | -          | 1        | 1      | Established |
| 172.16.0.2                                  | 65032  | internal | 00:01:27   | 2       | 6        | 7          | -          | 1        | 2      | Established |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
```

</details>

<!-- retry: 180s -->
On **PE_2**, run:

```saos
show bgp peers
```

Pass: Output contains `172.16.0.5` and `Established`

<details><summary>Example output</summary>

```
+-------------------------------------------------------------------------- BGP PEERS --------------------------------------------------------------------------+
|                                             |        |          | Up         | Peer    | Received | Advertised | Last       | Received | Sent   |             |
|                                             | Remote | Peer     | Time       | Table   | Pkt      | Pkt        | Reset      | Prefix   | Prefix |             |
| Peer                                        | AS     | Type     | (hh:mm:ss) | Version | Count    | Count      | (hh:mm:ss) | Count    | Count  | State       |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
| 172.16.0.5                                  | 65032  | internal | 00:00:25   | 1       | 2        | 1          | -          | 1        | 0      | Established |
| 172.16.0.1                                  | 65032  | internal | 00:01:28   | 2       | 8        | 7          | -          | 2        | 1      | Established |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
```

</details>

## G4: Task 4 — Configure EVPN-VPWS

On **PE_1**, run:

```saos
show forwarding-domains forwarding-domain vpws_1-fd
```

Pass: Output contains `vpws_1-fd` and `evpn-vpws`

<details><summary>Example output</summary>

```
+ FORWARDING DOMAIN +
| KEY  | VALUE      |
+------+------------+
| Name | vpws_1-fd  |
| Mode | evpn-vpws  |
+------+------------+
```

</details>

On **PE_3**, run:

```saos
show forwarding-domains forwarding-domain vpws_1-fd
```

Pass: Output contains `vpws_1-fd` and `evpn-vpws`

<details><summary>Example output</summary>

```
+ FORWARDING DOMAIN +
| KEY  | VALUE      |
+------+------------+
| Name | vpws_1-fd  |
| Mode | evpn-vpws  |
+------+------------+
```

</details>

On **PE_1**, run:

```saos
show classifiers
```

Pass: Output contains `CLASSIFIER-105` and `105`

<details><summary>Example output</summary>

```
+---------------------- CLASSIFIER ---------------------+
| Name                | Filter Parameter                |
+---------------------+---------------------------------+
| CLASSIFIER-105      | Classifier:single-tagged        |
| CLASSIFIER-UNTAGGED | ciena-mef-classifier:vtag-stack |
| default-vid-127     | Classifier:single-tagged        |
+---------------------+---------------------------------+
```

</details>

On **PE_3**, run:

```saos
show classifiers
```

Pass: Output contains `CLASSIFIER-105` and `105`

<details><summary>Example output</summary>

```
+---------------------- CLASSIFIER ---------------------+
| Name                | Filter Parameter                |
+---------------------+---------------------------------+
| CLASSIFIER-105      | Classifier:single-tagged        |
| CLASSIFIER-UNTAGGED | ciena-mef-classifier:vtag-stack |
| default-vid-127     | Classifier:single-tagged        |
+---------------------+---------------------------------+
```

</details>

## G5: Task 5 — Configure the customer attachment circuits

On **CE_1**, run:

```saos
show flow-points flow-point CE_1-CE_2-FP
```

Pass: Output contains `CE_1-CE_2-FP` and `CE_1-CE_2-FD` and `push-vid-105`

<details><summary>Example output</summary>

```
+--------------- FLOW POINT --------------+
| KEY                    | VALUE          |
+------------------------+----------------+
| Name                   | CE_1-CE_2-FP     |
| Forwarding Domain Name | CE_1-CE_2-FD     |
| Logical Port           | 1              |
| Statistics Collection  | on             |
| MTU Size               | 2000           |
| Admin State            | enabled        |
| Egress L2 Transform    |                |
|   Egress Name          | push-vid-105   |
|   Egress VLAN Stack    |                |
|     Tag                | 1              |
|     Push TPID          | tpid-8100      |
|     Push VID           | 105            |
| Classifier List        |                |
|                        | CLASSIFIER-105 |
+------------------------+----------------+
+----- FLOW POINT STATISTICS ------+
| KEY                 | VALUE      |
+---------------------+------------+
| Name                | CE_1-CE_2-FP |
| Rx Accepted Bytes   | 244        |
| Rx Accepted Frames  | 2          |
| Tx Forwarded Bytes  | 574        |
| Tx Forwarded Frames | 5          |
| Rx Yellow Bytes     | 0          |
| Rx Yellow Frames    | 0          |
| Rx Dropped Bytes    | 0          |
| Rx Dropped Frames   | 0          |
+---------------------+------------+
+----------- FLOW POINT STATE ----------+
| KEY                 | VALUE           |
+---------------------+-----------------+
| Name                | CE_1-CE_2-FP      |
| Oper State          | up              |
| Oper Up Time        | 0 days,0h:0m:8s |
| Egress L2 Transform |                 |
|   Egress VLAN Stack |                 |
|     Tag             | 1               |
|     Push TPID       | tpid-8100       |
|     Push VID        | 105             |
+---------------------+-----------------+
```

</details>

## G6: Task 6 — Verify the service

On **CE_2**, run:

```saos
show flow-points flow-point CE_1-CE_2-FP
```

Pass: Output contains `CE_1-CE_2-FP` and `CE_1-CE_2-FD` and `push-vid-105`

<details><summary>Example output</summary>

```
+--------------- FLOW POINT --------------+
| KEY                    | VALUE          |
+------------------------+----------------+
| Name                   | CE_1-CE_2-FP     |
| Forwarding Domain Name | CE_1-CE_2-FD     |
| Logical Port           | 2              |
| Statistics Collection  | on             |
| MTU Size               | 2000           |
| Admin State            | enabled        |
| Egress L2 Transform    |                |
|   Egress Name          | push-vid-105   |
|   Egress VLAN Stack    |                |
|     Tag                | 1              |
|     Push TPID          | tpid-8100      |
|     Push VID           | 105            |
| Classifier List        |                |
|                        | CLASSIFIER-105 |
+------------------------+----------------+
+----- FLOW POINT STATISTICS ------+
| KEY                 | VALUE      |
+---------------------+------------+
| Name                | CE_1-CE_2-FP |
| Rx Accepted Bytes   | 0          |
| Rx Accepted Frames  | 0          |
| Tx Forwarded Bytes  | 708        |
| Tx Forwarded Frames | 6          |
| Rx Yellow Bytes     | 0          |
| Rx Yellow Frames    | 0          |
| Rx Dropped Bytes    | 0          |
| Rx Dropped Frames   | 0          |
+---------------------+------------+
+----------- FLOW POINT STATE ----------+
| KEY                 | VALUE           |
+---------------------+-----------------+
| Name                | CE_1-CE_2-FP      |
| Oper State          | up              |
| Oper Up Time        | 0 days,0h:0m:4s |
| Egress L2 Transform |                 |
|   Egress VLAN Stack |                 |
|     Tag             | 1               |
|     Push TPID       | tpid-8100       |
|     Push VID        | 105             |
+---------------------+-----------------+
```

</details>
