# Cluster Installation Report

**Date**: 2026-03-14
**K3s Version**: v1.34.5+k3s1

## Nodes
```
[sudo] password for fpapale: NAME          STATUS   ROLES           AGE    VERSION        INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
k3s-master    Ready    control-plane   30m    v1.34.5+k3s1   192.168.0.100   <none>        Ubuntu 24.04.4 LTS   6.8.0-106-generic   containerd://2.1.5-k3s1
ks3-worker1   Ready    <none>          119s   v1.34.5+k3s1   192.168.0.101   <none>        Ubuntu 25.04         6.17.9-1-pve        containerd://2.1.5-k3s1
ks3-worker2   Ready    <none>          112s   v1.34.5+k3s1   192.168.0.102   <none>        Ubuntu 25.04         6.17.9-1-pve        containerd://2.1.5-k3s1
```

## All Pods
```
[sudo] password for fpapale: NAMESPACE     NAME                                      READY   STATUS      RESTARTS   AGE
demo          whoami-7c7f4944c6-ntdb4                   1/1     Running     0          19s
demo          whoami-7c7f4944c6-z5vfj                   1/1     Running     0          19s
kube-system   coredns-695cbbfcb9-ppm2l                  1/1     Running     0          29m
kube-system   helm-install-traefik-crd-dk4xj            0/1     Completed   0          29m
kube-system   helm-install-traefik-mk97b                0/1     Completed   1          29m
kube-system   local-path-provisioner-546dfc6456-rbtm7   1/1     Running     0          29m
kube-system   metrics-server-c8774f4f4-2bxrm            1/1     Running     0          29m
kube-system   svclb-traefik-791a747f-5vxp2              2/2     Running     0          29m
kube-system   svclb-traefik-791a747f-njpxk              2/2     Running     0          113s
kube-system   svclb-traefik-791a747f-w7c5l              2/2     Running     0          119s
kube-system   traefik-788bc4688c-hzzl4                  1/1     Running     0          29m
```

## What was installed
- K3s server on k3s-master (VM)
- K3s agents on ks3-worker1, ks3-worker2 (CT/LXC)
- Helm 3
- Namespaces: ingress, observability, gitops, storage, apps, databases, ai, demo
- Demo whoami app (deployment + service + ingress)
- Headlamp dashboard
