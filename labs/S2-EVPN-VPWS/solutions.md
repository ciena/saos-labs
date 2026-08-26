# Solutions

Use the preloaded baseline for context, then apply the learner solution blocks in task order.

## Preloaded baseline

### PE_1

```saos
# Preloaded start
fds fd PE_1-PE_2-FD mode vpls
oc-if:interfaces interface lb1 config name lb1 type loopback
oc-if:interfaces interface lb1 ipv4 addresses address 172.16.0.1 config ip 172.16.0.1 prefix-length 32
oc-if:interfaces interface lb1 ipv6 addresses address FC00::1 config ip FC00::1 prefix-length 128
oc-if:interfaces interface PE_1-PE_2-if config mtu 1500 name PE_1-PE_2-if type ip
oc-if:interfaces interface PE_1-PE_2-if config underlay-binding config fd PE_1-PE_2-FD
oc-if:interfaces interface PE_1-PE_2-if ipv4 addresses address 172.16.1.1 config ip 172.16.1.1 prefix-length 30
oc-if:interfaces interface PE_1-PE_2-if ipv6 addresses address FC00::600 config ip FC00::600 prefix-length 127
oc-if:interfaces interface lb10 config name lb10 type loopback
oc-if:interfaces interface lb10 ipv4 addresses address 10.65.0.32 config ip 10.65.0.32 prefix-length 32
routing-policy prefix-lists prefix-list lb10 mode ipv4 sequence 1 action permit ip-prefix 10.65.0.32/32
routing-policy policies policy lb10 statement 1 action permit
routing-policy policies policy lb10 statement 1 match route-entry lb10
routing-policy policies policy lb10 statement 1 set community append standard 65032:100
routing-policy policies policy lb10 statement 2 action deny
classifiers classifier CLASSIFIER-UNTAGGED filter-entry vtag-stack untagged-exclude-priority-tagged false
fps fp PE_1-PE_2-FP classifier-list-precedence 7 fd-name PE_1-PE_2-FD logical-port 1 mtu-size 2000 stats-collection on classifier-list CLASSIFIER-UNTAGGED
mpls interfaces interface PE_1-PE_2-if label-switching true
mpls interfaces interface lb1 label-switching true
segment-routing connected-prefix-sid-map 172.16.0.1/32 interface lb1 start-sid 1 value-type index
bgp instance 65032 router-id 172.16.0.1
bgp instance 65032 address-family ipv4 unicast
    exit
  exit
exit
bgp instance 65032 address-family ipv4 unicast redistribute connected policy lb10
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
bgp instance 65032 peer 172.16.0.2 remote-as 65032
bgp instance 65032 peer 172.16.0.2 update-source-interface lb1
bgp instance 65032 peer 172.16.0.2 password ciena123
bgp instance 65032 peer 172.16.0.2 address-family ipv4 unicast activate true soft-reconfiguration-inbound true
bgp instance 65032 peer 172.16.0.2 address-family vpnv4 unicast activate true
bgp instance 65032 peer 172.16.0.2 address-family l2vpn evpn activate true
bgp instance 65032 peer 172.16.0.2 address-family ipv4 labeled-unicast activate true
system config hostname PE_1
isis instance Bootcamp level-type level-1 net 49.0001.0172.0016.0001.00
isis instance Bootcamp cspf-flag true
isis instance Bootcamp interfaces interface lb1 interface-type point-to-point
isis instance Bootcamp interfaces interface lb1 address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if interface-type point-to-point level-type level-1
isis instance Bootcamp interfaces interface PE_1-PE_2-if address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if level-1 password ciena123
isis instance Bootcamp mpls-te level-type level-1 router-id 172.16.0.1
isis instance Bootcamp segment-routing enabled true srgb 16000 23999
isis instance Bootcamp segment-routing bindings advertise true receive true
# Preloaded end
```

### PE_2

```saos
# Preloaded start
fds fd PE_1-PE_2-FD mode vpls
oc-if:interfaces interface lb1 config name lb1 type loopback
oc-if:interfaces interface lb1 ipv4 addresses address 172.16.0.2 config ip 172.16.0.2 prefix-length 32
oc-if:interfaces interface lb1 ipv6 addresses address FC00::2 config ip FC00::2 prefix-length 128
oc-if:interfaces interface PE_1-PE_2-if config mtu 1500 name PE_1-PE_2-if type ip
oc-if:interfaces interface PE_1-PE_2-if config underlay-binding config fd PE_1-PE_2-FD
oc-if:interfaces interface PE_1-PE_2-if ipv4 addresses address 172.16.1.2 config ip 172.16.1.2 prefix-length 30
oc-if:interfaces interface PE_1-PE_2-if ipv6 addresses address FC00::601 config ip FC00::601 prefix-length 127
oc-if:interfaces interface lb10 config name lb10 type loopback
oc-if:interfaces interface lb10 ipv4 addresses address 10.65.0.33 config ip 10.65.0.33 prefix-length 32
routing-policy prefix-lists prefix-list lb10 mode ipv4 sequence 1 action permit ip-prefix 10.65.0.33/32
routing-policy policies policy lb10 statement 1 action permit
routing-policy policies policy lb10 statement 1 match route-entry lb10
routing-policy policies policy lb10 statement 1 set community append standard 65032:100
routing-policy policies policy lb10 statement 2 action deny
classifiers classifier CLASSIFIER-UNTAGGED filter-entry vtag-stack untagged-exclude-priority-tagged false
fps fp PE_1-PE_2-FP classifier-list-precedence 7 fd-name PE_1-PE_2-FD logical-port 1 mtu-size 2000 stats-collection on classifier-list CLASSIFIER-UNTAGGED
mpls interfaces interface PE_1-PE_2-if label-switching true
mpls interfaces interface lb1 label-switching true
segment-routing connected-prefix-sid-map 172.16.0.2/32 interface lb1 start-sid 2 value-type index
bgp instance 65032 router-id 172.16.0.2
bgp instance 65032 address-family ipv4 unicast
    exit
  exit
exit
bgp instance 65032 address-family ipv4 unicast redistribute connected policy lb10
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
bgp instance 65032 peer 172.16.0.1 remote-as 65032
bgp instance 65032 peer 172.16.0.1 update-source-interface lb1
bgp instance 65032 peer 172.16.0.1 password ciena123
bgp instance 65032 peer 172.16.0.1 address-family ipv4 unicast activate true soft-reconfiguration-inbound true
bgp instance 65032 peer 172.16.0.1 address-family vpnv4 unicast activate true
bgp instance 65032 peer 172.16.0.1 address-family l2vpn evpn activate true
bgp instance 65032 peer 172.16.0.1 address-family ipv4 labeled-unicast activate true
system config hostname PE_2
isis instance Bootcamp level-type level-1 net 49.0001.0172.0016.0002.00
isis instance Bootcamp cspf-flag true
isis instance Bootcamp interfaces interface lb1 interface-type point-to-point
isis instance Bootcamp interfaces interface lb1 address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if interface-type point-to-point level-type level-1
isis instance Bootcamp interfaces interface PE_1-PE_2-if address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if level-1 password ciena123
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

### CE_1

```saos
# Preloaded start
system config hostname CE_1
# Preloaded end
```

### CE_2

```saos
# Preloaded start
system config hostname CE_2
# Preloaded end
```

### CE_3

```saos
# Preloaded start
system config hostname CE_3
# Preloaded end
```

## Solution for Task 1

No configuration commands; this is a verification-only task.

## Solution for Task 2

### PE_1

```saos
# Task 2 start
fds fd PE_1-PE_3-FD mode vpls
oc-if:interfaces interface PE_1-PE_3-if config mtu 1500 name PE_1-PE_3-if type ip
oc-if:interfaces interface PE_1-PE_3-if config underlay-binding config fd PE_1-PE_3-FD
oc-if:interfaces interface PE_1-PE_3-if ipv4 addresses address 172.16.2.5 config ip 172.16.2.5 prefix-length 30
oc-if:interfaces interface PE_1-PE_3-if ipv6 addresses address FC00::60A config ip FC00::60A prefix-length 127
fps fp PE_1-PE_3-FP classifier-list-precedence 7 fd-name PE_1-PE_3-FD logical-port 4 mtu-size 2000 stats-collection on classifier-list CLASSIFIER-UNTAGGED
mpls interfaces interface PE_1-PE_3-if label-switching true
isis instance Bootcamp interfaces interface PE_1-PE_3-if interface-type point-to-point level-type level-1
isis instance Bootcamp interfaces interface PE_1-PE_3-if address-families address-family ipv6 unicast
# Task 2 end
```

### PE_2

```saos
# Task 2 start
fds fd PE_2-PE_3-FD mode vpls
oc-if:interfaces interface PE_2-PE_3-if config mtu 1500 name PE_2-PE_3-if type ip
oc-if:interfaces interface PE_2-PE_3-if config underlay-binding config fd PE_2-PE_3-FD
oc-if:interfaces interface PE_2-PE_3-if ipv4 addresses address 172.16.2.1 config ip 172.16.2.1 prefix-length 30
oc-if:interfaces interface PE_2-PE_3-if ipv6 addresses address FC00::608 config ip FC00::608 prefix-length 127
fps fp PE_2-PE_3-FP classifier-list-precedence 7 fd-name PE_2-PE_3-FD logical-port 4 mtu-size 2000 stats-collection on classifier-list CLASSIFIER-UNTAGGED
mpls interfaces interface PE_2-PE_3-if label-switching true
isis instance Bootcamp interfaces interface PE_2-PE_3-if interface-type point-to-point level-type level-1
isis instance Bootcamp interfaces interface PE_2-PE_3-if address-families address-family ipv6 unicast
# Task 2 end
```

### PE_3

```saos
# Task 2 start
fds fd PE_2-PE_3-FD mode vpls
fds fd PE_1-PE_3-FD mode vpls
oc-if:interfaces interface lb1 config name lb1 type loopback
oc-if:interfaces interface lb1 ipv4 addresses address 172.16.0.5 config ip 172.16.0.5 prefix-length 32
oc-if:interfaces interface lb1 ipv6 addresses address FC00::5 config ip FC00::5 prefix-length 128
oc-if:interfaces interface PE_2-PE_3-if config mtu 1500 name PE_2-PE_3-if type ip
oc-if:interfaces interface PE_2-PE_3-if config underlay-binding config fd PE_2-PE_3-FD
oc-if:interfaces interface PE_2-PE_3-if ipv4 addresses address 172.16.2.2 config ip 172.16.2.2 prefix-length 30
oc-if:interfaces interface PE_2-PE_3-if ipv6 addresses address FC00::609 config ip FC00::609 prefix-length 127
oc-if:interfaces interface PE_1-PE_3-if config mtu 1500 name PE_1-PE_3-if type ip
oc-if:interfaces interface PE_1-PE_3-if config underlay-binding config fd PE_1-PE_3-FD
oc-if:interfaces interface PE_1-PE_3-if ipv4 addresses address 172.16.2.6 config ip 172.16.2.6 prefix-length 30
oc-if:interfaces interface PE_1-PE_3-if ipv6 addresses address FC00::60B config ip FC00::60B prefix-length 127
classifiers classifier CLASSIFIER-UNTAGGED filter-entry vtag-stack untagged-exclude-priority-tagged false
fps fp PE_2-PE_3-FP classifier-list-precedence 7 fd-name PE_2-PE_3-FD logical-port 1 mtu-size 2000 stats-collection on classifier-list CLASSIFIER-UNTAGGED
fps fp PE_1-PE_3-FP classifier-list-precedence 7 fd-name PE_1-PE_3-FD logical-port 3 mtu-size 2000 stats-collection on classifier-list CLASSIFIER-UNTAGGED
mpls interfaces interface lb1 label-switching true
mpls interfaces interface PE_2-PE_3-if label-switching true
mpls interfaces interface PE_1-PE_3-if label-switching true
segment-routing connected-prefix-sid-map 172.16.0.5/32 interface lb1 start-sid 5 value-type index
isis instance Bootcamp cspf-flag true level-type level-1 net 49.0001.0172.0016.0005.00
isis instance Bootcamp interfaces interface lb1 interface-type point-to-point
isis instance Bootcamp interfaces interface lb1 address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_2-PE_3-if interface-type point-to-point level-type level-1
isis instance Bootcamp interfaces interface PE_2-PE_3-if address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_3-if interface-type point-to-point level-type level-1
isis instance Bootcamp interfaces interface PE_1-PE_3-if address-families address-family ipv6 unicast
isis instance Bootcamp mpls-te level-type level-1 router-id 172.16.0.5
isis instance Bootcamp segment-routing enabled true srgb 16000 23999
isis instance Bootcamp segment-routing bindings advertise true receive true
# Task 2 end
```

## Solution for Task 3

### PE_1

```saos
# Task 3 start
bgp instance 65032 peer 172.16.0.5 remote-as 65032 update-source-interface lb1 address-family l2vpn evpn activate true
# Task 3 end
```

### PE_2

```saos
# Task 3 start
bgp instance 65032 peer 172.16.0.5 remote-as 65032 update-source-interface lb1 address-family l2vpn evpn activate true
# Task 3 end
```

### PE_3

```saos
# Task 3 start
bgp instance 65032 router-id 172.16.0.5 address-family l2vpn evpn
bgp instance 65032 peer 172.16.0.1 remote-as 65032 update-source-interface lb1 address-family l2vpn evpn activate true
bgp instance 65032 peer 172.16.0.2 remote-as 65032 update-source-interface lb1 address-family l2vpn evpn activate true
# Task 3 end
```

## Solution for Task 4

### PE_1

```saos
# Task 4 start
fds fd vpws_1-fd mode evpn-vpws
classifiers classifier CLASSIFIER-105 filter-entry vtag-stack vtags 1 vlan-id 105
fps fp vpws_1-fp fd-name vpws_1-fd logical-port 2 stats-collection on classifier-list CLASSIFIER-105
fps fp vpws_1-fp egress-l2-transform push-vid-105 vlan-stack 1 push-tpid tpid-8100 push-vid 105
evpn evpn-instances evpn-instance 102 vpws-cross-connect-fd vpws_1-fd l2mtu 9216 local-service-id 2102 remote-service-id 1102
evpn evpn-instances evpn-instance 102 route-distinguisher ip-based value 172.16.0.1:102
evpn evpn-instances evpn-instance 102 vpn-target 0:102:102 route-target-type both
# Task 4 end
```

### PE_3

```saos
# Task 4 start
fds fd vpws_1-fd mode evpn-vpws
classifiers classifier CLASSIFIER-105 filter-entry vtag-stack vtags 1 vlan-id 105
fps fp vpws_1-fp fd-name vpws_1-fd logical-port 2 stats-collection on classifier-list CLASSIFIER-105
fps fp vpws_1-fp egress-l2-transform push-vid-105 vlan-stack 1 push-tpid tpid-8100 push-vid 105
evpn evpn-instances evpn-instance 102 vpws-cross-connect-fd vpws_1-fd l2mtu 9216 local-service-id 1102 remote-service-id 2102
evpn evpn-instances evpn-instance 102 route-distinguisher ip-based value 172.16.0.5:102
evpn evpn-instances evpn-instance 102 vpn-target 0:102:102 route-target-type both
# Task 4 end
```

## Solution for Task 5

### CE_1

```saos
# Task 5 start
fds fd CE_1-CE_2-FD mode vpls
oc-if:interfaces interface CE_1-CE_2-if config mtu 1500 name CE_1-CE_2-if type ip
oc-if:interfaces interface CE_1-CE_2-if config underlay-binding config fd CE_1-CE_2-FD
oc-if:interfaces interface CE_1-CE_2-if ipv4 addresses address 172.16.105.1 config ip 172.16.105.1 prefix-length 30
classifiers classifier CLASSIFIER-105 filter-entry vtag-stack vtags 1 vlan-id 105
fps fp CE_1-CE_2-FP fd-name CE_1-CE_2-FD logical-port 1 stats-collection on classifier-list CLASSIFIER-105
fps fp CE_1-CE_2-FP egress-l2-transform push-vid-105 vlan-stack 1 push-tpid tpid-8100 push-vid 105
# Task 5 end
```

## Solution for Task 6

### CE_2

```saos
# Task 6 start
fds fd CE_1-CE_2-FD mode vpls
oc-if:interfaces interface CE_1-CE_2-if config mtu 1500 name CE_1-CE_2-if type ip
oc-if:interfaces interface CE_1-CE_2-if config underlay-binding config fd CE_1-CE_2-FD
oc-if:interfaces interface CE_1-CE_2-if ipv4 addresses address 172.16.105.2 config ip 172.16.105.2 prefix-length 30
classifiers classifier CLASSIFIER-105 filter-entry vtag-stack vtags 1 vlan-id 105
fps fp CE_1-CE_2-FP fd-name CE_1-CE_2-FD logical-port 2 stats-collection on classifier-list CLASSIFIER-105
fps fp CE_1-CE_2-FP egress-l2-transform push-vid-105 vlan-stack 1 push-tpid tpid-8100 push-vid 105
# Task 6 end
```
