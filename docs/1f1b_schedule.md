# 1F1B Schedule

Enforces a strict steady-state memory balance by executing a single forward pass over a micro-batch and immediately scheduling a backward pass.

## Diagram

```mermaid
flowchart LR
    F[Forward i] --> B[Backward i-k]
```

Caps peak activation memory utilization to a fixed boundary.
