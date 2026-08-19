Deploy `F3-SR-MPLS`, then run the following validation checks.

## G1: Task 1 — Verify the deployed topology

<!-- retry: 120s -->
On **PE_1**, run:

```saos
ping ip destination FC00::2 source FC00::1 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to FC00::2, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 5.00 ms  TTL = 255
! seq_num = 2  RTT = 2.87 ms  TTL = 255
! seq_num = 3  RTT = 2.73 ms  TTL = 255
! seq_num = 4  RTT = 3.12 ms  TTL = 255
! seq_num = 5  RTT = 2.78 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 2.73/3.30/5.00
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
ping ip destination FC00::1 source FC00::2 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to FC00::1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.49 ms  TTL = 255
! seq_num = 2  RTT = 3.66 ms  TTL = 255
! seq_num = 3  RTT = 3.91 ms  TTL = 255
! seq_num = 4  RTT = 3.99 ms  TTL = 255
! seq_num = 5  RTT = 3.20 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 2.49/3.45/3.99
```

</details>

## G2: Task 2 — Configure SR-MPLS on PE_1

<!-- retry: 60s -->
On **PE_1**, run:

```saos
show isis segment-routing
```

Pass: Output contains `Bootcamp` and `Enabled`

<details><summary>Example output</summary>

```
+----------- ISIS SEGMENT-ROUTING STATE -----------+
| ISIS Tag | Config State | Oper State | Force PHP |
+----------+--------------+------------+-----------+
| Bootcamp | Enabled      | Enabled    | Disabled  |
+----------+--------------+------------+-----------+
```

</details>

On **PE_1**, run:

```saos
show segment-routing connected-prefix-sid-map
```

Pass: Output contains `172.16.0.1/32` and `lb1`

<details><summary>Example output</summary>

```
+----- SEGMENT-ROUTING SID MAP -----+
|  Name             |  Value        |
+-------------------+---------------+
| Prefix            | 172.16.0.1/32 |
| Interface         | lb1           |
| Value Type        | Index         |
| Start SID         | 1             |
| Range             | 1             |
| Algorithm         | SPF           |
| Last Hop Behavior | -             |
+-------------------+---------------+
```

</details>

## G3: Task 3 — Configure SR-MPLS on PE_2

<!-- retry: 60s -->
On **PE_2**, run:

```saos
show isis segment-routing
```

Pass: Output contains `Bootcamp` and `Enabled`

<details><summary>Example output</summary>

```
+----------- ISIS SEGMENT-ROUTING STATE -----------+
| ISIS Tag | Config State | Oper State | Force PHP |
+----------+--------------+------------+-----------+
| Bootcamp | Enabled      | Enabled    | Disabled  |
+----------+--------------+------------+-----------+
```

</details>

On **PE_2**, run:

```saos
show segment-routing connected-prefix-sid-map
```

Pass: Output contains `172.16.0.2/32` and `lb1`

<details><summary>Example output</summary>

```
+----- SEGMENT-ROUTING SID MAP -----+
|  Name             |  Value        |
+-------------------+---------------+
| Prefix            | 172.16.0.2/32 |
| Interface         | lb1           |
| Value Type        | Index         |
| Start SID         | 2             |
| Range             | 1             |
| Algorithm         | SPF           |
| Last Hop Behavior | -             |
+-------------------+---------------+
```

</details>

## G4: Task 4 — Verify the primary transport

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show isis segment-routing capability
```

Pass: Output contains `16000` and `23999` and `172.16.0.1` and `172.16.0.2`

<details><summary>Example output</summary>

```
+------------------------------- ISIS SEGMENT-ROUTING CAPABILITY --------------------------------+
|          |            |       |       |    Total  | SID Range  |            |           |      |
|          |            | SRGB  | SRGB  |      SID  |      List  |      SRMS  |           | Node |
| Instance |  Router ID | Start |   End | Supported |      Count | Preference | Algorithm | MSD  |
+----------+------------+-------+-------+-----------+------------+------------+-----------+------+
| Bootcamp | 172.16.0.1 | 16000 | 23999 |      8000 |          1 |        128 |       SPF | 0    |
+----------+------------+-------+-------+-----------+------------+------------+-----------+------+
| Bootcamp | 172.16.0.2 | 16000 | 23999 |      8000 |          1 |        128 |       SPF | 0    |
+----------+------------+-------+-------+-----------+------------+------------+-----------+------+
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
show isis segment-routing capability
```

Pass: Output contains `16000` and `23999` and `172.16.0.1` and `172.16.0.2`

<details><summary>Example output</summary>

```
+------------------------------- ISIS SEGMENT-ROUTING CAPABILITY --------------------------------+
|          |            |       |       |    Total  | SID Range  |            |           |      |
|          |            | SRGB  | SRGB  |      SID  |      List  |      SRMS  |           | Node |
| Instance |  Router ID | Start |   End | Supported |      Count | Preference | Algorithm | MSD  |
+----------+------------+-------+-------+-----------+------------+------------+-----------+------+
| Bootcamp | 172.16.0.1 | 16000 | 23999 |      8000 |          1 |        128 |       SPF | 0    |
+----------+------------+-------+-------+-----------+------------+------------+-----------+------+
| Bootcamp | 172.16.0.2 | 16000 | 23999 |      8000 |          1 |        128 |       SPF | 0    |
+----------+------------+-------+-------+-----------+------------+------------+-----------+------+
```

</details>

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show isis segment-routing mapping-table status active
```

Pass: Output contains `172.16.0.1/32` and `172.16.0.2/32`

<details><summary>Example output</summary>

```
+---------- ISIS SEGMENT-ROUTING MAPPING TABLE ACTIVE -----------+
| ISIS Instance |  Entry Prefix | SID Index | Range | Preference |
+---------------+---------------+-----------+-------+------------+
|    Bootcamp   | 172.16.0.1/32 |         1 |     1 |        192 |
|    Bootcamp   | 172.16.0.2/32 |         2 |     1 |        192 |
+---------------+---------------+-----------+-------+------------+
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
show isis segment-routing mapping-table status active
```

Pass: Output contains `172.16.0.1/32` and `172.16.0.2/32`

<details><summary>Example output</summary>

```
+---------- ISIS SEGMENT-ROUTING MAPPING TABLE ACTIVE -----------+
| ISIS Instance |  Entry Prefix | SID Index | Range | Preference |
+---------------+---------------+-----------+-------+------------+
|    Bootcamp   | 172.16.0.1/32 |         1 |     1 |        192 |
|    Bootcamp   | 172.16.0.2/32 |         2 |     1 |        192 |
+---------------+---------------+-----------+-------+------------+
```

</details>

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show mpls forwarding-table
```

Pass: Output contains `172.16.0.2/32` and `i >`

<details><summary>Example output</summary>

```
+--------------------------------------------------------------------------------------------------------------------+
| Codes: > - installed FTN, * - selected FTN, p - stale FTN, b - backup route                                        |
|        B - BGP FTN, K - CLI FTN, t - tunnel                                                                        |
|        L - LDP FTN, R - RSVP-TE FTN, S - SNMP FTN, I - IGP-Shortcut,                                               |
|        U - unknown FTN, O - SR-OSPF FTN, i - SR-ISIS FTN, k - SR-CLI FTN,                                          |
|        s - SR-TE FTN,  ip - IP-ISIS FTN, io - IP-OSPF FTN, ib - IP-BGP FTN,                                        |
|        M - MPLS-TP FTN, ias - IAS FTN, v - VPN FTN,                                                                |
|        m - PW-MPLS FTN, e - EVPN FTN                                                                               |
|        C - Color, Tn - Tunnel Name, f - Fallback, ML - Multicast LDP, IR - Ingress-Replication, F - Flex-Algorithm |
+--------------------------------------------------------------------------------------------------------------------+
+-------------------------------------- MPLS FORWARDING TABLE --------------------------------------+
|      |                    | Opaque |          Label          |                  |                 |
| Code |        FEC         |  ID    |     In     |    Out     |     Out Intf     |     Next Hop    |
+------+--------------------+--------+------------+------------+------------------+-----------------+
| i >  | 172.16.0.2/32      | 7      | -          | 3          | PE_1-PE_2-if     | 172.16.1.2      |
+------+--------------------+--------+------------+------------+------------------+-----------------+
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
show mpls forwarding-table
```

Pass: Output contains `172.16.0.1/32` and `i >`

<details><summary>Example output</summary>

```
+--------------------------------------------------------------------------------------------------------------------+
| Codes: > - installed FTN, * - selected FTN, p - stale FTN, b - backup route                                        |
|        B - BGP FTN, K - CLI FTN, t - tunnel                                                                        |
|        L - LDP FTN, R - RSVP-TE FTN, S - SNMP FTN, I - IGP-Shortcut,                                               |
|        U - unknown FTN, O - SR-OSPF FTN, i - SR-ISIS FTN, k - SR-CLI FTN,                                          |
|        s - SR-TE FTN,  ip - IP-ISIS FTN, io - IP-OSPF FTN, ib - IP-BGP FTN,                                        |
|        M - MPLS-TP FTN, ias - IAS FTN, v - VPN FTN,                                                                |
|        m - PW-MPLS FTN, e - EVPN FTN                                                                               |
|        C - Color, Tn - Tunnel Name, f - Fallback, ML - Multicast LDP, IR - Ingress-Replication, F - Flex-Algorithm |
+--------------------------------------------------------------------------------------------------------------------+
+-------------------------------------- MPLS FORWARDING TABLE --------------------------------------+
|      |                    | Opaque |          Label          |                  |                 |
| Code |        FEC         |  ID    |     In     |    Out     |     Out Intf     |     Next Hop    |
+------+--------------------+--------+------------+------------+------------------+-----------------+
| i >  | 172.16.0.1/32      | 8      | -          | 3          | PE_1-PE_2-if     | 172.16.1.1      |
+------+--------------------+--------+------------+------------+------------------+-----------------+
```

</details>

<!-- retry: 120s -->
On **PE_1**, run:

```saos
ping ip destination 172.16.0.2 source 172.16.0.1 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.0.2, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.84 ms  TTL = 255
! seq_num = 2  RTT = 3.69 ms  TTL = 255
! seq_num = 3  RTT = 3.03 ms  TTL = 255
! seq_num = 4  RTT = 3.16 ms  TTL = 255
! seq_num = 5  RTT = 3.61 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 2.84/3.27/3.69
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
ping ip destination 172.16.0.1 source 172.16.0.2 repeat-count 5
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 5 ICMP Echos to 172.16.0.1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.96 ms  TTL = 255
! seq_num = 2  RTT = 2.94 ms  TTL = 255
! seq_num = 3  RTT = 2.79 ms  TTL = 255
! seq_num = 4  RTT = 3.10 ms  TTL = 255
! seq_num = 5  RTT = 3.57 ms  TTL = 255
Success Rate is 100.00 percent (5/5)
Round-trip min/avg/max = 2.79/3.07/3.57
```

</details>
