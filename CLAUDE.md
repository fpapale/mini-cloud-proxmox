# Mini Cloud Proxmox Workspace Bootstrap Instructions

You are acting as a senior platform architect and repository bootstrap agent.

Your job is to initialize and maintain a workspace for a project called `mini-cloud-proxmox`.

## Mission

Create a clean, structured, implementation-ready workspace for a home mini-cloud running on Proxmox with a Kubernetes cluster based on K3s.

The workspace must support both:
1. architecture/design work
2. future implementation artifacts

This project is a home lab / mini-cloud with the following target stack:

- Proxmox VE as hypervisor
- K3s as Kubernetes distribution
- Preferred topology: 1 VM for control plane + 2 LXC/CT workers
- Traefik as ingress controller
- Headlamp as Kubernetes web dashboard
- Metrics Server
- Prometheus + Grafana
- Loki + Promtail
- Argo CD
- Nextcloud
- n8n
- PostgreSQL
- Redis
- Optional AI services such as Ollama / Open WebUI
- Optional distributed storage such as Longhorn in a later phase

The workspace must be organized to host:
- architecture documents
- diagrams
- ADRs
- Kubernetes manifests
- Helm values files
- GitOps app definitions
- observability configs
- storage configs
- scripts
- notes and backlog items

---

## Operating rules

1. Be idempotent.
   - If the structure already exists, do not destroy it.
   - Create missing files and folders only.
   - If a file exists and is non-empty, preserve it unless explicitly asked to update it.
   - Never delete existing user content unless explicitly instructed.

2. Be conservative.
   - Do not install software packages on the host machine unless explicitly requested.
   - Do not run destructive shell commands.
   - Do not modify global system configuration.
   - Limit yourself to preparing the project workspace structure and initial scaffold files.

3. Be practical.
   - Optimize for maintainability and clarity, not enterprise overkill.
   - Use simple, readable Markdown and YAML stubs.
   - Add brief comments in placeholder files where useful.

4. Keep the workspace implementation-ready.
   - Create folders and starter files that can later be used directly for Kubernetes manifests, Helm values, GitOps applications, diagrams, and architecture documentation.

---

## Root directory to create

Create this root folder if it does not already exist:

`mini-cloud-proxmox/`

All files and folders must live under this root.

---

## Required directory tree

Create the following structure under `mini-cloud-proxmox`:

mini-cloud-proxmox/
├─ README.md
├─ .gitignore
├─ docs/
│  ├─ architecture.md
│  ├─ topology.md
│  ├─ networking.md
│  ├─ storage-strategy.md
│  ├─ exposure-strategy.md
│  ├─ observability.md
│  ├─ gitops-strategy.md
│  ├─ implementation-roadmap.md
│  ├─ bom-sizing.md
│  └─ risk-register.md
├─ diagrams/
│  ├─ README.md
│  ├─ mini-cloud-architecture.mmd
│  ├─ network-flows.mmd
│  └─ namespaces.mmd
├─ adr/
│  ├─ README.md
│  ├─ ADR-001-topology.md
│  ├─ ADR-002-k3s-choice.md
│  ├─ ADR-003-storage-strategy.md
│  ├─ ADR-004-ingress-exposure.md
│  └─ ADR-005-observability-stack.md
├─ notes/
│  ├─ backlog.md
│  ├─ ideas.md
│  └─ lab-experiments.md
├─ scripts/
│  ├─ README.md
│  ├─ bootstrap/
│  │  └─ .gitkeep
│  ├─ proxmox/
│  │  └─ .gitkeep
│  ├─ k3s/
│  │  └─ .gitkeep
│  └─ ops/
│     └─ .gitkeep
├─ inventory/
│  ├─ README.md
│  ├─ nodes.md
│  ├─ ips.md
│  └─ resources.md
├─ k8s/
│  ├─ README.md
│  ├─ base/
│  │  ├─ namespaces/
│  │  │  └─ .gitkeep
│  │  ├─ ingress/
│  │  │  └─ .gitkeep
│  │  ├─ rbac/
│  │  │  └─ .gitkeep
│  │  ├─ storage/
│  │  │  └─ .gitkeep
│  │  └─ certs/
│  │     └─ .gitkeep
│  ├─ observability/
│  │  ├─ metrics-server/
│  │  │  └─ .gitkeep
│  │  ├─ prometheus/
│  │  │  └─ .gitkeep
│  │  ├─ grafana/
│  │  │  └─ .gitkeep
│  │  ├─ loki/
│  │  │  └─ .gitkeep
│  │  └─ promtail/
│  │     └─ .gitkeep
│  ├─ gitops/
│  │  ├─ argocd/
│  │  │  └─ .gitkeep
│  │  ├─ applications/
│  │  │  └─ .gitkeep
│  │  └─ app-of-apps/
│  │     └─ .gitkeep
│  ├─ storage/
│  │  ├─ local-path/
│  │  │  └─ .gitkeep
│  │  ├─ longhorn/
│  │  │  └─ .gitkeep
│  │  └─ pvc-examples/
│  │     └─ .gitkeep
│  ├─ apps/
│  │  ├─ headlamp/
│  │  │  └─ .gitkeep
│  │  ├─ nextcloud/
│  │  │  └─ .gitkeep
│  │  ├─ n8n/
│  │  │  └─ .gitkeep
│  │  ├─ postgresql/
│  │  │  └─ .gitkeep
│  │  ├─ redis/
│  │  │  └─ .gitkeep
│  │  ├─ ai/
│  │  │  └─ .gitkeep
│  │  └─ demo/
│  │     └─ .gitkeep
│  └─ environments/
│     ├─ lab/
│     │  └─ .gitkeep
│     └─ future/
│        └─ .gitkeep
├─ helm/
│  ├─ README.md
│  ├─ repositories.md
│  ├─ headlamp/
│  │  └─ values.yaml
│  ├─ prometheus-stack/
│  │  └─ values.yaml
│  ├─ loki/
│  │  └─ values.yaml
│  ├─ argocd/
│  │  └─ values.yaml
│  ├─ nextcloud/
│  │  └─ values.yaml
│  ├─ n8n/
│  │  └─ values.yaml
│  ├─ postgresql/
│  │  └─ values.yaml
│  ├─ redis/
│  │  └─ values.yaml
│  └─ longhorn/
│     └─ values.yaml
└─ .github/
   └─ workflows/
      └─ .gitkeep

---

## Files to initialize with meaningful starter content

Create these files with short but useful initial content:

### 1. `README.md`
Include:
- project title
- purpose of the mini-cloud
- target topology
- target services
- phases of implementation
- short repository map

### 2. `docs/architecture.md`
Include:
- executive summary
- architecture layers:
  - Proxmox layer
  - VM/CT layout
  - K3s cluster layer
  - ingress layer
  - observability layer
  - GitOps layer
  - apps/data layer
- note that AI and Longhorn are optional later phases

### 3. `docs/topology.md`
Include:
- preferred topology: 1 control-plane VM + 2 CT workers
- trade-offs of CT workers
- fallback option: all-VM if CT limitations appear

### 4. `docs/networking.md`
Include:
- north-south traffic
- east-west traffic
- admin/management traffic
- example hostnames:
  - headlamp.lab
  - grafana.lab
  - argocd.lab
  - nextcloud.lab
  - n8n.lab

### 5. `docs/storage-strategy.md`
Include:
- phase 1: local-path/default storage
- phase 2: persistent services
- phase 3: Longhorn optional
- pros/cons summary

### 6. `docs/exposure-strategy.md`
Include:
- local-only lab exposure first
- hosts file / local DNS approach
- which services should be internal-only
- HTTPS/cert-manager as later phase

### 7. `docs/observability.md`
Include:
- Metrics Server
- Prometheus
- Grafana
- Loki
- Promtail
- what each does

### 8. `docs/gitops-strategy.md`
Include:
- why Argo CD
- separation between infra and apps
- suggested future app-of-apps model

### 9. `docs/implementation-roadmap.md`
Include phases:
- Phase 0: Proxmox base prep
- Phase 1: K3s bootstrap
- Phase 2: dashboard + observability
- Phase 3: GitOps
- Phase 4: useful apps
- Phase 5: hardening, backups, optional AI/storage expansion

### 10. `docs/bom-sizing.md`
Include three sizing tiers:
- minimum viable
- recommended
- expanded with AI
Add placeholder tables.

### 11. `docs/risk-register.md`
Include a table with these risks:
- CT/LXC limitations
- resource contention
- ingress exposure
- storage fragility
- secrets handling
- backup gaps

### 12. `diagrams/mini-cloud-architecture.mmd`
Create a starter Mermaid diagram showing:
- user/browser
- Proxmox
- control-plane VM
- 2 CT workers
- K3s cluster
- Traefik
- Headlamp
- Prometheus/Grafana
- Loki
- Argo CD
- Apps
- Storage

### 13. `diagrams/network-flows.mmd`
Create a basic Mermaid flow diagram for:
- admin traffic
- ingress traffic
- internal cluster traffic

### 14. `diagrams/namespaces.mmd`
Create a Mermaid diagram for suggested namespaces:
- ingress
- observability
- gitops
- storage
- apps
- databases
- ai
- demo

### 15. ADR files
Initialize each ADR with:
- title
- status: proposed
- context
- decision
- consequences

### 16. `notes/lab-experiments.md`
Initialize with a checklist of learning experiments such as:
- pod self-healing
- node failure simulation
- rolling update
- rollback
- ingress routing
- PVC persistence
- node drain
- scaling

### 17. `inventory/nodes.md`
Create a starter table for:
- node name
- type (VM/CT)
- role
- CPU
- RAM
- disk
- IP

### 18. `inventory/ips.md`
Create a starter placeholder table for IP planning.

### 19. `inventory/resources.md`
Create a starter resource budgeting file.

### 20. `helm/repositories.md`
Add a placeholder list of future Helm repositories for:
- headlamp
- prometheus-community
- grafana
- argo
- bitnami
- nextcloud
- longhorn

### 21. `helm/*/values.yaml`
For each chart values file, create a minimal commented placeholder YAML, not a full real config yet.

---

## Content style

Use:
- concise, clean Markdown
- practical wording
- implementation-oriented structure
- no unnecessary verbosity

---

## Git ignore

Create a `.gitignore` suitable for a repo containing:
- editor temp files
- OS temp files
- local kubeconfigs
- secrets files
- `.env`
- generated archives

---

## Final task after scaffold creation

After creating the structure and starter files:

1. Print a concise summary of what was created.
2. Print the final tree.
3. Highlight any files that were skipped because they already existed.
4. Do not invent missing production configs yet.
5. Do not populate secrets.
6. Do not run Kubernetes commands unless explicitly requested.

---

## Success criteria

The workspace is considered successfully bootstrapped when:
- the full folder structure exists
- all required starter files exist
- the Markdown files contain meaningful initial scaffolding
- the Mermaid files contain valid starter diagrams
- the repository is ready for future architecture and implementation work

## Implementation-Ready Scaffold Extension

In addition to the base workspace bootstrap, extend the repository with implementation-ready starter artifacts.

### Extension goal

Prepare the `mini-cloud-proxmox` workspace not only as a documentation/design repository, but also as an initial executable scaffold for future Kubernetes deployment work.

The extension must remain:
- idempotent
- non-destructive
- conservative
- compatible with the existing repository structure already created

If files already exist:
- preserve non-empty files
- create only missing files
- if a placeholder file exists and is nearly empty, enrich it only if explicitly asked
- never overwrite user-authored content unless explicitly requested

---

### Additional folders and files to ensure exist

Under `mini-cloud-proxmox/`, ensure these files also exist if missing:

k8s/
├─ base/
│  ├─ namespaces/
│  │  ├─ namespaces.yaml
│  │  └─ kustomization.yaml
│  ├─ ingress/
│  │  ├─ whoami-ingress.yaml
│  │  └─ kustomization.yaml
│  ├─ rbac/
│  │  └─ README.md
│  ├─ storage/
│  │  ├─ pvc-demo.yaml
│  │  └─ kustomization.yaml
│  └─ certs/
│     └─ README.md
├─ apps/
│  ├─ demo/
│  │  ├─ whoami-deployment.yaml
│  │  ├─ whoami-service.yaml
│  │  ├─ whoami-ingress.yaml
│  │  └─ kustomization.yaml
│  ├─ headlamp/
│  │  └─ README.md
│  ├─ nextcloud/
│  │  └─ README.md
│  ├─ n8n/
│  │  └─ README.md
│  ├─ postgresql/
│  │  └─ README.md
│  ├─ redis/
│  │  └─ README.md
│  └─ ai/
│     └─ README.md
├─ gitops/
│  ├─ argocd/
│  │  ├─ namespace.yaml
│  │  ├─ install-notes.md
│  │  └─ kustomization.yaml
│  ├─ applications/
│  │  ├─ root-app.yaml
│  │  ├─ observability-app.yaml
│  │  ├─ demo-app.yaml
│  │  └─ apps-app.yaml
│  └─ app-of-apps/
│     └─ README.md
└─ observability/
   ├─ metrics-server/
   │  └─ README.md
   ├─ prometheus/
   │  └─ README.md
   ├─ grafana/
   │  └─ README.md
   ├─ loki/
   │  └─ README.md
   └─ promtail/
      └─ README.md

helm/
├─ headlamp/
│  └─ values.yaml
├─ prometheus-stack/
│  └─ values.yaml
├─ loki/
│  └─ values.yaml
├─ argocd/
│  └─ values.yaml
├─ nextcloud/
│  └─ values.yaml
├─ n8n/
│  └─ values.yaml
├─ postgresql/
│  └─ values.yaml
├─ redis/
│  └─ values.yaml
└─ longhorn/
   └─ values.yaml

---

### Additional starter artifacts to create

Create the following minimal starter manifests and notes if they do not already exist.

#### 1. `k8s/base/namespaces/namespaces.yaml`
Create Kubernetes Namespace manifests for:
- ingress
- observability
- gitops
- storage
- apps
- databases
- ai
- demo

#### 2. `k8s/base/namespaces/kustomization.yaml`
Reference `namespaces.yaml`.

#### 3. `k8s/apps/demo/whoami-deployment.yaml`
Create a minimal Deployment for a lightweight demo app such as `traefik/whoami` with 2 replicas.

#### 4. `k8s/apps/demo/whoami-service.yaml`
Create a ClusterIP Service exposing the demo app on port 80.

#### 5. `k8s/apps/demo/whoami-ingress.yaml`
Create a sample Ingress using `traefik` ingressClassName and host `whoami.lab`.

#### 6. `k8s/apps/demo/kustomization.yaml`
Reference the demo deployment, service, and ingress.

#### 7. `k8s/base/storage/pvc-demo.yaml`
Create a very small sample PVC for lab demonstration purposes.

#### 8. `k8s/base/storage/kustomization.yaml`
Reference `pvc-demo.yaml`.

#### 9. `k8s/gitops/argocd/namespace.yaml`
Create an Argo CD namespace manifest for `argocd` or `gitops` depending on the chosen naming convention, and explain the choice in comments if needed.

#### 10. `k8s/gitops/applications/root-app.yaml`
Create a starter Argo CD Application manifest placeholder following an app-of-apps approach.
Do not invent a real repo URL; use obvious placeholders and comments.

#### 11. `k8s/gitops/applications/observability-app.yaml`
Create a placeholder Argo CD Application manifest pointing to the observability path.

#### 12. `k8s/gitops/applications/demo-app.yaml`
Create a placeholder Argo CD Application manifest pointing to the demo app path.

#### 13. `k8s/gitops/applications/apps-app.yaml`
Create a placeholder Argo CD Application manifest pointing to the apps path.

#### 14. `helm/*/values.yaml`
For each chart values file, upgrade the placeholder so that it contains:
- a short header comment
- namespace field if relevant
- ingress enabled/disabled example if relevant
- persistence section if relevant
- resources section placeholder
- notes that values are intentionally minimal and non-production

Do not generate fully production-ready values yet.

---

### Kustomize support

Where relevant, add minimal `kustomization.yaml` files so that the repository can evolve toward a Kustomize-friendly structure.

At minimum:
- `k8s/base/namespaces/kustomization.yaml`
- `k8s/base/ingress/kustomization.yaml`
- `k8s/base/storage/kustomization.yaml`
- `k8s/apps/demo/kustomization.yaml`
- `k8s/gitops/argocd/kustomization.yaml`

These files should be minimal and valid.

---

### README/notes enrichment

If missing, create or enrich the following README files with concise implementation-oriented guidance:

- `k8s/README.md`
- `scripts/README.md`
- `inventory/README.md`
- `k8s/apps/headlamp/README.md`
- `k8s/apps/nextcloud/README.md`
- `k8s/apps/n8n/README.md`
- `k8s/apps/postgresql/README.md`
- `k8s/apps/redis/README.md`
- `k8s/apps/ai/README.md`
- `k8s/observability/*/README.md`

Each should explain:
- purpose
- expected future contents
- whether the component is phase 1, phase 2, or optional/later

---

### Constraints for starter manifests

All starter manifests must:
- be valid YAML
- be intentionally minimal
- include short comments where useful
- avoid secrets
- avoid real credentials
- avoid hardcoded production domains
- avoid pretending to be fully production-ready
- use obvious placeholders where needed

---

### Final behavior for extension tasks

When executing this extension:
1. Create only missing folders/files.
2. Preserve existing user-authored content.
3. Print a summary of:
   - newly created files
   - skipped existing files
   - files left intentionally as placeholders
4. Show the updated tree.
5. Do not run cluster commands unless explicitly requested.