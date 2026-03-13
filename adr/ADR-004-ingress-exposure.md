# ADR-004: Ingress Exposure

**Status:** Proposed

**Context:** How services are exposed to the network.
**Decision:** Keep it local-only initially using Traefik and `/etc/hosts`. 
**Consequences:** Secure for lab, but requires client config to test.
