# Mini Cloud Proxmox

## Scopo del Progetto
Un mini-cloud per ambienti home lab basato su Proxmox VE con un cluster Kubernetes gestito tramite K3s. 
Il progetto è progettato per ospitare applicazioni infrastrutturali, database, servizi GitOps ed esperimenti di laboratorio in modo leggero e scalabile.

## Topologia di Riferimento
* **1x Hypervisor**: Proxmox VE
* **1x Control Plane (K3s Server)**: Macchina Virtuale (VM) per isolamento e stabilità del kernel.
* **2x Worker Nodes (K3s Agent)**: Linux Containers (CT/LXC) per ridurre l'overhead e massimizzare le prestazioni.

## Servizi Inclusi
* **Rete / Ingress**: Traefik (integrato in K3s)
* **Dashboard**: Headlamp
* **Osservabilità**: Prometheus + Grafana (Metriche), Loki + Promtail (Log)
* **GitOps**: Argo CD
* **App e Dati**: Nextcloud, n8n, PostgreSQL, Redis

---

## 🛠 Modalità di Installazione e Avvio Rapido

Questa sezione descrive nel dettaglio i passi necessari per effettuare il deployment dell'intero ambiente partendo da zero.

### Fase 0: Preparazione Ambiente Proxmox
1. **Configurazione Rete:** Assicurarsi di avere un bridge di rete in Proxmox dedicato o adeguato per i nodi K3s, con DHCP o IP statici pianificati in `inventory/ips.md`.
2. **Creazione Control Plane (VM):** Creare una VM (es. Debian 12) allocando 2+ vCPU e 2+ GB di RAM. Disabilitare lo swap.
3. **Creazione Nodi Worker (LXC):** Creare 2 container LXC (Debian/Ubuntu). **Importante:** Disabilitare lo swap e abilitare le opzioni `nesting` e `keyctl` nelle opzioni del container, necessarie per il corretto funzionamento dei container Kubernetes all'interno di LXC.

### Fase 1: Startup del Cluster K3s
1. Accedere SSH alla VM Control Plane ed installare K3s (Server):
   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
2. Estrarre il token di join del nodo master:
   ```bash
   cat /var/lib/rancher/k3s/server/node-token
   ```
3. Accedere tramite SSH ai nodi LXC Worker ed unirli al cluster (Agent):
   ```bash
   curl -sfL https://get.k3s.io | K3S_URL=https://<IP_CONTROL_PLANE>:6443 K3S_TOKEN=<TOKEN> sh -
   ```
4. Verificare i nodi dal Control Plane:
   ```bash
   kubectl get nodes
   ```

### Fase 2: Configurazione Storage Base
Di default, K3s include `local-path-provisioner`. Questo fornirà storage persistente legato al singolo nodo. 
- Usare questa classe di storage per database e servizi stateful in questa fase iniziale (configurazioni base in `k8s/storage/local-path/`).

### Fase 3: Dashboard e Osservabilità
Tutti i deployment infrastrutturali si trovano sotto `k8s/` e `helm/`.
1. **Headlamp (Dashboard Kubernetes):**
   ```bash
   kubectl apply -k k8s/apps/headlamp/
   ```
2. **Stack Prometheus & Loki:** Preparare ed applicare prima i namespace (`k8s/base/namespaces/`) e successivamente usare Helm con i file `values.yaml` personalizzati:
   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update
   # Deploy Prometheus Stack
   helm upgrade --install prometheus prometheus-community/kube-prometheus-stack -f helm/prometheus-stack/values.yaml -n observability
   ```

### Fase 4: GitOps con Argo CD
Il repository è progettato secondo i principi GitOps usando il pattern "App of Apps".
1. Installare Argo CD nel cluster:
   ```bash
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
   ```
2. Applicare l'App sorgente ("App of Apps") che punta alla specifica cartella di questo repository:
   ```bash
   kubectl apply -f k8s/gitops/app-of-apps/
   ```
3. Da questo momento, Argo CD monitorerà questo branch GitHub e riconcilierà lo stato nel cluster installando Nextcloud, n8n, Redis e Postgres automaticamente.

### Fase 5: Operazioni Post-Installazione e Utilizzo Lab
- **Esposizione:** Aggiungere nel proprio file `/etc/hosts` (o DNS locale) i domini locali:
  - `<IP_TRAEFIK_WORKER> argocd.lab nextcloud.lab n8n.lab grafana.lab`
- **Ripristini ed Upgrade:** Qualsiasi modifica architetturale deve passare in formato dichiarativo su questo repository git, garantendo l'idempotenza e la ricostruibilità del lab in Proxmox.

---

## Mappa del Repository
* `docs/` - Documenti di design e architettura.
* `adr/` - Architecture Decision Records (Scelte architetturali).
* `diagrams/` - Diagrammi Mermaid dell'architettura e network.
* `inventory/` - Inventario dei nodi e degli IP allocati.
* `k8s/` - Manifest Kubernetes organizzati per dominio.
* `helm/` - File customizzati `values.yaml` per deployment Helm complessi.
* `scripts/` - Script ausiliari e di automazione.


---
## How to bootstrap this repo with Antigravity

This repository is designed to be initialized and extended by an agent-driven workflow in Antigravity.

### Goal

Use Antigravity to create or extend the `mini-cloud-proxmox` repository structure without overwriting existing non-empty files.

### Before you start

Make sure:
- this repository is stored inside a local folder you can open as an Antigravity workspace
- `AGENTS.md` exists at the repository root
- `CLAUDE.md` and `GEMINI.md` are present if you want cross-agent compatibility
- you have reviewed the placeholder parameters in the section below

### Recommended Antigravity workspace setup

When opening Antigravity:
1. Create or open a workspace pointing to the parent folder that contains `mini-cloud-proxmox`
2. Open the repository in that workspace
3. Keep the agent in Planning mode for the first bootstrap pass
4. Use a review policy such as `Request Review` or `Agent decides`
5. Keep terminal execution conservative, ideally sandboxed, for repository bootstrap tasks
6. Do not ask the agent to run cluster installation commands during the repository bootstrap phase

### Recommended first prompt

Use one of these prompts in Antigravity:

#### First-time bootstrap
`Read AGENTS.md and bootstrap the mini-cloud-proxmox repository. Create the required folder tree and starter files on disk, preserve any existing non-empty files, and then show me the final tree plus created vs skipped files.`

#### Extension pass
`Read AGENTS.md and extend the existing mini-cloud-proxmox repository. Treat it as already initialized, create only missing folders/files, do not overwrite non-empty files, and then show me the updated tree plus created vs skipped files.`

### What the agent is expected to create

The agent should create:
- architecture and design documents
- diagrams and ADR files
- inventory and notes
- starter Kubernetes manifests
- starter Kustomize files
- Helm values placeholders
- GitOps placeholder applications
- implementation-oriented README files

### What the agent should NOT do during bootstrap

During repository bootstrap, the agent should not:
- install packages on the machine
- change global system configuration
- invent secrets or credentials
- run destructive shell commands
- apply Kubernetes manifests to a real cluster
- install K3s or Proxmox components unless explicitly requested later

### Parameters to customize before real deployment

Review and adjust these placeholders before using the repository for a real environment.

| Parameter | Example | Where to update |
|---|---|---|
| Project root path | `~/projects/mini-cloud-proxmox` | local folder / workspace |
| Workspace folder path | `~/projects` | Antigravity workspace selection |
| Cluster name | `mini-cloud-lab` | docs, inventory, future manifests |
| Control-plane hostname | `k3s-master` | `inventory/nodes.md`, future provisioning files |
| Worker 1 hostname | `k3s-worker-1` | `inventory/nodes.md` |
| Worker 2 hostname | `k3s-worker-2` | `inventory/nodes.md` |
| Control-plane node type | `VM` | `docs/topology.md`, inventory |
| Worker node type | `CT` | `docs/topology.md`, inventory |
| IP subnet | `192.168.50.0/24` | `docs/networking.md`, `inventory/ips.md` |
| Control-plane IP | `192.168.50.10` | inventory, future manifests |
| Worker 1 IP | `192.168.50.11` | inventory |
| Worker 2 IP | `192.168.50.12` | inventory |
| Local lab domain | `lab` or `lab.local` | ingress samples, docs |
| Demo ingress host | `whoami.lab` | `k8s/apps/demo/*.yaml` |
| Headlamp host | `headlamp.lab` | docs, future ingress |
| Grafana host | `grafana.lab` | docs, future ingress |
| Argo CD host | `argocd.lab` | docs, future ingress |
| Nextcloud host | `nextcloud.lab` | docs, future ingress |
| n8n host | `n8n.lab` | docs, future ingress |
| Storage mode | `local-path` | docs, storage files |
| Later storage mode | `longhorn` | docs, future Helm values |
| Git repository URL | `https://example.invalid/mini-cloud-proxmox.git` | Argo CD placeholders |
| Argo CD namespace | `argocd` or `gitops` | `k8s/gitops/*` |
| Optional AI enabled | `false` | docs and future app manifests |

### Where to put real values later

Use these locations when you move from placeholders to real configuration:
- `inventory/nodes.md` for node names, roles, and sizes
- `inventory/ips.md` for IP planning
- `docs/networking.md` for domain and traffic choices
- `docs/storage-strategy.md` for storage decisions
- `helm/*/values.yaml` for chart-specific settings
- `k8s/apps/*` for per-application manifests
- `k8s/gitops/applications/*` for Argo CD application definitions

### Suggested workflow after bootstrap

1. Bootstrap the repository structure
2. Review the generated tree
3. Fill in inventory and IP planning
4. Refine architecture and topology docs
5. Decide whether workers remain CT-based or move to VM
6. Start preparing real Helm values and manifests
7. Only after that, move to actual Proxmox and K3s installation steps

### Prompt to install
Read AGENTS.md and extend or bootstrap the current mini-cloud-proxmox repository. Treat the repository as already initialized if it exists. Create only missing folders and files, preserve all non-empty files, populate the requested starter content, and then show me the final tree plus created vs skipped files.

I parametri non li metti in un file separato all’inizio. Per questa fase li metti in tre posti:

README.md → tabella di riferimento iniziale
inventory/nodes.md e inventory/ips.md → dati reali di nodi e rete
helm/*/values.yaml e k8s/apps/* → valori tecnici reali quando passerai dall’architettura all’installazione
See `docs/prompts/antigravity-install-k3s.md` for the execution prompt used to install the cluster on the target nodes.