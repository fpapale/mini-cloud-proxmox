# GitOps Strategy

## Tool
* Argo CD

## Justification
* Standardizes deployments
* Drift detection
* Visual UI for application states

## Separation of Concerns
* Infrastructure (observability, ingress, cert-manager) vs Apps (n8n, nextcloud).

## App-of-Apps Model
* A root Argo CD Application will point to the `k8s/gitops/app-of-apps` directory, which contains other Application manifests.
