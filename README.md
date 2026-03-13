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
