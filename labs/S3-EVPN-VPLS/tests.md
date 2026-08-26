Deploy `S3-EVPN-VPLS`, then run the following validation checks.

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
| chassis-id                  | 0C008A2347F1   |
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
On **CE_2**, run:

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
| chassis-id                  | 0C00714D89F1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 2              |
| port-id                     | 2              |
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
```

</details>

<!-- retry: 60s -->
On **CE_3**, run:

```saos
show lldp neighbors
```

Pass: Output contains `system-name` and `PE_3`

<details><summary>Example output</summary>

```
+--------------- LLDP NEIGHBORS ---------------+
| Parameter                   | Value          |
+-----------------------------+----------------+
| interface                   | 1              |
| chassis-id                  | 0C00AC57DDF1   |
| chassis-id-subtype          | mac-address    |
| port-desc                   | 2              |
| port-id                     | 2              |
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
| 172.16.0.5                                  | 65032  | internal | 00:02:30   | 6       | 5        | 5          | -          | 2        | 2      | Established |
| 172.16.0.2                                  | 65032  | internal | 00:02:41   | 2       | 9        | 9          | -          | 3        | 3      | Established |
+---------------------------------------------+--------+----------+------------+---------+----------+------------+------------+----------+--------+-------------+
```

</details>

## G2: Task 2 — Configure the EVPN-VPLS MAC-VRF on the PEs

On **PE_1**, run:

```saos
show forwarding-domains forwarding-domain elan_1-fd
```

Pass: Output contains `elan_1-fd` and `evpn-vpls`

<details><summary>Example output</summary>

```
+ FORWARDING DOMAIN +
| KEY  | VALUE      |
+------+------------+
| Name | elan_1-fd  |
| Mode | evpn-vpls  |
+------+------------+
```

</details>

On **PE_2**, run:

```saos
show forwarding-domains forwarding-domain elan_1-fd
```

Pass: Output contains `elan_1-fd` and `evpn-vpls`

<details><summary>Example output</summary>

```
+ FORWARDING DOMAIN +
| KEY  | VALUE      |
+------+------------+
| Name | elan_1-fd  |
| Mode | evpn-vpls  |
+------+------------+
```

</details>

On **PE_3**, run:

```saos
show forwarding-domains forwarding-domain elan_1-fd
```

Pass: Output contains `elan_1-fd` and `evpn-vpls`

<details><summary>Example output</summary>

```
+ FORWARDING DOMAIN +
| KEY  | VALUE      |
+------+------------+
| Name | elan_1-fd  |
| Mode | evpn-vpls  |
+------+------------+
```

</details>

On **PE_1**, run:

```saos
show classifiers
```

Pass: Output contains `CLASSIFIER-106` and `106`

<details><summary>Example output</summary>

```
+---------------------- CLASSIFIER ---------------------+
| Name                | Filter Parameter                |
+---------------------+---------------------------------+
| CLASSIFIER-106      | Classifier:single-tagged        |
| CLASSIFIER-UNTAGGED | ciena-mef-classifier:vtag-stack |
| default-vid-127     | Classifier:single-tagged        |
+---------------------+---------------------------------+
```

</details>

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show evpn instances
```

Pass: Output contains `103` and `0:103:103`

<details><summary>Example output</summary>

```
+-------------------------------------- EVPN INSTANCE STATE ---------------------------------------+
|         | Route          | Route     |       SR Policy        |       Number of       |   SRv6   |
| EVPN ID | Distinguisher  | Targets   |    Color    | Fallback | Cross-Connect Entries |  Locator |
+---------+----------------+-----------+-------------+----------+-----------------------+----------+
| 103     | 172.16.0.1:103 | 0:103:103 |      -      |  enable  |           1           |    -     |
+---------+----------------+-----------+-------------+----------+-----------------------+----------+
```

</details>

## G3: Task 3 — Configure customer edge CE_1

On **CE_1**, run:

```saos
show flow-points flow-point CE_1-PE_1-FP
```

Pass: Output contains `CE_1-PE_1-FP` and `CE_1-PE_1-FD` and `push-vid-106`

<details><summary>Example output</summary>

```
+--------------- FLOW POINT --------------+
| KEY                    | VALUE          |
+------------------------+----------------+
| Name                   | CE_1-PE_1-FP   |
| Forwarding Domain Name | CE_1-PE_1-FD   |
| Logical Port           | 1              |
| Statistics Collection  | on             |
| MTU Size               | 2000           |
| Admin State            | enabled        |
| Egress L2 Transform    |                |
|   Egress Name          | push-vid-106   |
|   Egress VLAN Stack    |                |
|     Tag                | 1              |
|     Push TPID          | tpid-8100      |
|     Push VID           | 106            |
| Classifier List        |                |
|                        | CLASSIFIER-106 |
+------------------------+----------------+
+------ FLOW POINT STATISTICS -------+
| KEY                 | VALUE        |
+---------------------+--------------+
| Name                | CE_1-PE_1-FP |
| Rx Accepted Bytes   | 86728042     |
| Rx Accepted Frames  | 889874       |
| Tx Forwarded Bytes  | 4796         |
| Tx Forwarded Frames | 53           |
| Rx Yellow Bytes     | 0            |
| Rx Yellow Frames    | 0            |
| Rx Dropped Bytes    | 0            |
| Rx Dropped Frames   | 396870       |
+---------------------+--------------+
+----------- FLOW POINT STATE -----------+
| KEY                 | VALUE            |
+---------------------+------------------+
| Name                | CE_1-PE_1-FP     |
| Oper State          | up               |
| Oper Up Time        | 0 days,0h:1m:31s |
| Egress L2 Transform |                  |
|   Egress VLAN Stack |                  |
|     Tag             | 1                |
|     Push TPID       | tpid-8100        |
|     Push VID        | 106              |
+---------------------+------------------+
```

</details>

## G4: Task 4 — Configure customer edge CE_2

On **CE_2**, run:

```saos
show flow-points flow-point CE_2-PE_2-FP
```

Pass: Output contains `CE_2-PE_2-FP` and `CE_2-PE_2-FD` and `push-vid-106`

<details><summary>Example output</summary>

```
+--------------- FLOW POINT --------------+
| KEY                    | VALUE          |
+------------------------+----------------+
| Name                   | CE_2-PE_2-FP   |
| Forwarding Domain Name | CE_2-PE_2-FD   |
| Logical Port           | 1              |
| Statistics Collection  | on             |
| MTU Size               | 2000           |
| Admin State            | enabled        |
| Egress L2 Transform    |                |
|   Egress Name          | push-vid-106   |
|   Egress VLAN Stack    |                |
|     Tag                | 1              |
|     Push TPID          | tpid-8100      |
|     Push VID           | 106            |
| Classifier List        |                |
|                        | CLASSIFIER-106 |
+------------------------+----------------+
+------ FLOW POINT STATISTICS -------+
| KEY                 | VALUE        |
+---------------------+--------------+
| Name                | CE_2-PE_2-FP |
| Rx Accepted Bytes   | 66881244     |
| Rx Accepted Frames  | 674482       |
| Tx Forwarded Bytes  | 1672564      |
| Tx Forwarded Frames | 26116        |
| Rx Yellow Bytes     | 0            |
| Rx Yellow Frames    | 0            |
| Rx Dropped Bytes    | 0            |
| Rx Dropped Frames   | 271287       |
+---------------------+--------------+
+----------- FLOW POINT STATE -----------+
| KEY                 | VALUE            |
+---------------------+------------------+
| Name                | CE_2-PE_2-FP     |
| Oper State          | up               |
| Oper Up Time        | 0 days,0h:1m:31s |
| Egress L2 Transform |                  |
|   Egress VLAN Stack |                  |
|     Tag             | 1                |
|     Push TPID       | tpid-8100        |
|     Push VID        | 106              |
+---------------------+------------------+
```

</details>

<!-- retry: 60s -->
On **CE_1**, run:

```saos
ping ip destination 172.16.106.2 source 172.16.106.1 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.106.2, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 5.43 ms  TTL = 255
! seq_num = 2  RTT = 8.87 ms  TTL = 255
! seq_num = 3  RTT = 6.77 ms  TTL = 255
! seq_num = 4  RTT = 7.89 ms  TTL = 255
! seq_num = 5  RTT = 6.28 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 5.43/7.05/8.87
```

</details>

## G5: Task 5 — Configure customer edge CE_3 and verify the E-LAN

On **CE_3**, run:

```saos
show flow-points flow-point CE_3-PE_3-FP
```

Pass: Output contains `CE_3-PE_3-FP` and `CE_3-PE_3-FD` and `push-vid-106`

<details><summary>Example output</summary>

```
+--------------- FLOW POINT --------------+
| KEY                    | VALUE          |
+------------------------+----------------+
| Name                   | CE_3-PE_3-FP   |
| Forwarding Domain Name | CE_3-PE_3-FD   |
| Logical Port           | 1              |
| Statistics Collection  | on             |
| MTU Size               | 2000           |
| Admin State            | enabled        |
| Egress L2 Transform    |                |
|   Egress Name          | push-vid-106   |
|   Egress VLAN Stack    |                |
|     Tag                | 1              |
|     Push TPID          | tpid-8100      |
|     Push VID           | 106            |
| Classifier List        |                |
|                        | CLASSIFIER-106 |
+------------------------+----------------+
+------ FLOW POINT STATISTICS -------+
| KEY                 | VALUE        |
+---------------------+--------------+
| Name                | CE_3-PE_3-FP |
| Rx Accepted Bytes   | 30909270     |
| Rx Accepted Frames  | 329440       |
| Tx Forwarded Bytes  | 4310760      |
| Tx Forwarded Frames | 67330        |
| Rx Yellow Bytes     | 0            |
| Rx Yellow Frames    | 0            |
| Rx Dropped Bytes    | 0            |
| Rx Dropped Frames   | 114946       |
+---------------------+--------------+
+----------- FLOW POINT STATE ----------+
| KEY                 | VALUE           |
+---------------------+-----------------+
| Name                | CE_3-PE_3-FP    |
| Oper State          | up              |
| Oper Up Time        | 0 days,0h:1m:7s |
| Egress L2 Transform |                 |
|   Egress VLAN Stack |                 |
|     Tag             | 1               |
|     Push TPID       | tpid-8100       |
|     Push VID        | 106             |
+---------------------+-----------------+
```

</details>

<!-- retry: 60s -->
On **CE_1**, run:

```saos
ping ip destination 172.16.106.3 source 172.16.106.1 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.106.3, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 5.00 ms  TTL = 255
! seq_num = 2  RTT = 4.51 ms  TTL = 255
! seq_num = 3  RTT = 6.62 ms  TTL = 255
! seq_num = 4  RTT = 6.71 ms  TTL = 255
! seq_num = 5  RTT = 6.23 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 4.51/5.81/6.71
```

</details>

<!-- retry: 60s -->
On **CE_2**, run:

```saos
ping ip destination 172.16.106.3 source 172.16.106.2 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.106.3, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 6.15 ms  TTL = 255
! seq_num = 2  RTT = 6.87 ms  TTL = 255
! seq_num = 3  RTT = 5.36 ms  TTL = 255
! seq_num = 4  RTT = 7.52 ms  TTL = 255
! seq_num = 5  RTT = 6.44 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 5.36/6.47/7.52
```

</details>

<!-- retry: 60s -->
On **CE_3**, run:

```saos
ping ip destination 172.16.106.1 source 172.16.106.3 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.106.1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 6.98 ms  TTL = 255
! seq_num = 2  RTT = 6.00 ms  TTL = 255
! seq_num = 3  RTT = 6.36 ms  TTL = 255
! seq_num = 4  RTT = 4.74 ms  TTL = 255
! seq_num = 5  RTT = 6.32 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 4.74/6.08/6.98
```

</details>

<!-- retry: 60s -->
On **PE_1**, run:

```saos
show evpn instances vpls forwarding-database
```

Pass: Output contains `elan_1-fd` and `172.16.0.2` and `172.16.0.5`

<details><summary>Example output</summary>

```
+--------------------------------------------------+
| Codes: > - installed FTN,                        |
|        L - local, R - remote,                    |
|        C - control-word, P - primary, B - backup |
+--------------------------------------------------+
+-------------------------------------------------------- EVPN VPLS FORWARDING DATABASE ---------------------------------------------------------+
| State | EVPN ID | Forwarding Domain | MAC            | IP | Next Hop   |  Ethernet Segment Identifier  | Out Label | SRv6 Service SID | Flags  |
+-------+---------+-------------------+----------------+----+------------+-------------------------------+-----------+------------------+--------+
|   >   |   103   | elan_1-fd         | 0c00:4fd6:fbf5 | -  | 172.16.0.2 | 00:00:00:00:00:00:00:00:00:00 | 132000    | -                | (R)(C) |
|       |   103   | elan_1-fd         | 0c00:d033:10f5 | -  | 0.0.0.0    | 00:00:00:00:00:00:00:00:00:00 | 132000    | -                | (L)(C) |
|   >   |   103   | elan_1-fd         | 0c00:d8b5:43f5 | -  | 172.16.0.5 | 00:00:00:00:00:00:00:00:00:00 | 132000    | -                | (R)(C) |
+-------+---------+-------------------+----------------+----+------------+-------------------------------+-----------+------------------+--------+
```

</details>
