# Activation Checkpointing

Memory footprint compression technique discarding intermediate activation tensors and recalculating them on-the-fly.

## Diagram

```mermaid
flowchart TD
    A[Forward Loop] -->|Discard| B[Intermediate Tensors]
    C[Backward Pass] -->|Recalculate| B
```

Keeps VRAM utilization beneath physical GPU limits.
