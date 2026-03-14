# Rollback Notes

## What was changed on each node

### k3s-master (192.168.0.100 — VM)
- Installed: K3s server v1.34.5+k3s1, Helm 3
- Config file: `/etc/rancher/k3s/config.yaml`
- Kubeconfig: `/etc/rancher/k3s/k3s.yaml`
- Data dir: `/var/lib/rancher/k3s/`
- Applied manifests: namespaces, demo whoami app, headlamp
- Packages installed: curl, ca-certificates, sudo, jq, vim, nano

### ks3-worker1 (192.168.0.101 — CT/LXC)
- Installed: K3s agent v1.34.5+k3s1
- Config file: `/etc/rancher/k3s/config.yaml`
- Data dir: `/var/lib/rancher/k3s/`
- Feature gate: `KubeletInUserNamespace=true`
- Snapshotter: `native`
- Packages installed: curl, ca-certificates, sudo, jq, vim, nano

### ks3-worker2 (192.168.0.102 — CT/LXC)
- Same as ks3-worker1

## How to stop K3s

```bash
# On master
sudo systemctl stop k3s

# On workers
sudo systemctl stop k3s-agent
```

## How to uninstall K3s

```bash
# On master (WARNING: destroys the entire cluster)
sudo /usr/local/bin/k3s-uninstall.sh

# On workers
sudo /usr/local/bin/k3s-agent-uninstall.sh
```

## How to uninstall Helm charts

```bash
helm uninstall headlamp -n apps
```

## Add-ons present
- Traefik (built-in with K3s)
- Metrics Server (built-in with K3s)
- CoreDNS (built-in with K3s)
- local-path-provisioner (built-in with K3s)
- Headlamp (Helm chart in apps namespace)
- Demo whoami app (in demo namespace)
