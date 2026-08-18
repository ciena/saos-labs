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

No configuration commands; this is a verification-only task.

## Solution for Task 2

### PE_1

```saos
# Task 2 start
isis instance Bootcamp level-type level-1 net 49.0001.0172.0016.0001.00
isis instance Bootcamp interfaces interface lb1 interface-type point-to-point
isis instance Bootcamp interfaces interface PE_1-PE_2-if interface-type point-to-point level-type level-1
# Task 2 end
```

## Solution for Task 3

### PE_2

```saos
# Task 3 start
isis instance Bootcamp level-type level-1 net 49.0001.0172.0016.0002.00
isis instance Bootcamp interfaces interface lb1 interface-type point-to-point
isis instance Bootcamp interfaces interface PE_1-PE_2-if interface-type point-to-point level-type level-1
# Task 3 end
```

## Solution for Task 4

No configuration commands; this is a verification-only task.

## Solution for Task 5

No configuration commands; this is a verification-only task.

## Solution for Task 6

### PE_1

```saos
# Task 6 start
isis instance Bootcamp interfaces interface lb1 address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if address-families address-family ipv6 unicast
# Task 6 end
```

### PE_2

```saos
# Task 6 start
isis instance Bootcamp interfaces interface lb1 address-families address-family ipv6 unicast
isis instance Bootcamp interfaces interface PE_1-PE_2-if address-families address-family ipv6 unicast
# Task 6 end
```

## Solution for Task 7

No configuration commands; this is a verification-only task.

## Solution for Task 8

### PE_1

```saos
# Task 8 start
isis instance Bootcamp interfaces interface PE_1-PE_2-if level-1 password ciena123
# Task 8 end
```

### PE_2

```saos
# Task 8 start
isis instance Bootcamp interfaces interface PE_1-PE_2-if level-1 password ciena123
# Task 8 end
```
