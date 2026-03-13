# Storage Strategy

## Phase 1
* local-path provisioner (default K3s). Fast and simple for initial non-HA testing.

## Phase 2
* Persistent deployments for databases (Postgres, Redis) mapped to local-path PVCs pinned to specific nodes.

## Phase 3
* Longhorn (Optional) for distributed block storage, enhancing HA.

## Pros/Cons Summary
* **Local-path:** Low overhead, high performance, but zero redundancy.
* **Longhorn:** High redundancy and replication, but noticeable IO and CPU overhead for small nodes.
