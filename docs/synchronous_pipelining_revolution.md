# The Synchronous Pipelining Revolution (GPipe / 1F1B)

Dismantled the naive model-parallel wall by introducing the 1F1B execution schedule popularized by Google's GPipe.

## Diagram

```mermaid
sequenceDiagram
    participant GPU0
    participant GPU1
    GPU0->>GPU1: Forward pass (Micro-batch 1)
    GPU1-->>GPU0: Backward pass (Micro-batch 1)
```

Workload is fractured into independent micro-batches to stabilize memory allocations.
