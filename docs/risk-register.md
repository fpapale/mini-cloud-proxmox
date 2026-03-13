# Risk Register

| Risk | Description | Mitigation |
|---|---|---|
| CT/LXC limitations | Certain K8s features (e.g. storage CSI) fail in LXC | Fall back to VM workers |
| Resource contention | Promtail/Longhorn consuming too much CPU | Implement limits and requests |
| Ingress exposure | Unintended access to internal services | Strict internal DNS, no port forwarding |
| Storage fragility | Local-path failing limits pod scheduling | Backup data via scripts / Proxmox |
| Secrets handling | Committing secrets to git | Use SOPS or External Secrets |
| Backup gaps | Missing application state in Git | Routine Proxmox snapshots and volume backups |
