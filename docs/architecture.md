# Architecture

## Executive Summary
This document outlines the architecture of the mini-cloud platform running on Proxmox, emphasizing a lightweight, GitOps-ready Kubernetes environment.

## Architecture Layers
- **Proxmox layer:** Bare-metal hypervisor providing compute boundaries.
- **VM/CT layout:** 1 Control Plane VM and 2 LXC (CT) worker nodes to balance isolation and overhead.
- **K3s cluster layer:** Lightweight, CNCF-certified Kubernetes distribution.
- **Ingress layer:** Traefik ingress controller for L7 routing.
- **Observability layer:** Prometheus, Grafana, Loki, Promtail, and Metrics Server.
- **GitOps layer:** Argo CD managing app-of-apps deployments.
- **Apps/Data layer:** Nextcloud, n8n, Postgres, Redis.

*Note: AI workloads and Longhorn distributed storage are optional later phases.*
