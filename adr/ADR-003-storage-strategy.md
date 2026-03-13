# ADR-003: Storage Strategy

**Status:** Proposed

**Context:** We need persistent volumes for apps like Postgres and Nextcloud.
**Decision:** Phase 1 uses K3s default local-path provisioner. Longhorn is deferred to Phase 3.
**Consequences:** No HA storage initially, meaning pod loss or node loss requires manual intervention or restores.
