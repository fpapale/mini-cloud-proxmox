# Access Notes

## Local DNS / hosts entries

Add the following to your local `/etc/hosts` (Linux/Mac) or `C:\Windows\System32\drivers\etc\hosts` (Windows):

```
192.168.0.100  whoami.lab headlamp.lab grafana.lab argocd.lab nextcloud.lab n8n.lab
```

## Services

| Service   | URL                     | Status        | Access Method       |
|-----------|-------------------------|---------------|---------------------|
| whoami    | http://whoami.lab       | ✅ Deployed    | Traefik Ingress     |
| Headlamp  | http://headlamp.lab    | ⏳ Pending     | port-forward or Ingress |
| Grafana   | http://grafana.lab     | ❌ Not installed | —                 |
| Argo CD   | http://argocd.lab      | ❌ Not installed | —                 |

## Port-forward fallback

If Traefik ingress is not working for a service, use kubectl port-forward:

```bash
# Headlamp
kubectl port-forward -n apps svc/headlamp 8080:80
# Then open http://localhost:8080

# whoami
kubectl port-forward -n demo svc/whoami 8081:80
# Then open http://localhost:8081
```

## Internal-only services

The following are intentionally cluster-internal:
- CoreDNS
- Metrics Server
- local-path-provisioner
