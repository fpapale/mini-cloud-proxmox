# Kubernetes Manifests

Core, non-Helm manifests for cluster operations.

### Structure
- `base/` - Shared resources (namespaces, rbac, default storage).
- `apps/` - Application deployments (Phase 4).
- `gitops/` - Argo CD App-of-Apps manifests (Phase 3).
- `observability/` - Monitoring stack (Phase 2).
- `storage/` - Storage provisioner configs (Phase 1 / 5).
