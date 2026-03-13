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