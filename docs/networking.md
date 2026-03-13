# Networking

## North-South Traffic
* External client -> Traefik Ingress Controller -> Cluster Services

## East-West Traffic
* Internal K3s networking (Flannel/Calico depending on final K3s config)

## Admin/Management Traffic
* Proxmox GUI: 8006
* Kubernetes API: 6443

## Example Hostnames (Lab exposure)
* `headlamp.lab`
* `grafana.lab`
* `argocd.lab`
* `nextcloud.lab`
* `n8n.lab`
