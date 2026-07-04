# The Naive Model-Parallel Era

This era represents the early distributed baseline where deep neural networks were chopped raw across hardware bounds. 

## Diagram

```mermaid
flowchart LR
    A[Giant Batch] --> B[GPU 0: Layers 1-16]
    B --> C[PCIe Transfer]
    C --> D[GPU 1: Layers 17-32]
```

It suffered from catastrophic hardware underutilization due to idle periods.
