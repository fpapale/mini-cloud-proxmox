# ADR-001: Topology

**Status:** Proposed

**Context:** We need a balance of resource utilization and isolation on a single Proxmox node.
**Decision:** We will use 1 Control Plane VM and 2 LXC (CT) workers.
**Consequences:** Low overhead for workers, but potential limitations with advanced K8s storage networking.
