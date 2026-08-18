Deploy `F2-IS-IS-Routing`, then run the following validation checks.

## G1: Task 2 — Create an IS-IS instance on PE_1 and add interfaces to it

On **PE_1**, run:

```saos
show isis summary
```

Pass: Output contains `Bootcamp` and `level-1` and `0172.0016.0001` and `49.0001`

<details><summary>Example output</summary>

```
+------------------------ ISIS SUMMARY -----------------------+
| Name                                      |           Value |
+-------------------------------------------+-----------------+
| Instance                                  |        Bootcamp |
| Level Type                                |         level-1 |
| System ID                                 |  0172.0016.0001 |
| Area Ids                                  |         49.0001 |
| Topology Type                             | Single-Topology |
| Dynamic Hostname                          |           False |
| Transition                                |           False |
| Level 1                                   |                 |
|   Authentication                          |        Disabled |
|   Authentication Type                     |               - |
|   Authentication Send Only                |           False |
|   Level Restarting                        |           False |
|   Configured T2 Restart Timer (Seconds)   |              60 |
|   Remaining T2 Restart Timer (Seconds)    |               0 |
|   Minimum LSP Generation Interval (ms)    |             100 |
|   Maximum LSP Generation Interval (ms)    |           10000 |
| Level 2                                   |                 |
|   Authentication                          |        Disabled |
|   Authentication Type                     |               - |
|   Authentication Send Only                |           False |
|   Level Restarting                        |           False |
|   Configured T2 Restart Timer (Seconds)   |              60 |
|   Remaining T2 Restart Timer (Seconds)    |               0 |
|   Minimum LSP Generation Interval (ms)    |             100 |
|   Maximum LSP Generation Interval (ms)    |           10000 |
| MPLS-TE                                   |  Not Configured |
| Segment Routing                           |        Disabled |
| Microloop Avoidance                       |        Disabled |
| Graceful Restart                          |        Disabled |
| Graceful Restart Helper                   |         Enabled |
| Node Restarting                           |           False |
| Configured T3 Grace Period (Seconds)      |           65535 |
| Remaining T3 Grace Period (Seconds)       |               0 |
| Interfaces                                |                 |
|                                           |                 |
|   Interface Name                          |    PE_1-PE_2-if |
|     Interface Type                        |  point-to-point |
|     Level Type                            |         level-1 |
|     Passive Interface                     |           False |
|     IPv4 Unicast                          |            True |
|     IPv6 Unicast                          |            True |
|     Level 1                               |                 |
|       Authentication                      |         Enabled |
|       Authentication Type                 |        HMAC-MD5 |
|       Authentication Send Only            |           False |
|       Metric                              |              10 |
|       Wide Metric                         |              10 |
|       Admin Tag                           |               - |
|       T1 Restart Hello Interval (Seconds) |               3 |
|       Restart Request (RR) Sent           |               0 |
|       Restart Acknowledge (RA) Received   |               0 |
|       Restart Request (RR) Received       |               0 |
|       Restart Acknowledge (RA) Sent       |               0 |
|     Level 2                               |                 |
|       Authentication                      |         Enabled |
|       Authentication Type                 |        HMAC-MD5 |
|       Authentication Send Only            |           False |
|       Metric                              |              10 |
|       Wide Metric                         |              10 |
|       Admin Tag                           |               - |
|       T1 Restart Hello Interval (Seconds) |               3 |
|       Restart Request (RR) Sent           |               0 |
|       Restart Acknowledge (RA) Received   |               0 |
|       Restart Request (RR) Received       |               0 |
|       Restart Acknowledge (RA) Sent       |               0 |
|                                           |                 |
|   Interface Name                          |             lb1 |
|     Interface Type                        |  point-to-point |
|     Level Type                            |       level-1-2 |
|     Passive Interface                     |           False |
|     IPv4 Unicast                          |            True |
|     IPv6 Unicast                          |            True |
|     Level 1                               |                 |
|       Authentication                      |        Disabled |
|       Authentication Type                 |               - |
|       Authentication Send Only            |           False |
|       Metric                              |              10 |
|       Wide Metric                         |              10 |
|       Admin Tag                           |               - |
|       T1 Restart Hello Interval (Seconds) |               3 |
|       Restart Request (RR) Sent           |               0 |
|       Restart Acknowledge (RA) Received   |               0 |
|       Restart Request (RR) Received       |               0 |
|       Restart Acknowledge (RA) Sent       |               0 |
|     Level 2                               |                 |
|       Authentication                      |        Disabled |
|       Authentication Type                 |               - |
|       Authentication Send Only            |           False |
|       Metric                              |              10 |
|       Wide Metric                         |              10 |
|       Admin Tag                           |               - |
|       T1 Restart Hello Interval (Seconds) |               3 |
|       Restart Request (RR) Sent           |               0 |
|       Restart Acknowledge (RA) Received   |               0 |
|       Restart Request (RR) Received       |               0 |
|       Restart Acknowledge (RA) Sent       |               0 |
+-------------------------------------------+-----------------+
```

</details>

## G2: Task 3 — Create an IS-IS instance on PE_2 and add interfaces to it

On **PE_2**, run:

```saos
show isis summary
```

Pass: Output contains `Bootcamp` and `level-1` and `0172.0016.0002` and `49.0001`

<details><summary>Example output</summary>

```
+------------------------ ISIS SUMMARY -----------------------+
| Name                                      |           Value |
+-------------------------------------------+-----------------+
| Instance                                  |        Bootcamp |
| Level Type                                |         level-1 |
| System ID                                 |  0172.0016.0002 |
| Area Ids                                  |         49.0001 |
| Topology Type                             | Single-Topology |
| Dynamic Hostname                          |           False |
| Transition                                |           False |
| Level 1                                   |                 |
|   Authentication                          |        Disabled |
|   Authentication Type                     |               - |
|   Authentication Send Only                |           False |
|   Level Restarting                        |           False |
|   Configured T2 Restart Timer (Seconds)   |              60 |
|   Remaining T2 Restart Timer (Seconds)    |               0 |
|   Minimum LSP Generation Interval (ms)    |             100 |
|   Maximum LSP Generation Interval (ms)    |           10000 |
| Level 2                                   |                 |
|   Authentication                          |        Disabled |
|   Authentication Type                     |               - |
|   Authentication Send Only                |           False |
|   Level Restarting                        |           False |
|   Configured T2 Restart Timer (Seconds)   |              60 |
|   Remaining T2 Restart Timer (Seconds)    |               0 |
|   Minimum LSP Generation Interval (ms)    |             100 |
|   Maximum LSP Generation Interval (ms)    |           10000 |
| MPLS-TE                                   |  Not Configured |
| Segment Routing                           |        Disabled |
| Microloop Avoidance                       |        Disabled |
| Graceful Restart                          |        Disabled |
| Graceful Restart Helper                   |         Enabled |
| Node Restarting                           |           False |
| Configured T3 Grace Period (Seconds)      |           65535 |
| Remaining T3 Grace Period (Seconds)       |               0 |
| Interfaces                                |                 |
|                                           |                 |
|   Interface Name                          |    PE_1-PE_2-if |
|     Interface Type                        |  point-to-point |
|     Level Type                            |         level-1 |
|     Passive Interface                     |           False |
|     IPv4 Unicast                          |            True |
|     IPv6 Unicast                          |            True |
|     Level 1                               |                 |
|       Authentication                      |         Enabled |
|       Authentication Type                 |        HMAC-MD5 |
|       Authentication Send Only            |           False |
|       Metric                              |              10 |
|       Wide Metric                         |              10 |
|       Admin Tag                           |               - |
|       T1 Restart Hello Interval (Seconds) |               3 |
|       Restart Request (RR) Sent           |               0 |
|       Restart Acknowledge (RA) Received   |               0 |
|       Restart Request (RR) Received       |               0 |
|       Restart Acknowledge (RA) Sent       |               0 |
|     Level 2                               |                 |
|       Authentication                      |         Enabled |
|       Authentication Type                 |        HMAC-MD5 |
|       Authentication Send Only            |           False |
|       Metric                              |              10 |
|       Wide Metric                         |              10 |
|       Admin Tag                           |               - |
|       T1 Restart Hello Interval (Seconds) |               3 |
|       Restart Request (RR) Sent           |               0 |
|       Restart Acknowledge (RA) Received   |               0 |
|       Restart Request (RR) Received       |               0 |
|       Restart Acknowledge (RA) Sent       |               0 |
|                                           |                 |
|   Interface Name                          |             lb1 |
|     Interface Type                        |  point-to-point |
|     Level Type                            |       level-1-2 |
|     Passive Interface                     |           False |
|     IPv4 Unicast                          |            True |
|     IPv6 Unicast                          |            True |
|     Level 1                               |                 |
|       Authentication                      |        Disabled |
|       Authentication Type                 |               - |
|       Authentication Send Only            |           False |
|       Metric                              |              10 |
|       Wide Metric                         |              10 |
|       Admin Tag                           |               - |
|       T1 Restart Hello Interval (Seconds) |               3 |
|       Restart Request (RR) Sent           |               0 |
|       Restart Acknowledge (RA) Received   |               0 |
|       Restart Request (RR) Received       |               0 |
|       Restart Acknowledge (RA) Sent       |               0 |
|     Level 2                               |                 |
|       Authentication                      |        Disabled |
|       Authentication Type                 |               - |
|       Authentication Send Only            |           False |
|       Metric                              |              10 |
|       Wide Metric                         |              10 |
|       Admin Tag                           |               - |
|       T1 Restart Hello Interval (Seconds) |               3 |
|       Restart Request (RR) Sent           |               0 |
|       Restart Acknowledge (RA) Received   |               0 |
|       Restart Request (RR) Received       |               0 |
|       Restart Acknowledge (RA) Sent       |               0 |
+-------------------------------------------+-----------------+
```

</details>

<!-- retry: 90s -->
On **PE_1**, run:

```saos
show isis neighbors
```

Pass: Output contains `0172.0016.0002` and `PE_1-PE_2-if` and `Up`

<details><summary>Example output</summary>

```
+-------------------------------------- ISIS NEIGHBOR STATE: Bootcamp ---------------------------------------+
| Neighbor |                        |                  |                |       |   Hold   |      |          |
|   Type   |       System ID        |    Interface     |      SNPA      | State | Time (s) | Type | Protocol |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
|   P2P    |     0172.0016.0002     |   PE_1-PE_2-if   | 0c00.e1d6.83f6 |    Up |       23 |  L1  |  IS-IS   |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
show isis neighbors
```

Pass: Output contains `0172.0016.0001` and `PE_1-PE_2-if` and `Up`

<details><summary>Example output</summary>

```
+-------------------------------------- ISIS NEIGHBOR STATE: Bootcamp ---------------------------------------+
| Neighbor |                        |                  |                |       |   Hold   |      |          |
|   Type   |       System ID        |    Interface     |      SNPA      | State | Time (s) | Type | Protocol |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
|   P2P    |     0172.0016.0001     |   PE_1-PE_2-if   | 0c00.2f0f.4af6 |    Up |       22 |  L1  |  IS-IS   |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
```

</details>

<!-- retry: 90s -->
On **PE_1**, run:

```saos
show ip routes
```

Pass: Output contains `172.16.0.2/32` and `172.16.1.2`

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
| *>    |  I   |  L1 | Bootcamp         | 172.16.0.2/32      | [115/20]  | 172.16.1.2      | PE_1-PE_2-if              | -               | -                         | 00:00:56    |
| *>    |  C   |  -  | -                | 172.16.1.0/30      | [0/0]     | -               | PE_1-PE_2-if              | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 90s -->
On **PE_1**, run:

```saos
ping ip destination 172.16.0.2 source 172.16.0.1 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to 172.16.0.2, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.58 ms  TTL = 255
! seq_num = 2  RTT = 1.73 ms  TTL = 255
! seq_num = 3  RTT = 2.33 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 1.73/2.21/2.58
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
show ip routes
```

Pass: Output contains `172.16.0.1/32` and `172.16.1.1`

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
| *>    |  I   |  L1 | Bootcamp         | 172.16.0.1/32      | [115/20]  | 172.16.1.1      | PE_1-PE_2-if              | -               | -                         | 00:00:40    |
| *>    |  C   |  -  | -                | 172.16.0.2/32      | [0/0]     | -               | lb1                       | -               | -                         | -           |
| *>    |  C   |  -  | -                | 172.16.1.0/30      | [0/0]     | -               | PE_1-PE_2-if              | -               | -                         | -           |
+-------+------+-----+------------------+--------------------+-----------+-----------------+---------------------------+-----------------+---------------------------+-------------+
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
ping ip destination 172.16.0.1 source 172.16.0.2 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to 172.16.0.1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 3.31 ms  TTL = 255
! seq_num = 2  RTT = 1.93 ms  TTL = 255
! seq_num = 3  RTT = 2.03 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 1.93/2.42/3.31
```

</details>

## G3: Task 6 — Add the ipv6 address-family to the IS-IS interfaces

On **PE_1**, run:

```saos
show isis interfaces
```

Pass: Output contains `PE_1-PE_2-if` and `lb1` and `IPv6`

<details><summary>Example output</summary>

```
+------------------------ ISIS INTERFACE STATE -----------------------+
| Name                             |                            Value |
+----------------------------------+----------------------------------+
| Interface                        |                     PE_1-PE_2-if |
| Routing Protocol                 |                  ISIS (Bootcamp) |
| Network Type                     |                   Point-to-Point |
| Circuit Type                     |                          level-1 |
| Local Circuit ID                 |                               02 |
| Extended Local Circuit ID        |                         3FFFD8F2 |
| Local SNPA                       |                                - |
| Hello Padding                    |                             True |
| LDP IGP SYNC Status              |                   Not Configured |
| IP Interface Address(es)         |                    172.16.1.1/30 |
| IPv6 Interface Address(es)       |                    fc00::600/127 |
|                                  |      fe80::e00:2fff:fe0f:4af6/64 |
| Level Index                      |                          level-1 |
|    Circuit ID                    |                0172.0016.0001.02 |
|    Active Adjacencies            |                                1 |
|    LSP MTU                       |                             1492 |
|    Metric (Narrow/Wide)          |                            10/10 |
|    Admin Tag                     |                                - |
|    Protocol Oper State           |                               up |
|    Next Hello                    |                        5 seconds |
|    Hello Interval                |                       10 seconds |
|    Hello Multiplier              |                                3 |
|    Authentication                |                              MD5 |
|   Password                       |                             **** |
| BFD                              |                         Disabled |
| BFD IPv6                         |                         Disabled |
+----------------------------------+----------------------------------+
| Interface                        |                              lb1 |
| Routing Protocol                 |                  ISIS (Bootcamp) |
| Network Type                     |                   Point-to-Point |
| Circuit Type                     |                        level-1-2 |
| Local Circuit ID                 |                               01 |
| Extended Local Circuit ID        |                         3FFFE8F5 |
| Local SNPA                       |                                - |
| Hello Padding                    |                             True |
| LDP IGP SYNC Status              |                   Not Configured |
| IP Interface Address(es)         |                    172.16.0.1/32 |
| IPv6 Interface Address(es)       |                      fc00::1/128 |
|                                  |      fe80::e00:2fff:fe0f:4af6/64 |
| Level Index                      |                          level-1 |
|    Circuit ID                    |                0172.0016.0001.01 |
|    Active Adjacencies            |                                0 |
|    LSP MTU                       |                             1492 |
|    Metric (Narrow/Wide)          |                            10/10 |
|    Admin Tag                     |                                - |
|    Protocol Oper State           |                               up |
|    Next Hello                    |                        0 seconds |
|    Hello Interval                |                       10 seconds |
|    Hello Multiplier              |                                3 |
|    Authentication                |                          Not Set |
| BFD                              |                         Disabled |
| BFD IPv6                         |                         Disabled |
+----------------------------------+----------------------------------+
```

</details>

On **PE_2**, run:

```saos
show isis interfaces
```

Pass: Output contains `PE_1-PE_2-if` and `lb1` and `IPv6`

<details><summary>Example output</summary>

```
+------------------------ ISIS INTERFACE STATE -----------------------+
| Name                             |                            Value |
+----------------------------------+----------------------------------+
| Interface                        |                     PE_1-PE_2-if |
| Routing Protocol                 |                  ISIS (Bootcamp) |
| Network Type                     |                   Point-to-Point |
| Circuit Type                     |                          level-1 |
| Local Circuit ID                 |                               02 |
| Extended Local Circuit ID        |                         3FFFD8F2 |
| Local SNPA                       |                                - |
| Hello Padding                    |                             True |
| LDP IGP SYNC Status              |                   Not Configured |
| IP Interface Address(es)         |                    172.16.1.2/30 |
| IPv6 Interface Address(es)       |                    fc00::601/127 |
|                                  |      fe80::e00:e1ff:fed6:83f6/64 |
| Level Index                      |                          level-1 |
|    Circuit ID                    |                0172.0016.0002.02 |
|    Active Adjacencies            |                                1 |
|    LSP MTU                       |                             1492 |
|    Metric (Narrow/Wide)          |                            10/10 |
|    Admin Tag                     |                                - |
|    Protocol Oper State           |                               up |
|    Next Hello                    |                        6 seconds |
|    Hello Interval                |                       10 seconds |
|    Hello Multiplier              |                                3 |
|    Authentication                |                              MD5 |
|   Password                       |                             **** |
| BFD                              |                         Disabled |
| BFD IPv6                         |                         Disabled |
+----------------------------------+----------------------------------+
| Interface                        |                              lb1 |
| Routing Protocol                 |                  ISIS (Bootcamp) |
| Network Type                     |                   Point-to-Point |
| Circuit Type                     |                        level-1-2 |
| Local Circuit ID                 |                               01 |
| Extended Local Circuit ID        |                         3FFFE8F5 |
| Local SNPA                       |                                - |
| Hello Padding                    |                             True |
| LDP IGP SYNC Status              |                   Not Configured |
| IP Interface Address(es)         |                    172.16.0.2/32 |
| IPv6 Interface Address(es)       |                      fc00::2/128 |
|                                  |      fe80::e00:e1ff:fed6:83f6/64 |
| Level Index                      |                          level-1 |
|    Circuit ID                    |                0172.0016.0002.01 |
|    Active Adjacencies            |                                0 |
|    LSP MTU                       |                             1492 |
|    Metric (Narrow/Wide)          |                            10/10 |
|    Admin Tag                     |                                - |
|    Protocol Oper State           |                               up |
|    Next Hello                    |                        0 seconds |
|    Hello Interval                |                       10 seconds |
|    Hello Multiplier              |                                3 |
|    Authentication                |                          Not Set |
| BFD                              |                         Disabled |
| BFD IPv6                         |                         Disabled |
+----------------------------------+----------------------------------+
```

</details>

<!-- retry: 90s -->
On **PE_1**, run:

```saos
ping ip destination FC00::2 source FC00::1 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to FC00::2, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 1.87 ms  TTL = 255
! seq_num = 2  RTT = 1.82 ms  TTL = 255
! seq_num = 3  RTT = 2.05 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 1.82/1.91/2.05
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
ping ip destination FC00::1 source FC00::2 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to FC00::1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 1.61 ms  TTL = 255
! seq_num = 2  RTT = 2.37 ms  TTL = 255
! seq_num = 3  RTT = 1.74 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 1.61/1.91/2.37
```

</details>

## G4: Task 8 — Add MD5 authentication to the IS-IS neighbor association

<!-- retry: 90s -->
On **PE_1**, run:

```saos
show isis interfaces
```

Pass: Output contains `PE_1-PE_2-if` and `level-1` and `MD5`

<details><summary>Example output</summary>

```
+------------------------ ISIS INTERFACE STATE -----------------------+
| Name                             |                            Value |
+----------------------------------+----------------------------------+
| Interface                        |                     PE_1-PE_2-if |
| Routing Protocol                 |                  ISIS (Bootcamp) |
| Network Type                     |                   Point-to-Point |
| Circuit Type                     |                          level-1 |
| Local Circuit ID                 |                               02 |
| Extended Local Circuit ID        |                         3FFFD8F2 |
| Local SNPA                       |                                - |
| Hello Padding                    |                             True |
| LDP IGP SYNC Status              |                   Not Configured |
| IP Interface Address(es)         |                    172.16.1.1/30 |
| IPv6 Interface Address(es)       |                    fc00::600/127 |
|                                  |      fe80::e00:2fff:fe0f:4af6/64 |
| Level Index                      |                          level-1 |
|    Circuit ID                    |                0172.0016.0001.02 |
|    Active Adjacencies            |                                1 |
|    LSP MTU                       |                             1492 |
|    Metric (Narrow/Wide)          |                            10/10 |
|    Admin Tag                     |                                - |
|    Protocol Oper State           |                               up |
|    Next Hello                    |                        8 seconds |
|    Hello Interval                |                       10 seconds |
|    Hello Multiplier              |                                3 |
|    Authentication                |                              MD5 |
|   Password                       |                             **** |
| BFD                              |                         Disabled |
| BFD IPv6                         |                         Disabled |
+----------------------------------+----------------------------------+
| Interface                        |                              lb1 |
| Routing Protocol                 |                  ISIS (Bootcamp) |
| Network Type                     |                   Point-to-Point |
| Circuit Type                     |                        level-1-2 |
| Local Circuit ID                 |                               01 |
| Extended Local Circuit ID        |                         3FFFE8F5 |
| Local SNPA                       |                                - |
| Hello Padding                    |                             True |
| LDP IGP SYNC Status              |                   Not Configured |
| IP Interface Address(es)         |                    172.16.0.1/32 |
| IPv6 Interface Address(es)       |                      fc00::1/128 |
|                                  |      fe80::e00:2fff:fe0f:4af6/64 |
| Level Index                      |                          level-1 |
|    Circuit ID                    |                0172.0016.0001.01 |
|    Active Adjacencies            |                                0 |
|    LSP MTU                       |                             1492 |
|    Metric (Narrow/Wide)          |                            10/10 |
|    Admin Tag                     |                                - |
|    Protocol Oper State           |                               up |
|    Next Hello                    |                        0 seconds |
|    Hello Interval                |                       10 seconds |
|    Hello Multiplier              |                                3 |
|    Authentication                |                          Not Set |
| BFD                              |                         Disabled |
| BFD IPv6                         |                         Disabled |
+----------------------------------+----------------------------------+
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
show isis interfaces
```

Pass: Output contains `PE_1-PE_2-if` and `level-1` and `MD5`

<details><summary>Example output</summary>

```
+------------------------ ISIS INTERFACE STATE -----------------------+
| Name                             |                            Value |
+----------------------------------+----------------------------------+
| Interface                        |                     PE_1-PE_2-if |
| Routing Protocol                 |                  ISIS (Bootcamp) |
| Network Type                     |                   Point-to-Point |
| Circuit Type                     |                          level-1 |
| Local Circuit ID                 |                               02 |
| Extended Local Circuit ID        |                         3FFFD8F2 |
| Local SNPA                       |                                - |
| Hello Padding                    |                             True |
| LDP IGP SYNC Status              |                   Not Configured |
| IP Interface Address(es)         |                    172.16.1.2/30 |
| IPv6 Interface Address(es)       |                    fc00::601/127 |
|                                  |      fe80::e00:e1ff:fed6:83f6/64 |
| Level Index                      |                          level-1 |
|    Circuit ID                    |                0172.0016.0002.02 |
|    Active Adjacencies            |                                1 |
|    LSP MTU                       |                             1492 |
|    Metric (Narrow/Wide)          |                            10/10 |
|    Admin Tag                     |                                - |
|    Protocol Oper State           |                               up |
|    Next Hello                    |                        9 seconds |
|    Hello Interval                |                       10 seconds |
|    Hello Multiplier              |                                3 |
|    Authentication                |                              MD5 |
|   Password                       |                             **** |
| BFD                              |                         Disabled |
| BFD IPv6                         |                         Disabled |
+----------------------------------+----------------------------------+
| Interface                        |                              lb1 |
| Routing Protocol                 |                  ISIS (Bootcamp) |
| Network Type                     |                   Point-to-Point |
| Circuit Type                     |                        level-1-2 |
| Local Circuit ID                 |                               01 |
| Extended Local Circuit ID        |                         3FFFE8F5 |
| Local SNPA                       |                                - |
| Hello Padding                    |                             True |
| LDP IGP SYNC Status              |                   Not Configured |
| IP Interface Address(es)         |                    172.16.0.2/32 |
| IPv6 Interface Address(es)       |                      fc00::2/128 |
|                                  |      fe80::e00:e1ff:fed6:83f6/64 |
| Level Index                      |                          level-1 |
|    Circuit ID                    |                0172.0016.0002.01 |
|    Active Adjacencies            |                                0 |
|    LSP MTU                       |                             1492 |
|    Metric (Narrow/Wide)          |                            10/10 |
|    Admin Tag                     |                                - |
|    Protocol Oper State           |                               up |
|    Next Hello                    |                        0 seconds |
|    Hello Interval                |                       10 seconds |
|    Hello Multiplier              |                                3 |
|    Authentication                |                          Not Set |
| BFD                              |                         Disabled |
| BFD IPv6                         |                         Disabled |
+----------------------------------+----------------------------------+
```

</details>

<!-- retry: 90s -->
On **PE_1**, run:

```saos
show isis neighbors
```

Pass: Output contains `0172.0016.0002` and `Up`

<details><summary>Example output</summary>

```
+-------------------------------------- ISIS NEIGHBOR STATE: Bootcamp ---------------------------------------+
| Neighbor |                        |                  |                |       |   Hold   |      |          |
|   Type   |       System ID        |    Interface     |      SNPA      | State | Time (s) | Type | Protocol |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
|   P2P    |     0172.0016.0002     |   PE_1-PE_2-if   | 0c00.e1d6.83f6 |    Up |       29 |  L1  |  IS-IS   |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
show isis neighbors
```

Pass: Output contains `0172.0016.0001` and `Up`

<details><summary>Example output</summary>

```
+-------------------------------------- ISIS NEIGHBOR STATE: Bootcamp ---------------------------------------+
| Neighbor |                        |                  |                |       |   Hold   |      |          |
|   Type   |       System ID        |    Interface     |      SNPA      | State | Time (s) | Type | Protocol |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
|   P2P    |     0172.0016.0001     |   PE_1-PE_2-if   | 0c00.2f0f.4af6 |    Up |       27 |  L1  |  IS-IS   |
+----------+------------------------+------------------+----------------+-------+----------+------+----------+
```

</details>

<!-- retry: 90s -->
On **PE_1**, run:

```saos
ping ip destination FC00::2 source FC00::1 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to FC00::2, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 1.92 ms  TTL = 255
! seq_num = 2  RTT = 2.87 ms  TTL = 255
! seq_num = 3  RTT = 2.28 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 1.92/2.36/2.87
```

</details>

<!-- retry: 90s -->
On **PE_2**, run:

```saos
ping ip destination FC00::1 source FC00::2 repeat-count 3
```

Pass: Output contains `100.00 percent`

<details><summary>Example output</summary>

```
Sending 3 ICMP Echos to FC00::1, timeout is 1 second

Codes: 
'!' - Success, 'Q' - Request not sent, '.' - Timeout 

 Type 'Ctrl+C' to abort

! seq_num = 1  RTT = 2.00 ms  TTL = 255
! seq_num = 2  RTT = 2.94 ms  TTL = 255
! seq_num = 3  RTT = 2.04 ms  TTL = 255
Success Rate is 100.00 percent (3/3)
Round-trip min/avg/max = 2.00/2.33/2.94
```

</details>
