# ADR-002: K3s Formulation

**Status:** Proposed

**Context:** A lightweight Kubernetes distribution is required.
**Decision:** Use K3s due to its low footprint and built-in SQLite datastore mapping well to single-master setups.
**Consequences:** Less enterprise bloat, but lacks out-of-the-box HA etcd (unless configured).
