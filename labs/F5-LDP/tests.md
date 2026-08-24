Deploy `F5-LDP`, then run the following validation checks.

## G1: Task 1 — Configure LDP on PE_1

On **PE_1**, run:

```saos
show ldp
```

Pass: Output contains `172.16.0.1`

<details><summary>Example output</summary>

```
+---------------------- LDP STATE ----------------------+
| Name                         | Value                  |
+------------------------------+------------------------+
| Instance                     | default                |
| Version                      | 1                      |
| FEC Count                    | 3                      |
| Session Count                | Total:1     UP:1       |
| Targeted Count               | Total:0     UP:0       |
| PW Status TLV                | False                  |
| Inter-area LSP               | False                  |
| Neighbor Liveness (s)        | 120                    |
| Max Recovery (s)             | 120                    |
| GR helper-enable             | True                   |
| GR enable                    | False                  |
| Router ID                    | 172.16.0.1             |
| Advertisement Mode           | downstream-unsolicited |
| Label Retention Mode         | liberal                |
| Label Control Mode           | ordered                |
| Targeted Hello Hold Time (s) | 45                     |
| Targeted Hello Interval (s)  | 15                     |
| Hold Time (s)                | 15                     |
| Hello Interval (s)           | 5                      |
| Keepalive Interval (s)       | 10                     |
| Keepalive Timeout (s)        | 30                     |
| Label Space                  | 0                      |
| Transport Address            | 172.16.0.1             |
+------------------------------+------------------------+
```

</details>

## G2: Task 2 — Configure LDP on PE_2

On **PE_2**, run:

```saos
show ldp
```

Pass: Output contains `172.16.0.2`

<details><summary>Example output</summary>

```
+---------------------- LDP STATE ----------------------+
| Name                         | Value                  |
+------------------------------+------------------------+
| Instance                     | default                |
| Version                      | 1                      |
| FEC Count                    | 3                      |
| Session Count                | Total:1     UP:1       |
| Targeted Count               | Total:0     UP:0       |
| PW Status TLV                | False                  |
| Inter-area LSP               | False                  |
| Neighbor Liveness (s)        | 120                    |
| Max Recovery (s)             | 120                    |
| GR helper-enable             | True                   |
| GR enable                    | False                  |
| Router ID                    | 172.16.0.2             |
| Advertisement Mode           | downstream-unsolicited |
| Label Retention Mode         | liberal                |
| Label Control Mode           | ordered                |
| Targeted Hello Hold Time (s) | 45                     |
| Targeted Hello Interval (s)  | 15                     |
| Hold Time (s)                | 15                     |
| Hello Interval (s)           | 5                      |
| Keepalive Interval (s)       | 10                     |
| Keepalive Timeout (s)        | 30                     |
| Label Space                  | 0                      |
| Transport Address            | 172.16.0.2             |
+------------------------------+------------------------+
```

</details>

## G3: Task 3 — Verify the alternative transport

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show ldp adjacencies
```

Pass: Output contains `172.16.0.2` and `PE_1-PE_2-if`

<details><summary>Example output</summary>

```
+----------------------- LDP ADJACENCY STATE ------------------------+
|            |              |  Hold    |                |            |
| IP Address |    Interface | Time (s) | LDP Identifier |    Type    |
+------------+--------------+----------+----------------+------------+
| 172.16.1.2 | PE_1-PE_2-if |    15    |     172.16.0.2 | LINK HELLO |
+------------+--------------+----------+----------------+------------+
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
show ldp adjacencies
```

Pass: Output contains `172.16.0.1` and `PE_1-PE_2-if`

<details><summary>Example output</summary>

```
+----------------------- LDP ADJACENCY STATE ------------------------+
|            |              |  Hold    |                |            |
| IP Address |    Interface | Time (s) | LDP Identifier |    Type    |
+------------+--------------+----------+----------------+------------+
| 172.16.1.1 | PE_1-PE_2-if |    15    |     172.16.0.1 | LINK HELLO |
+------------+--------------+----------+----------------+------------+
```

</details>

<!-- retry: 120s -->
On **PE_1**, run:

```saos
show mpls ftn-table
```

Pass: Output contains `PE_1-PE_2-if` and `172.16.0.2` and `push`

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
+------------------------------------------------------------------------------- MPLS FTN TABLE -------------------------------------------------------------------------------+
|          |                    |                                      |        |          Label          |                  |                 |  Oper  | Admin  |    Inner    |
|   Code   |        FEC         |              Qualifiers              | OpCode |     In     |    Out     |  Out Interface   |     Next Hop    | Status | Status | Label Stack |
+----------+--------------------+--------------------------------------+--------+------------+------------+------------------+-----------------+--------+--------+-------------+
| L *>     | 172.16.0.2/32      | -                                    |  push  | -          | 3          | PE_1-PE_2-if     | 172.16.1.2      |   Up   |   Up   |             |
+----------+--------------------+--------------------------------------+--------+------------+------------+------------------+-----------------+--------+--------+-------------+
```

</details>

<!-- retry: 120s -->
On **PE_2**, run:

```saos
show mpls ftn-table
```

Pass: Output contains `PE_1-PE_2-if` and `172.16.0.1` and `push`

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
+------------------------------------------------------------------------------- MPLS FTN TABLE -------------------------------------------------------------------------------+
|          |                    |                                      |        |          Label          |                  |                 |  Oper  | Admin  |    Inner    |
|   Code   |        FEC         |              Qualifiers              | OpCode |     In     |    Out     |  Out Interface   |     Next Hop    | Status | Status | Label Stack |
+----------+--------------------+--------------------------------------+--------+------------+------------+------------------+-----------------+--------+--------+-------------+
| L *>     | 172.16.0.1/32      | -                                    |  push  | -          | 3          | PE_1-PE_2-if     | 172.16.1.1      |   Up   |   Up   |             |
+----------+--------------------+--------------------------------------+--------+------------+------------+------------------+-----------------+--------+--------+-------------+
```

</details>
