import os

root = r"d:\mini-cloud-proxmox"

# Files and their starter content
files_to_create = {
    "README.md": """# Mini Cloud Proxmox

## Purpose
A home lab mini-cloud running on Proxmox VE with a Kubernetes cluster based on K3s.
Designed to host infrastructure apps, databases, and lab experiments.

## Target Topology
* 1x Proxmox VE hypervisor
* 1x Control Plane VM (K3s server)
* 2x Worker Nodes CT/LXC (K3s agent)

## Target Services
* Traefik (Ingress)
* Headlamp (Dashboard)
* Observability: Prometheus + Grafana, Loki + Promtail
* Argo CD (GitOps)
* Nextcloud
* n8n
* PostgreSQL
* Redis
* Optional: AI services (Ollama / Open WebUI)
* Optional: Distributed storage (Longhorn)

## Implementation Phases
* Phase 0: Proxmox base prep
* Phase 1: K3s bootstrap
* Phase 2: Dashboard + observability
* Phase 3: GitOps
* Phase 4: Useful apps
* Phase 5: Hardening, backups, optional AI/storage expansion

## Repository Map
* `docs/`: Architecture and planning documents
* `diagrams/`: Mermaid diagrams
* `adr/`: Architecture Decision Records
* `notes/`: Backlog and experiments
* `scripts/`: Automation scripts
* `inventory/`: Node and IP planning
* `k8s/`: Kubernetes manifests and GitOps
* `helm/`: Helm values placeholders

## How to bootstrap this repo with Antigravity
Run the prompt specified in AGENTS.md to initialize or extend this repository.

## Parameters to customize before real deployment
| Parameter | Example Value |
|---|---|
| project root path | `/opt/mini-cloud` |
| workspace folder path | `/opt/mini-cloud/proxmox` |
| cluster name | `home-k3s` |
| control-plane hostname | `master01` |
| worker hostnames | `worker01, worker02` |
| node type | `VM, CT(LXC)` |
| IP subnet | `192.168.1.0/24` |
| control-plane IP | `192.168.1.10` |
| worker IPs | `192.168.1.11, 192.168.1.12` |
| local lab domain | `lab.local` |
| ingress hostnames | `*.lab.local` |
| storage mode | `local-path` |
| Git repository URL | `https://github.com/fpapale/mini-cloud-proxmox` |
| Argo CD namespace | `argocd` |
| optional AI enablement | `false` |
""",
    ".gitignore": """# OS generated
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/

# Kubeconfig
kubeconfig.yaml
*.kubeconfig

# Secrets
.env
*.secret.yaml

# Archives
*.tar.gz
*.zip
""",
    "docs/architecture.md": """# Architecture

## Executive Summary
This document outlines the architecture for the mini-cloud running on Proxmox VE with K3s.

## Architecture Layers
* **Proxmox layer**: Base hypervisor.
* **VM/CT layout**: 1 VM (control plane) + 2 CTs (workers).
* **K3s cluster layer**: Kubernetes distribution.
* **Ingress layer**: Traefik.
* **Observability layer**: Prometheus, Grafana, Loki, Promtail.
* **GitOps layer**: Argo CD.
* **Apps/data layer**: Nextcloud, n8n, databases.

Note: AI and Longhorn are optional later phases.
""",
    "docs/topology.md": """# Topology

* **Preferred topology**: 1 control-plane VM + 2 CT workers.
* **Trade-offs of CT workers**: Lower resource usage, but potential restrictions on certain kernel features or storage drivers.
* **Fallback option**: all-VM if CT limitations appear.
""",
    "docs/networking.md": """# Networking

* **North-south traffic**: Handled by Traefik ingress.
* **East-west traffic**: Internal cluster networking (Flannel/Cilium).
* **Admin/management traffic**: SSH, Proxmox API, K3s API.
* **Example hostnames**: `headlamp.lab`, `grafana.lab`, `argocd.lab`, `nextcloud.lab`, `n8n.lab`.
""",
    "docs/storage-strategy.md": """# Storage Strategy

* **Phase 1**: local-path/default storage.
* **Phase 2**: persistent services using local-path.
* **Phase 3**: Longhorn optional (distributed block storage).
* **Pros/Cons summary**: local-path is simple but tied to a specific node; Longhorn adds HA but uses more resources.
""",
    "docs/exposure-strategy.md": """# Exposure Strategy

* Local-only lab exposure first.
* Hosts file / local DNS approach for initial access.
* Define which services should be internal-only (e.g., Prometheus UI).
* HTTPS/cert-manager as a later phase.
""",
    "docs/observability.md": """# Observability

* **Metrics Server**: For HPA and basic `kubectl top`.
* **Prometheus**: Metric collection and storage.
* **Grafana**: Dashboard visualization.
* **Loki**: Log aggregation.
* **Promtail**: Log shipping to Loki.
""",
    "docs/gitops-strategy.md": """# GitOps Strategy

* **Why Argo CD**: Declarative, automated deployment from Git.
* **Separation**: Clear separation between infra and apps.
* **Suggested future**: app-of-apps model for scalable management.
""",
    "docs/implementation-roadmap.md": """# Implementation Roadmap

* Phase 0: Proxmox base prep
* Phase 1: K3s bootstrap
* Phase 2: Dashboard + observability
* Phase 3: GitOps
* Phase 4: Useful apps
* Phase 5: Hardening, backups, optional AI/storage expansion
""",
    "docs/bom-sizing.md": """# BOM & Sizing

| Tier | CPU | RAM | Storage | Notes |
|---|---|---|---|---|
| Minimum viable | 4 vCPU | 8GB | 50GB | Basic services only |
| Recommended | 8 vCPU | 16GB | 100GB | Standard lab setup |
| Expanded with AI | 12+ vCPU | 32GB+ | 200GB+ | Needs GPU for LLMs |
""",
    "docs/risk-register.md": """# Risk Register

| Risk | Description | Mitigation |
|---|---|---|
| CT/LXC limitations | Some K8s features may fail in LXC | Use VMs as fallback |
| Resource contention | High memory usage from monitoring | Tune requests/limits |
| Ingress exposure | Security risks if exposed | Keep lab local only |
| Storage fragility | Data loss with local-path | Implement backups |
| Secrets handling | Hardcoded secrets in Git | Use .env or Sealed Secrets |
| Backup gaps | No disaster recovery plan | Setup Velero or Proxmox backups |
""",
    "docs/prompts/README.md": """# Installation Prompts
""",
    "diagrams/README.md": """# Diagrams
Store all architecture and flow diagrams here.
""",
    "diagrams/mini-cloud-architecture.mmd": """graph TD
    User -->|Browser| Traefik
    subgraph Proxmox
        subgraph K3s Cluster
            Traefik --> Headlamp
            Traefik --> ArgoCD
            Traefik --> Apps
            Traefik --> Prometheus
        end
    end
""",
    "diagrams/network-flows.mmd": """graph LR
    Admin -->|SSH/API| ControlPlane
    Ingress -->|HTTP/S| Services
    Services -->|Internal| Database
""",
    "diagrams/namespaces.mmd": """graph TD
    Cluster --> ingress
    Cluster --> observability
    Cluster --> gitops
    Cluster --> storage
    Cluster --> apps
    Cluster --> databases
    Cluster --> ai
    Cluster --> demo
""",
    "adr/README.md": """# Architecture Decision Records
Document all significant architectural decisions here.
""",
    "adr/ADR-001-topology.md": """# ADR-001: Topology

**Status:** Proposed

**Context:** Need to decide on the VM vs CT split for K3s nodes.

**Decision:** 1 VM control plane, 2 CT workers.

**Consequences:** Lower overhead, but potential LXC compatibility issues.
""",
    "adr/ADR-002-k3s-choice.md": """# ADR-002: K3s Choice

**Status:** Proposed

**Context:** Choosing a Kubernetes distribution.

**Decision:** K3s.

**Consequences:** Lightweight, easy to install, edge-focused.
""",
    "adr/ADR-003-storage-strategy.md": """# ADR-003: Storage Strategy

**Status:** Proposed

**Context:** Deciding on PV storage mechanism.

**Decision:** Use local-path initially, evaluate Longhorn later.

**Consequences:** No initial HA for data, simplified setup.
""",
    "adr/ADR-004-ingress-exposure.md": """# ADR-004: Ingress Exposure

**Status:** Proposed

**Context:** Managing external access to services.

**Decision:** Traefik ingress with local DNS and hosts file.

**Consequences:** Manual DNS updates required on client machines.
""",
    "adr/ADR-005-observability-stack.md": """# ADR-005: Observability Stack

**Status:** Proposed

**Context:** Selecting monitoring and logging tools.

**Decision:** Prometheus, Grafana, Loki, Promtail.

**Consequences:** Standard cloud-native stack, slightly high resource usage.
""",
    "notes/backlog.md": "# Backlog\n\n* Setup autodeploy\n",
    "notes/ideas.md": "# Ideas\n\n* Explore external-dns\n",
    "notes/lab-experiments.md": """# Lab Experiments

* [ ] pod self-healing
* [ ] node failure simulation
* [ ] rolling update
* [ ] rollback
* [ ] ingress routing
* [ ] PVC persistence
* [ ] node drain
* [ ] scaling
""",
    "scripts/README.md": "# Scripts\nAutomation and operational scripts.\n",
    "inventory/README.md": "# Inventory\nEnvironment infrastructure details.\n",
    "inventory/nodes.md": """# Nodes

| Node Name | Type | Role | CPU | RAM | Disk | IP |
|---|---|---|---|---|---|---|
| master01 | VM | Control | 2 | 4 | 20G | TBD |
| worker01 | CT | Worker | 2 | 4 | 20G | TBD |
| worker02 | CT | Worker | 2 | 4 | 20G | TBD |
""",
    "inventory/ips.md": """# IP Planning

| Service / Node | IP Address | MAC / Notes |
|---|---|---|
| Proxmox Host | 192.168.0.100 | |
| k3s-master | 192.168.0.101 | |
| k3s-worker1 | 192.168.0.102 | |
| k3s-worker2 | 192.168.0.103 | |
""",
    "inventory/resources.md": "# Resources Budget\nTotal CPU, RAM, Disk available.\n",
    "k8s/README.md": "# Kubernetes Manifests\nContains all K8s resources and GitOps apps.\n",
    "k8s/base/namespaces/namespaces.yaml": """apiVersion: v1
kind: Namespace
metadata:
  name: ingress
---
apiVersion: v1
kind: Namespace
metadata:
  name: observability
---
apiVersion: v1
kind: Namespace
metadata:
  name: gitops
---
apiVersion: v1
kind: Namespace
metadata:
  name: storage
---
apiVersion: v1
kind: Namespace
metadata:
  name: apps
---
apiVersion: v1
kind: Namespace
metadata:
  name: databases
---
apiVersion: v1
kind: Namespace
metadata:
  name: ai
---
apiVersion: v1
kind: Namespace
metadata:
  name: demo
""",
    "k8s/base/namespaces/kustomization.yaml": """apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - namespaces.yaml
""",
    "k8s/base/ingress/whoami-ingress.yaml": """# Demo ingress note: actual ingresses should live with the app manifests
""",
    "k8s/base/ingress/kustomization.yaml": """apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - whoami-ingress.yaml
""",
    "k8s/base/rbac/README.md": "# RBAC\nRole-based access control configs.\n",
    "k8s/base/storage/pvc-demo.yaml": """apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: demo-pvc
  namespace: demo
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
""",
    "k8s/base/storage/kustomization.yaml": """apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - pvc-demo.yaml
""",
    "k8s/base/certs/README.md": "# Certificates\nStore cert-manager configs here.\n",
    "k8s/observability/metrics-server/README.md": "# Metrics Server\nPhase 1 component.\n",
    "k8s/observability/prometheus/README.md": "# Prometheus\nPhase 2 component.\n",
    "k8s/observability/grafana/README.md": "# Grafana\nPhase 2 component.\n",
    "k8s/observability/loki/README.md": "# Loki\nPhase 2 component.\n",
    "k8s/observability/promtail/README.md": "# Promtail\nPhase 2 component.\n",
    "k8s/gitops/argocd/namespace.yaml": """apiVersion: v1
kind: Namespace
metadata:
  name: argocd
""",
    "k8s/gitops/argocd/install-notes.md": """# Install Notes
For Argo CD installation. Use this for initial bootstrap before GitOps takes over.
""",
    "k8s/gitops/argocd/kustomization.yaml": """apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - namespace.yaml
""",
    "k8s/gitops/applications/root-app.yaml": """apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: root-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/fpapale/mini-cloud-proxmox.git
    targetRevision: HEAD
    path: k8s/gitops/app-of-apps
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
""",
    "k8s/gitops/applications/observability-app.yaml": """apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: observability
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/fpapale/mini-cloud-proxmox.git
    targetRevision: HEAD
    path: k8s/observability
  destination:
    server: https://kubernetes.default.svc
    namespace: observability
""",
    "k8s/gitops/applications/demo-app.yaml": """apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: demo
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/fpapale/mini-cloud-proxmox.git
    targetRevision: HEAD
    path: k8s/apps/demo
  destination:
    server: https://kubernetes.default.svc
    namespace: demo
""",
    "k8s/gitops/applications/apps-app.yaml": """apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: apps
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/fpapale/mini-cloud-proxmox.git
    targetRevision: HEAD
    path: k8s/apps
  destination:
    server: https://kubernetes.default.svc
    namespace: apps
""",
    "k8s/gitops/app-of-apps/README.md": "# App of Apps\nPattern to manage multiple Argo CD applications here.\n",
    "k8s/apps/headlamp/README.md": "# Headlamp\nPhase 2 component.\n",
    "k8s/apps/nextcloud/README.md": "# Nextcloud\nPhase 4 component.\n",
    "k8s/apps/n8n/README.md": "# n8n\nPhase 4 component.\n",
    "k8s/apps/postgresql/README.md": "# PostgreSQL\nPhase 4 component.\n",
    "k8s/apps/redis/README.md": "# Redis\nPhase 4 component.\n",
    "k8s/apps/ai/README.md": "# AI Services\nOptional later phase.\n",
    "k8s/apps/demo/whoami-deployment.yaml": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: whoami
  namespace: demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: whoami
  template:
    metadata:
      labels:
        app: whoami
    spec:
      containers:
      - name: whoami
        image: traefik/whoami
        ports:
        - containerPort: 80
""",
    "k8s/apps/demo/whoami-service.yaml": """apiVersion: v1
kind: Service
metadata:
  name: whoami
  namespace: demo
spec:
  selector:
    app: whoami
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
""",
    "k8s/apps/demo/whoami-ingress.yaml": """apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: whoami
  namespace: demo
spec:
  ingressClassName: traefik
  rules:
  - host: whoami.lab
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: whoami
            port:
              number: 80
""",
    "k8s/apps/demo/kustomization.yaml": """apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - whoami-deployment.yaml
  - whoami-service.yaml
  - whoami-ingress.yaml
""",
    "helm/README.md": "# Helm Charts\nValues for Helm deployments.\n",
    "helm/repositories.md": """# Helm Repositories

* headlamp: https://headlamp-k8s.github.io/headlamp/
* prometheus-community: https://prometheus-community.github.io/helm-charts
* grafana: https://grafana.github.io/helm-charts
* argo: https://argoproj.github.io/argo-helm
* bitnami: https://charts.bitnami.com/bitnami
* nextcloud: https://nextcloud.github.io/helm/
* longhorn: https://charts.longhorn.io
""",
    "helm/headlamp/values.yaml": """# Minimal values for Headlamp
ingress:
  enabled: false
""",
    "helm/prometheus-stack/values.yaml": """# Minimal values for Prometheus Stack
grafana:
  enabled: true
""",
    "helm/loki/values.yaml": """# Minimal values for Loki
loki:
  auth_enabled: false
""",
    "helm/argocd/values.yaml": """# Minimal values for Argo CD
server:
  ingress:
    enabled: false
""",
    "helm/nextcloud/values.yaml": """# Minimal values for Nextcloud
nextcloud:
  host: nextcloud.lab
""",
    "helm/n8n/values.yaml": """# Minimal values for n8n
ingress:
  enabled: false
""",
    "helm/postgresql/values.yaml": """# Minimal values for PostgreSQL
architecture: standalone
""",
    "helm/redis/values.yaml": """# Minimal values for Redis
architecture: standalone
""",
    "helm/longhorn/values.yaml": """# Minimal values for Longhorn
persistence:
  defaultClassReplicaCount: 2
"""
}

dirs_to_create = [
    "docs",
    "docs/prompts",
    "diagrams",
    "adr",
    "notes",
    "scripts/bootstrap",
    "scripts/proxmox",
    "scripts/k3s",
    "scripts/ops",
    "inventory",
    "k8s/base/namespaces",
    "k8s/base/ingress",
    "k8s/base/rbac",
    "k8s/base/storage",
    "k8s/base/certs",
    "k8s/observability/metrics-server",
    "k8s/observability/prometheus",
    "k8s/observability/grafana",
    "k8s/observability/loki",
    "k8s/observability/promtail",
    "k8s/gitops/argocd",
    "k8s/gitops/applications",
    "k8s/gitops/app-of-apps",
    "k8s/storage/local-path",
    "k8s/storage/longhorn",
    "k8s/storage/pvc-examples",
    "k8s/apps/headlamp",
    "k8s/apps/nextcloud",
    "k8s/apps/n8n",
    "k8s/apps/postgresql",
    "k8s/apps/redis",
    "k8s/apps/ai",
    "k8s/apps/demo",
    "k8s/environments/lab",
    "k8s/environments/future",
    "helm/headlamp",
    "helm/prometheus-stack",
    "helm/loki",
    "helm/argocd",
    "helm/nextcloud",
    "helm/n8n",
    "helm/postgresql",
    "helm/redis",
    "helm/longhorn",
    ".github/workflows"
]

gitkeeps = [
    "scripts/bootstrap/.gitkeep",
    "scripts/proxmox/.gitkeep",
    "scripts/k3s/.gitkeep",
    "scripts/ops/.gitkeep",
    "k8s/storage/local-path/.gitkeep",
    "k8s/storage/longhorn/.gitkeep",
    "k8s/storage/pvc-examples/.gitkeep",
    "k8s/environments/lab/.gitkeep",
    "k8s/environments/future/.gitkeep",
    ".github/workflows/.gitkeep"
]

created = []
skipped = []

# ensure root exists
if not os.path.exists(root):
    os.makedirs(root)

for d in dirs_to_create:
    dp = os.path.join(root, d)
    if not os.path.exists(dp):
        os.makedirs(dp)

for gk in gitkeeps:
    fp = os.path.join(root, gk)
    if not os.path.exists(fp) or os.path.getsize(fp) == 0:
        with open(fp, "w") as f:
            f.write("")
        created.append(gk)
    else:
        skipped.append(gk)

for fpath, content in files_to_create.items():
    fp = os.path.join(root, fpath)
    if not os.path.exists(fp) or os.path.getsize(fp) == 0:
        with open(fp, "w", encoding='utf-8') as f:
            f.write(content)
        created.append(fpath)
    else:
        skipped.append(fpath)

print("Created files:")
for f in sorted(created): print(f"  + {f}")
print("\\nSkipped files (already exist and not empty):")
for f in sorted(skipped): print(f"  - {f}")

def display_tree(start_path, prefix=''):
    contents = sorted(os.listdir(start_path))
    pointers = ['+-- '] * (len(contents) - 1) + ['\\--- ']
    for pointer, name in zip(pointers, contents):
        if name in ['.git', '.vscode', '.idea']:
            continue
        print(prefix + pointer + name)
        path = os.path.join(start_path, name)
        if os.path.isdir(path):
            extension = '|   ' if pointer == '+-- ' else '    '
            display_tree(path, prefix=prefix + extension)

print("\\nFinal Tree:")
print(os.path.basename(root) + "/")
display_tree(root)
