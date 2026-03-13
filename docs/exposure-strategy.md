# Exposure Strategy

## Lab Environment (Current)
* Local-only lab exposure initially.
* Services resolvable via a local `/etc/hosts` file or internal DNS server.

## Internal-Only Services
* Headlamp
* Grafana
* Argo CD
* Internal APIs

## Later Phases
* HTTPS exposure via cert-manager (self-signed or Let's Encrypt DNS challenge).
