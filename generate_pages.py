import os
import re

docs_dir = 'docs'
os.makedirs(docs_dir, exist_ok=True)

topics = [
    {
        "name": "The Naive Model-Parallel Era (Traditional ML, Pre-2019)",
        "filename": "naive_model_parallel_era.md",
        "title": "The Naive Model-Parallel Era",
        "content": "This era represents the early distributed baseline where deep neural networks were chopped raw across hardware bounds. \n\n## Diagram\n\n```mermaid\nflowchart LR\n    A[Giant Batch] --> B[GPU 0: Layers 1-16]\n    B --> C[PCIe Transfer]\n    C --> D[GPU 1: Layers 17-32]\n```\n\nIt suffered from catastrophic hardware underutilization due to idle periods."
    },
    {
        "name": "The Synchronous Pipelining Revolution (GPipe / 1F1B, 2019–2020)",
        "filename": "synchronous_pipelining_revolution.md",
        "title": "The Synchronous Pipelining Revolution (GPipe / 1F1B)",
        "content": "Dismantled the naive model-parallel wall by introducing the 1F1B execution schedule popularized by Google's GPipe.\n\n## Diagram\n\n```mermaid\nsequenceDiagram\n    participant GPU0\n    participant GPU1\n    GPU0->>GPU1: Forward pass (Micro-batch 1)\n    GPU1-->>GPU0: Backward pass (Micro-batch 1)\n```\n\nWorkload is fractured into independent micro-batches to stabilize memory allocations."
    },
    {
        "name": "The Interleaved 1F1B Multi-Chunk Era (Megatron-LM, 2021–2024)",
        "filename": "interleaved_1f1b_multi_chunk_era.md",
        "title": "The Interleaved 1F1B Multi-Chunk Era",
        "content": "Slashed pipeline bubbles by interleaving architectural layer assignments.\n\n## Diagram\n\n```mermaid\ngantt\n    title Interleaved Scheduling\n    section GPU 0\n    Chunk A :a1, 0, 10\n    Chunk C :a2, 20, 30\n    section GPU 1\n    Chunk B :b1, 10, 20\n    Chunk D :b2, 30, 40\n```\n\nEach GPU hosts multiple smaller, alternating sub-chunks."
    },
    {
        "name": "The Zero-Bubble & Asynchronous Activation Offloading Era (~2024–Present)",
        "filename": "zero_bubble_era.md",
        "title": "The Zero-Bubble Era",
        "content": "The current modern state-of-the-art infrastructure standard built to scale across frontier trillion-parameter foundation clusters.\n\n## Diagram\n\n```mermaid\nflowchart TD\n    A[Forward Pass] --> B[Backward Activations]\n    B --> C[Backward Weights]\n    C -.-> D[Zero Bubble Offloading]\n```\n\nIt decouples backward passes into independent operations."
    },
    {
        "name": "A. GPipe Schedule (Fill-Drain Pipelining)",
        "filename": "gpipe_schedule.md",
        "title": "GPipe Schedule (Fill-Drain Pipelining)",
        "content": "Processes all forward micro-batches continuously across the pipeline cards before initiating backward passes.\n\n## Diagram\n\n```mermaid\nstateDiagram-v2\n    [*] --> Fill\n    Fill --> Drain\n    Drain --> [*]\n```\n\nPeak activation memory footprints scale linearly with the number of micro-batches."
    },
    {
        "name": "B. 1F1B Schedule (One Forward, One Backward)",
        "filename": "1f1b_schedule.md",
        "title": "1F1B Schedule",
        "content": "Enforces a strict steady-state memory balance by executing a single forward pass over a micro-batch and immediately scheduling a backward pass.\n\n## Diagram\n\n```mermaid\nflowchart LR\n    F[Forward i] --> B[Backward i-k]\n```\n\nCaps peak activation memory utilization to a fixed boundary."
    },
    {
        "name": "C. Interleaved 1F1B Schedule",
        "filename": "interleaved_1f1b.md",
        "title": "Interleaved 1F1B Schedule",
        "content": "Sub-divides each physical GPU process into multiple virtual stages holding non-contiguous blocks of layers.\n\n## Diagram\n\n```mermaid\nflowchart TD\n    V1[Virtual Stage 1] --> V2[Virtual Stage 2]\n    V2 --> V3[Virtual Stage 3]\n```\n\nSlashed bubble overhead dramatically."
    },
    {
        "name": "Peer-to-Peer (P2P) Communication Primitives",
        "filename": "p2p_communication.md",
        "title": "Peer-to-Peer (P2P) Communication",
        "content": "Bypasses global cluster broadcast walls. Operates strictly via direct point-to-point boundary calls.\n\n## Diagram\n\n```mermaid\nflowchart LR\n    Node1 <-->|P2P Send/Recv| Node2\n```\n\nUses optimized NCCL drivers over InfiniBand networks."
    },
    {
        "name": "Activation Checkpointing (Rematerialization)",
        "filename": "activation_checkpointing.md",
        "title": "Activation Checkpointing",
        "content": "Memory footprint compression technique discarding intermediate activation tensors and recalculating them on-the-fly.\n\n## Diagram\n\n```mermaid\nflowchart TD\n    A[Forward Loop] -->|Discard| B[Intermediate Tensors]\n    C[Backward Pass] -->|Recalculate| B\n```\n\nKeeps VRAM utilization beneath physical GPU limits."
    },
    {
        "name": "The Parameter-Heterogeneity Load Imbalance Wall",
        "filename": "load_imbalance_wall.md",
        "title": "The Load Imbalance Wall",
        "content": "Modern architectures with massive expert parameters cause severe load imbalance when cut uniformly.\n\n## Diagram\n\n```mermaid\npie title Compute Distribution\n    \"Expert Layers\" : 70\n    \"Dense Layers\" : 30\n```\n\nMitigated by adaptive layer profiling."
    },
    {
        "name": "The Activation Memory Accumulation Crisis",
        "filename": "memory_accumulation_crisis.md",
        "title": "The Activation Memory Accumulation Crisis",
        "content": "Physical volume of un-reduced activation maps explodes as pipeline depth expands.\n\n## Diagram\n\n```mermaid\nflowchart LR\n    GPU[GPU VRAM] -->|Offload| CPU[Host RAM]\n```\n\nMitigated by Asynchronous Activation Swapping."
    },
    {
        "name": "Pre-Training Trillion-Parameter Foundational LLMs (Megatron-DeepSpeed Systems)",
        "filename": "pre_training_llms.md",
        "title": "Pre-Training Trillion-Parameter Foundational LLMs",
        "content": "Crucial structural backbone for training elite base architectures like Llama 3 and DeepSeek-V3.\n\n## Diagram\n\n```mermaid\nflowchart TD\n    A[3D Parallel Topology] --> B(Tensor Parallelism)\n    A --> C(Pipeline Parallelism)\n    A --> D(Data Parallelism)\n```\n\nSplitting massive parameter structures across thousands of GPUs cleanly."
    },
    {
        "name": "High-Volume Spatio-Temporal Video Generation Scaling (Sora Class)",
        "filename": "video_generation_scaling.md",
        "title": "High-Volume Spatio-Temporal Video Generation Scaling",
        "content": "Coordinates large-scale video simulation networks where massive 3D spacetime token cubes are sharded.\n\n## Diagram\n\n```mermaid\nflowchart LR\n    Tokens[Spacetime Tokens] --> ODE[ODE Vector Fields]\n```\n\nAllows ODE vector fields to optimize over multi-megapixel video sequences concurrently."
    },
    {
        "name": "Enterprise Post-Training On-Policy RL Alignment Sprints (RLHF / PPO)",
        "filename": "rl_alignment_sprints.md",
        "title": "Enterprise Post-Training On-Policy RL Alignment",
        "content": "Powers distributed alignment loops for advanced reasoning models requiring multiple networks in VRAM concurrently.\n\n## Diagram\n\n```mermaid\nflowchart TD\n    A[RL Loop] --> Actor\n    A --> Critic\n    A --> Reference\n    A --> RewardModel\n```\n\nCuts parallel networks across isolated node shards."
    }
]

for topic in topics:
    filepath = os.path.join(docs_dir, topic["filename"])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {topic['title']}\n\n{topic['content']}\n")

with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

for topic in topics:
    name = topic["name"]
    filename = topic["filename"]
    search_str = f"**{name}**"
    replace_str = f"[**{name}**](./docs/{filename})"
    readme_content = readme_content.replace(search_str, replace_str)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("Pages created and README updated.")
