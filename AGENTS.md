# Mini Cloud Proxmox - Repository Bootstrap and Scaffold Rules

You are acting as a senior platform architect, repository bootstrap agent, and implementation scaffold assistant.

Your job is to initialize, extend, and maintain a workspace for a project called `mini-cloud-proxmox`.

## Mission

Create and maintain a clean, structured, implementation-ready workspace for a home mini-cloud running on Proxmox with a Kubernetes cluster based on K3s.

The repository must support both:
1. architecture and design work
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

The repository must be organized to host:
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

## Operating Rules

1. Be idempotent.
   - If the structure already exists, do not destroy it.
   - Create missing files and folders only.
   - If a file exists and is non-empty, preserve it unless explicitly asked to update it.
   - Never delete existing user content unless explicitly instructed.

2. Be conservative.
   - Do not install software packages on the host machine unless explicitly requested.
   - Do not run destructive shell commands.
   - Do not modify global system configuration.
   - Limit yourself to preparing the project workspace structure and starter scaffold files unless the user explicitly asks for implementation or execution.

3. Be practical.
   - Optimize for maintainability and clarity, not enterprise overkill.
   - Use simple, readable Markdown and YAML stubs.
   - Add brief comments in placeholder files where useful.

4. Keep the repository implementation-ready.
   - Create folders and starter files that can later be used directly for Kubernetes manifests, Helm values, GitOps applications, diagrams, and architecture documentation.

5. Prefer preserving user-authored work.
   - If a file is already meaningful, do not rewrite it.
   - If a placeholder file exists and is almost empty, enrich it only if explicitly asked.
   - When in doubt, skip and report.

---

## Root Directory

Create this root folder if it does not already exist:

`mini-cloud-proxmox/`

All files and folders must live under this root.

---

## Required Directory Tree

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
│  │  │  ├─ namespaces.yaml
│  │  │  └─ kustomization.yaml
│  │  ├─ ingress/
│  │  │  ├─ whoami-ingress.yaml
│  │  │  └─ kustomization.yaml
│  │  ├─ rbac/
│  │  │  └─ README.md
│  │  ├─ storage/
│  │  │  ├─ pvc-demo.yaml
│  │  │  └─ kustomization.yaml
│  │  └─ certs/
│  │     └─ README.md
│  ├─ observability/
│  │  ├─ metrics-server/
│  │  │  └─ README.md
│  │  ├─ prometheus/
│  │  │  └─ README.md
│  │  ├─ grafana/
│  │  │  └─ README.md
│  │  ├─ loki/
│  │  │  └─ README.md
│  │  └─ promtail/
│  │     └─ README.md
│  ├─ gitops/
│  │  ├─ argocd/
│  │  │  ├─ namespace.yaml
│  │  │  ├─ install-notes.md
│  │  │  └─ kustomization.yaml
│  │  ├─ applications/
│  │  │  ├─ root-app.yaml
│  │  │  ├─ observability-app.yaml
│  │  │  ├─ demo-app.yaml
│  │  │  └─ apps-app.yaml
│  │  └─ app-of-apps/
│  │     └─ README.md
│  ├─ storage/
│  │  ├─ local-path/
│  │  │  └─ .gitkeep
│  │  ├─ longhorn/
│  │  │  └─ .gitkeep
│  │  └─ pvc-examples/
│  │     └─ .gitkeep
│  ├─ apps/
│  │  ├─ headlamp/
│  │  │  └─ README.md
│  │  ├─ nextcloud/
│  │  │  └─ README.md
│  │  ├─ n8n/
│  │  │  └─ README.md
│  │  ├─ postgresql/
│  │  │  └─ README.md
│  │  ├─ redis/
│  │  │  └─ README.md
│  │  ├─ ai/
│  │  │  └─ README.md
│  │  └─ demo/
│  │     ├─ whoami-deployment.yaml
│  │     ├─ whoami-service.yaml
│  │     ├─ whoami-ingress.yaml
│  │     └─ kustomization.yaml
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

## Files To Initialize With Meaningful Starter Content

Create these files with short but useful initial content if they are missing.

### `README.md`
Include:
- project title
- purpose of the mini-cloud
- target topology
- target services
- phases of implementation
- short repository map
- a section called `How to bootstrap this repo with Antigravity`
- a section called `Parameters to customize before real deployment`

### `docs/architecture.md`
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

### `docs/topology.md`
Include:
- preferred topology: 1 control-plane VM + 2 CT workers
- trade-offs of CT workers
- fallback option: all-VM if CT limitations appear

### `docs/networking.md`
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

### `docs/storage-strategy.md`
Include:
- phase 1: local-path/default storage
- phase 2: persistent services
- phase 3: Longhorn optional
- pros/cons summary

### `docs/exposure-strategy.md`
Include:
- local-only lab exposure first
- hosts file / local DNS approach
- which services should be internal-only
- HTTPS/cert-manager as later phase

### `docs/observability.md`
Include:
- Metrics Server
- Prometheus
- Grafana
- Loki
- Promtail
- what each does

### `docs/gitops-strategy.md`
Include:
- why Argo CD
- separation between infra and apps
- suggested future app-of-apps model

### `docs/implementation-roadmap.md`
Include phases:
- Phase 0: Proxmox base prep
- Phase 1: K3s bootstrap
- Phase 2: dashboard + observability
- Phase 3: GitOps
- Phase 4: useful apps
- Phase 5: hardening, backups, optional AI/storage expansion

### `docs/bom-sizing.md`
Include three sizing tiers:
- minimum viable
- recommended
- expanded with AI
Add placeholder tables.

### `docs/risk-register.md`
Include a table with these risks:
- CT/LXC limitations
- resource contention
- ingress exposure
- storage fragility
- secrets handling
- backup gaps

### `diagrams/mini-cloud-architecture.mmd`
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

### `diagrams/network-flows.mmd`
Create a basic Mermaid flow diagram for:
- admin traffic
- ingress traffic
- internal cluster traffic

### `diagrams/namespaces.mmd`
Create a Mermaid diagram for suggested namespaces:
- ingress
- observability
- gitops
- storage
- apps
- databases
- ai
- demo

### ADR files
Initialize each ADR with:
- title
- status: proposed
- context
- decision
- consequences

### `notes/lab-experiments.md`
Initialize with a checklist of learning experiments such as:
- pod self-healing
- node failure simulation
- rolling update
- rollback
- ingress routing
- PVC persistence
- node drain
- scaling

### `inventory/nodes.md`
Create a starter table for:
- node name
- type (VM/CT)
- role
- CPU
- RAM
- disk
- IP

### `inventory/ips.md`
Create a starter placeholder table for IP planning.

### `inventory/resources.md`
Create a starter resource budgeting file.

### `helm/repositories.md`
Add a placeholder list of future Helm repositories for:
- headlamp
- prometheus-community
- grafana
- argo
- bitnami
- nextcloud
- longhorn

### `helm/*/values.yaml`
For each chart values file, create a minimal commented placeholder YAML, not a full real config yet.

---

## Additional Starter Artifacts To Create

Create the following minimal starter manifests and notes if they do not already exist.

### `k8s/base/namespaces/namespaces.yaml`
Create Kubernetes Namespace manifests for:
- ingress
- observability
- gitops
- storage
- apps
- databases
- ai
- demo

### `k8s/base/namespaces/kustomization.yaml`
Reference `namespaces.yaml`.

### `k8s/apps/demo/whoami-deployment.yaml`
Create a minimal Deployment for `traefik/whoami` with 2 replicas.

### `k8s/apps/demo/whoami-service.yaml`
Create a ClusterIP Service exposing the demo app on port 80.

### `k8s/apps/demo/whoami-ingress.yaml`
Create a sample Ingress using `traefik` as `ingressClassName` and host `whoami.lab`.

### `k8s/apps/demo/kustomization.yaml`
Reference the demo deployment, service, and ingress.

### `k8s/base/ingress/whoami-ingress.yaml`
Create a second simple ingress sample or a note explaining that demo ingress lives under app manifests. Keep it minimal and consistent.

### `k8s/base/ingress/kustomization.yaml`
Create a minimal valid kustomization file.

### `k8s/base/storage/pvc-demo.yaml`
Create a very small sample PVC for lab demonstration purposes.

### `k8s/base/storage/kustomization.yaml`
Reference `pvc-demo.yaml`.

### `k8s/gitops/argocd/namespace.yaml`
Create an Argo CD namespace manifest for `argocd` or `gitops` depending on the chosen naming convention, and explain the choice in comments if needed.

### `k8s/gitops/argocd/install-notes.md`
Add a short note explaining this folder is for install-related files and handoff to GitOps management later.

### `k8s/gitops/argocd/kustomization.yaml`
Create a minimal valid kustomization file.

### `k8s/gitops/applications/root-app.yaml`
Create a starter Argo CD Application manifest placeholder following an app-of-apps approach.
Do not invent a real repo URL; use obvious placeholders and comments.

### `k8s/gitops/applications/observability-app.yaml`
Create a placeholder Argo CD Application manifest pointing to the observability path.

### `k8s/gitops/applications/demo-app.yaml`
Create a placeholder Argo CD Application manifest pointing to the demo app path.

### `k8s/gitops/applications/apps-app.yaml`
Create a placeholder Argo CD Application manifest pointing to the apps path.

### `helm/*/values.yaml`
For each chart values file, ensure it contains:
- a short header comment
- namespace field if relevant
- ingress enabled/disabled example if relevant
- persistence section if relevant
- resources section placeholder
- notes that values are intentionally minimal and non-production

Do not generate fully production-ready values yet.

---

## Kustomize Support

Where relevant, add minimal `kustomization.yaml` files so that the repository can evolve toward a Kustomize-friendly structure.

At minimum:
- `k8s/base/namespaces/kustomization.yaml`
- `k8s/base/ingress/kustomization.yaml`
- `k8s/base/storage/kustomization.yaml`
- `k8s/apps/demo/kustomization.yaml`
- `k8s/gitops/argocd/kustomization.yaml`

These files should be minimal and valid.

---

## README And Notes Enrichment

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
- `k8s/observability/metrics-server/README.md`
- `k8s/observability/prometheus/README.md`
- `k8s/observability/grafana/README.md`
- `k8s/observability/loki/README.md`
- `k8s/observability/promtail/README.md`

Each should explain:
- purpose
- expected future contents
- whether the component is phase 1, phase 2, or optional/later

---

## Constraints For Starter Manifests

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

## Content Style

Use:
- concise, clean Markdown
- practical wording
- implementation-oriented structure
- no unnecessary verbosity

---

## Git Ignore

Create a `.gitignore` suitable for a repo containing:
- editor temp files
- OS temp files
- local kubeconfigs
- secrets files
- `.env`
- generated archives

---

## Parameters To Support In README

When generating `README.md`, include a section called `Parameters to customize before real deployment` with a small table covering at least:
- project root path
- workspace folder path
- cluster name
- control-plane hostname
- worker hostnames
- node type (VM/CT)
- IP subnet
- control-plane IP
- worker IPs
- local lab domain
- ingress hostnames
- storage mode
- Git repository URL placeholder
- Argo CD namespace choice
- optional AI enablement

Use placeholders and examples only.

---

## Final Behavior

When executing these rules:
1. Create only missing folders/files.
2. Preserve existing user-authored content.
3. Print a concise summary of:
   - newly created files
   - skipped existing files
   - files left intentionally as placeholders
4. Show the final tree.
5. Do not invent production secrets or credentials.
6. Do not run Kubernetes commands unless explicitly requested.
7. Treat the repository as already initialized if it exists; this may be an extension pass rather than a full regeneration.

---

## Success Criteria

The repository is considered successfully bootstrapped when:
- the full folder structure exists
- all required starter files exist
- the Markdown files contain meaningful initial scaffolding
- the Mermaid files contain valid starter diagrams
- the starter YAML manifests are valid and intentionally minimal
- the repository is ready for future architecture and implementation work