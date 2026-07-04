# The Interleaved 1F1B Multi-Chunk Era

Slashed pipeline bubbles by interleaving architectural layer assignments.

## Diagram

```mermaid
gantt
    title Interleaved Scheduling
    section GPU 0
    Chunk A :a1, 0, 10
    Chunk C :a2, 20, 30
    section GPU 1
    Chunk B :b1, 10, 20
    Chunk D :b2, 30, 40
```

Each GPU hosts multiple smaller, alternating sub-chunks.
