# Enterprise Post-Training On-Policy RL Alignment

Powers distributed alignment loops for advanced reasoning models requiring multiple networks in VRAM concurrently.

## Diagram

```mermaid
flowchart TD
    A[RL Loop] --> Actor
    A --> Critic
    A --> Reference
    A --> RewardModel
```

Cuts parallel networks across isolated node shards.
