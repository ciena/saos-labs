# F1 — Topology

![F1 topology](./topo.clab.svg)

![F1 detail](./topo.detail.svg)

## Containerlab topology

```yaml
name: F1-Loopbacks-and-Interfaces
topology:
  defaults:
    kind: ciena_saos
    image: vrnetlab/ciena_saos:10-12-00-0228
    labels:
      lab-mode: hands-on
  nodes:
    PE_1:
      type: '5162'
      startup-config: configs/PE_1.cfg.partial
    PE_2:
      type: '5162'
      startup-config: configs/PE_2.cfg.partial
    PE_3:
      type: '5162'
      labels:
        lab-state: unused
      startup-config: configs/PE_3.cfg.partial
    CE1:
      type: '3984'
      labels:
        lab-state: unused
      startup-config: configs/CE1.cfg.partial
    CE2:
      type: '3984'
      labels:
        lab-state: unused
      startup-config: configs/CE2.cfg.partial
  links:
  - endpoints: [ "PE_1:1", "PE_2:1" ]
  - endpoints: [ "PE_1:2", "CE1:1" ]
  - endpoints: [ "PE_2:2", "CE2:1" ]
  - endpoints: [ "PE_2:4", "PE_3:1" ]
  - endpoints: [ "PE_1:4", "PE_3:3" ]
  - endpoints: [ "CE2:2", "PE_3:2" ]
```
