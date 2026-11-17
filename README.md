# Informatics ITS Graph Theory IUP

## Group 1: Network Flow Assignment

<div align=center>

|    NRP     |           Nama              |
| :--------: |       :------------:        |
| 5025251012 | Khumaidy Syafiq El Maududy  |
| 5025251015 | Renato Kiran Arisandi       |
| 5025251016 | Keven John Gondowardojo     |
| 5025251010 | Agile Octa Agrakha Handrian |

</div>

---

### Overview

This repository contains implementations of **two network flow algorithms other than the Ford-Fulkerson Algorithm** as required for the Graph Theory assignment:

1. **[Dinic's Algorithm](./Dinic's%20Algorithm/)**
   * Multi-path augmenting flow algorithm based on constructing layered **Level Graphs** (via BFS) and finding **Blocking Flows** (via DFS with edge pointer pruning).
   * **Time Complexity**: $\mathcal{O}(V^2 E)$ in general networks, $\mathcal{O}(E \sqrt{V})$ in unit networks.

2. **[Push-Relabel Algorithm](./Push-Relabel%20Algorithm/)** (Goldberg–Tarjan)
   * Local operation algorithm based on **Preflows**, **Height Functions (Distance Labels)**, and **FIFO Discharge** (`push` and `relabel`), completely eliminating global source-to-sink path searches.
   * **Time Complexity**: $\mathcal{O}(V^3)$ with FIFO selection.

---

### Algorithm Comparison

| Feature | Dinic's Algorithm | Push-Relabel Algorithm | Standard Ford-Fulkerson |
| :--- | :---: | :---: | :---: |
| **Approach** | Level Graph & Blocking Flow | Preflow & Local Push/Relabel | Single Augmenting Path (DFS) |
| **Time Complexity** | $\mathcal{O}(V^2 E)$ | $\mathcal{O}(V^3)$ | $\mathcal{O}(E \cdot \|f^*\|)$ |
| **Flow Conservation** | Maintained after each phase | Relaxed during execution (Preflow) | Maintained at every step |
| **Path Search** | Global BFS layers + DFS paths | None (strictly local operations) | Global DFS |

---

### How to Run

Each algorithm is implemented with pure standard Python libraries.

```bash
# Algorithm 1: Dinic's Algorithm
cd "Dinic's Algorithm"
python implementation.py

# Algorithm 2: Push-Relabel Algorithm
cd "../Push-Relabel Algorithm"
python implementation.py
```

Sample cases and verification are available in each respective folder's `sample.txt` and `README.md`.
