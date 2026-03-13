# Topology

## Preferred Topology
* 1x Control Plane (VM)
* 2x Worker Nodes (CT/LXC)

## Trade-offs of CT Workers
**Pros:** Lower overhead, fast boot times, direct host resource mapping.
**Cons:** Kernel sharing limits, challenges with specific CSI drivers or storage overlays.

## Fallback Option
If CT limitations appear (e.g., issues with Longhorn or specific persistent volumes), we will pivot to an all-VM worker topology.
