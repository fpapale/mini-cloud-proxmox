# BOM & Sizing

## Minimum Viable
| Component | CPU | RAM | Disk | Note |
|---|---|---|---|---|
| Control Plane VM | 2 vCPU | 2 GB | 20 GB | Minimal K3s master |
| Worker 1 (CT) | 2 vCPU | 2 GB | 20 GB | |
| Worker 2 (CT) | 2 vCPU | 2 GB | 20 GB | |

## Recommended
| Component | CPU | RAM | Disk | Note |
|---|---|---|---|---|
| Control Plane VM | 2 vCPU | 4 GB | 30 GB | |
| Worker 1 (CT) | 4 vCPU | 8 GB | 50 GB | Primary apps |
| Worker 2 (CT) | 4 vCPU | 8 GB | 50 GB | Observability |

## Expanded with AI
| Component | CPU | RAM | Disk | Note |
|---|---|---|---|---|
| Control Plane VM | 2 vCPU | 4 GB | 30 GB | |
| AI Worker (VM/CT) | 8+ vCPU/GPU | 16+ GB | 100+ GB | Depends on LLM model |
