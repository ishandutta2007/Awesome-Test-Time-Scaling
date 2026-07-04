# Peer-to-Peer (P2P) Communication

Bypasses global cluster broadcast walls. Operates strictly via direct point-to-point boundary calls.

## Diagram

```mermaid
flowchart LR
    Node1 <-->|P2P Send/Recv| Node2
```

Uses optimized NCCL drivers over InfiniBand networks.
