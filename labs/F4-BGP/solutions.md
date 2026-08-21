# Solutions

Use the preloaded baseline for context, then apply the learner solution blocks in task order.

## Preloaded baseline

### PE_1

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

### PE_2

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

### PE_3

```saos
# Preloaded start
system config hostname PE_3
# Preloaded end
```

### CE1

```saos
# Preloaded start
system config hostname CE1
# Preloaded end
```

### CE2

```saos
# Preloaded start
system config hostname CE2
# Preloaded end
```

## Solution for Task 1

### PE_1

```saos
# Task 1 start
bgp instance 65032 router-id 172.16.0.1
# Task 1 end
```

### PE_2

```saos
# Task 1 start
bgp instance 65032 router-id 172.16.0.2
# Task 1 end
```

## Solution for Task 2

### PE_1

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

### PE_2

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

## Solution for Task 3

### PE_1

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

### PE_2

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

## Solution for Task 4

### PE_1

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

### PE_2

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

## Solution for Task 5

No configuration commands; this is a verification-only task.
