# Antigravity prompt - K3s cluster installation

Use this prompt in Antigravity to install and validate the 3-node K3s cluster.

Important: read node addresses from `inventory/ips.md` and treat that file as the authoritative source for node IP resolution.

Read AGENTS.md and use it as the repository source of truth.

Act as a cautious platform engineer. Your task is to install and validate a 3-node K3s cluster for the existing `mini-cloud-proxmox` project, using the repository structure and preserving idempotency.

This is a real installation task, not just a documentation task.

## Execution mode

- Treat this as an execution pass, not a scaffold-only pass.
- Be idempotent where possible.
- Preserve existing repo files unless an update is needed and safe.
- Prefer configuration files over ephemeral shell flags.
- Never invent secrets or credentials.
- Never store kubeconfig or tokens inside the git-tracked repository.
- Ask for review before any risky or destructive action.
- If a prerequisite is missing, stop and report clearly.

## Required access assumptions

You must be able to reach the target nodes through SSH from the current Antigravity environment or through an available tool/connector.
If SSH or remote access is not available, stop immediately and report what is missing.

## User-supplied parameters

Use these values unless the repository already contains clearer real values.

Primary source of truth for node addresses:
- `inventory/ips.md`

Secondary source of truth for node naming, roles, and topology:
- `inventory/nodes.md`
- `docs/topology.md`
- `docs/networking.md`

Read node IPs from `inventory/ips.md` first.
If `inventory/ips.md` contains valid node address information, prefer those values over inline prompt defaults.
Use inline defaults only as a fallback when `inventory/ips.md` is missing or incomplete.

PARAM_CLUSTER_NAME="mini-cloud-lab"
PARAM_DOMAIN="lab"
PARAM_K3S_VERSION=""                  # empty = stable channel
PARAM_K3S_CHANNEL="stable"

PARAM_ADMIN_USER="YOUR_SSH_USER"
PARAM_SSH_KEY_PATH="~/.ssh/id_ed25519"

PARAM_PROXMOX_HOST=""                 # optional, only if available for CT verification
PARAM_PROXMOX_SSH_USER="root"
PARAM_CT_WORKER1_ID=""                # optional
PARAM_CT_WORKER2_ID=""                # optional

PARAM_SERVER_HOSTNAME="k3s-master"
PARAM_WORKER1_HOSTNAME="k3s-worker-1"
PARAM_WORKER2_HOSTNAME="k3s-worker-2"

PARAM_SERVER_IP_DEFAULT="192.168.50.10"
PARAM_WORKER1_IP_DEFAULT="192.168.50.11"
PARAM_WORKER2_IP_DEFAULT="192.168.50.12"

PARAM_NODE1_TYPE="VM"                 # VM or CT
PARAM_NODE2_TYPE="CT"
PARAM_NODE3_TYPE="CT"

PARAM_POD_CIDR="10.42.0.0/16"
PARAM_SERVICE_CIDR="10.43.0.0/16"

PARAM_ARGOCD_NAMESPACE="argocd"

PARAM_ENABLE_BASE_MANIFESTS="true"
PARAM_ENABLE_HELM="true"
PARAM_ENABLE_METRICS_SERVER="true"
PARAM_ENABLE_HEADLAMP="true"
PARAM_ENABLE_OBSERVABILITY="false"
PARAM_ENABLE_ARGOCD="false"

PARAM_ENABLE_NEXTCLOUD="false"
PARAM_ENABLE_N8N="false"
PARAM_ENABLE_POSTGRESQL="false"
PARAM_ENABLE_REDIS="false"
PARAM_ENABLE_AI="false"
PARAM_ENABLE_LONGHORN="false"

PARAM_HEADLAMP_HOST="headlamp.lab"
PARAM_GRAFANA_HOST="grafana.lab"
PARAM_ARGOCD_HOST="argocd.lab"
PARAM_WHOAMI_HOST="whoami.lab"
PARAM_NEXTCLOUD_HOST="nextcloud.lab"
PARAM_N8N_HOST="n8n.lab"

## High-level goals

1. Verify prerequisites and connectivity.
2. Verify or infer the final node plan from the repository.
3. Prepare the three Linux nodes for K3s.
4. Install K3s server on the control-plane node.
5. Join the two worker nodes as agents.
6. Validate the cluster.
7. Install Helm on the server/admin node if missing.
8. Apply repository base manifests if enabled.
9. Install the selected core platform components into the cluster.
10. Produce a precise final report with created/updated files, commands run, validation output, and next manual steps.

## Phase 1 - Repository and parameter resolution

1. Read:
   - AGENTS.md
   - README.md
   - inventory/nodes.md
   - inventory/ips.md
   - docs/networking.md
   - docs/topology.md

2. Treat `inventory/ips.md` as the primary source of truth for node IP addresses.

3. Parse `inventory/ips.md` and resolve, at minimum:
   - control-plane hostname
   - control-plane IP
   - worker-1 hostname
   - worker-1 IP
   - worker-2 hostname
   - worker-2 IP

4. Use `inventory/nodes.md` and `docs/topology.md` to confirm:
   - node roles
   - node types (VM or CT)
   - intended topology

5. Resolution priority must be:
   1. `inventory/ips.md` for node IPs
   2. `inventory/nodes.md` for node names and roles
   3. `docs/topology.md` and `docs/networking.md` for supporting context
   4. inline `PARAM_*_DEFAULT` values only as a last fallback

6. If `inventory/ips.md` is missing, malformed, or does not clearly identify all 3 nodes, stop and report exactly what is missing.
   Do not guess node IPs if the repository is expected to contain them.

7. Print the effective installation plan before making changes, including:
   - resolved hostnames
   - resolved IP addresses
   - resolved node types
   - detected source of each value

### Expected `inventory/ips.md` structure

- a Markdown table or clearly structured list
- one row/item per node
- fields should include, if available:
  - node name
  - hostname
  - role
  - type
  - IP address

Example acceptable structure:

| node_name | hostname      | role          | type | ip            |
|-----------|---------------|---------------|------|---------------|
| node-1    | k3s-master    | control-plane | VM   | 192.168.50.10 |
| node-2    | k3s-worker-1  | worker        | CT   | 192.168.50.11 |
| node-3    | k3s-worker-2  | worker        | CT   | 192.168.50.12 |

If the file uses a different but unambiguous format, parse it conservatively.
If it is ambiguous, stop and report.

## Phase 2 - Remote access preflight

Before testing connectivity, print the resolved node/IP mapping extracted from `inventory/ips.md`.
If the mapping is ambiguous, stop before attempting SSH.

1. Verify that SSH to all three nodes works using the resolved user and key.
2. Verify host reachability with ping and a simple SSH command.
3. Verify that the three nodes have unique hostnames.
4. Verify the target nodes are modern Linux systems suitable for K3s.
5. Check for:
   - hostname
   - IP address
   - OS release
   - systemd
   - cgroups
   - available disk
   - available memory
   - swap status
   - time sync status if easy to verify
6. If workers are CTs and PARAM_PROXMOX_HOST plus CT IDs are provided:
   - SSH to the Proxmox host
   - inspect `pct config <CTID>` for both worker CTs
   - verify `features: nesting=1,keyctl=1` or equivalent effective configuration
   - do not change Proxmox CT config automatically unless explicitly approved
   - if missing, stop and report exactly what must be fixed on Proxmox

## Phase 3 - OS preparation on all nodes

On all three nodes:
1. Update package metadata.
2. Install only minimal required utilities if missing:
   - curl
   - ca-certificates
   - sudo
   - jq
   - vim or nano
3. Disable swap for the current session if enabled.
4. If persistent swap disable is needed, do it conservatively and back up any modified config file first.
5. Ensure `/etc/hosts` contains the three node mappings.
6. Ensure the final hostnames match the effective plan.
7. Do not install Docker.

If a firewall service is active and blocks cluster traffic, report it and request review before changing firewall rules.

## Phase 4 - K3s configuration files

Prefer configuration files over long install commands.

### On the server node

Create or update:
`/etc/rancher/k3s/config.yaml`

Use a minimal stable server configuration with:
- `write-kubeconfig-mode: "0644"`
- `tls-san:` including the server IP and hostname
- explicit `cluster-cidr`
- explicit `service-cidr`

Do not disable Traefik unless the repository explicitly says so.
Do not enable optional advanced features unless required.

### On agent nodes

Create or update:
`/etc/rancher/k3s/config.yaml`

Use:
- `server: https://<server-ip>:6443`
- `token: <join-token>`
- if useful, add a node label reflecting whether the node is vm or ct
- do not add unnecessary taints

Back up any existing K3s config file before changing it.

## Phase 5 - Install K3s server

1. Install K3s on the server node using the official install script.
2. Respect PARAM_K3S_VERSION if set, otherwise use PARAM_K3S_CHANNEL.
3. Start the server service.
4. Wait for readiness.
5. Validate:
   - `systemctl status k3s`
   - kubeconfig exists
   - `kubectl get nodes`
   - `kubectl get pods -A`
6. Retrieve the node token securely from the server node for agent join.
7. Do not write the token into git-tracked files.

## Phase 6 - Install K3s agents

For each worker:
1. Install the K3s agent using the official install script.
2. Use the already-created `/etc/rancher/k3s/config.yaml`.
3. Start the service.
4. Validate:
   - `systemctl status k3s-agent`
   - node appears in `kubectl get nodes -o wide`

## Phase 7 - Cluster validation

From the server node:
1. Confirm all three nodes are `Ready`.
2. Confirm system pods are healthy.
3. Save a human-readable validation report inside the repository at:
   - `notes/cluster-install-report.md`
4. Do not store secrets in the report.

The report should include:
- effective node plan
- timestamps
- K3s version
- node readiness output
- kube-system pod summary
- any warnings or deviations

## Phase 8 - Helm installation

If PARAM_ENABLE_HELM is true:
1. Install Helm on the server/admin node if missing.
2. Verify `helm version`.
3. Update or create:
   - `helm/repositories.md`
   - `notes/helm-install-report.md`

## Phase 9 - Apply repository base manifests

If PARAM_ENABLE_BASE_MANIFESTS is true:
1. Apply namespace/base manifests from the repository.
2. Apply demo app manifests if they exist and are valid.
3. Validate:
   - namespaces created
   - demo deployment healthy
   - demo service healthy
   - ingress object created

Use repository manifests as the source of truth whenever possible.

## Phase 10 - Install core platform components

### Metrics Server

If PARAM_ENABLE_METRICS_SERVER is true:
- install it using the most straightforward supported approach
- validate `kubectl top nodes`

### Headlamp

If PARAM_ENABLE_HEADLAMP is true:
- install using Helm and the repository values file if present
- place it in the intended namespace
- if ingress is configured in values, use PARAM_HEADLAMP_HOST
- otherwise leave access notes in the report

### Observability

If PARAM_ENABLE_OBSERVABILITY is true:
- install kube-prometheus-stack using `helm/prometheus-stack/values.yaml` if present
- install Loki using `helm/loki/values.yaml` if present
- validate the main pods and services
- if ingress is configured, use PARAM_GRAFANA_HOST

### Argo CD

If PARAM_ENABLE_ARGOCD is true:
- create/install in PARAM_ARGOCD_NAMESPACE
- use repo manifests or Helm values where appropriate
- validate the main server/controller pods
- if ingress is configured, use PARAM_ARGOCD_HOST
- do not invent a real Git repo URL in Argo CD applications; keep placeholders if the repo target is not finalized

## Phase 11 - Optional app installs

Install these only if the corresponding flags are true and the repository has enough values/manifests to do so safely:
- Nextcloud
- n8n
- PostgreSQL
- Redis
- AI services
- Longhorn

If repository config is too incomplete for safe install:
- do not guess production settings
- skip the install
- report exactly what is missing

## Phase 12 - Local access notes

Create or update:
- `notes/access-notes.md`

Include:
- suggested `/etc/hosts` entries for the lab domain
- how to access whoami, Headlamp, Grafana, Argo CD
- whether port-forward is required
- which services are intentionally internal-only

## Phase 13 - Safety and rollback notes

Create or update:
- `notes/rollback-notes.md`

Include:
- what was changed on each node
- where K3s config files live
- which services were installed
- how to stop or uninstall K3s safely
- which add-ons are present

## Constraints

- Use the official K3s install script.
- Prefer `/etc/rancher/k3s/config.yaml` for persisted configuration.
- Keep secrets off the repo.
- Do not overwrite non-empty repo files without a reason.
- Do not assume production DNS or certificates.
- Do not expose services publicly unless explicitly configured for local lab ingress.
- Treat `inventory/ips.md` as authoritative for node addresses whenever it contains valid values.
- If any critical preflight fails, stop and report rather than guessing.

## Final output required

At the end, print:
1. what was installed
2. what was skipped
3. exact validation results
4. any manual actions still required
5. the updated repository files
6. a concise “cluster ready / not ready” verdict