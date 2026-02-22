# A* Maze Solver (Python)

A simple implementation of the A* (A-star) search algorithm in Python, demonstrated on a 4×4 maze represented as a graph.  

This project showcases heuristic search, priority queue usage, and state-space exploration using the Manhattan distance heuristic.

---

## 🚀 Overview

This project implements the A* pathfinding algorithm to compute the optimal path between two rooms in a maze.

The maze is modeled as a graph:
- Each room is a node represented by `(x, y)` coordinates.
- Edges represent open doors between rooms.
- Movement cost between rooms is uniform (cost = 1).
- The heuristic function is Manhattan distance.

---

## 🧠 Algorithm Details

The implementation includes:

- A custom `State` class representing a room
- Priority queue (`heap-based`) for selecting lowest `f(n)` state
- Manhattan distance heuristic
- Visited set to prevent re-expansion
- Path reconstruction during search

A* uses:

```
f(n) = g(n) + h(n)
```

Where:
- `g(n)` = cost from start to current node  
- `h(n)` = Manhattan distance to goal  

---

## 🛠 Requirements

Python 3.9+

No external libraries required.

---

## ▶️ How to Run

From the project directory:

```bash
python maze_solver.py
```

Expected output:

```
Optimal path:
(0,3) → ... → (3,0)
Number of steps: X
```

---

## 📂 Project Structure

```
src/
  maze_solver.py
README.md
```

---

## 🔬 Concepts Demonstrated

- Heuristic search (A*)
- Priority queues
- State-space representation
- Graph traversal
- Hashable custom objects (`__hash__`, `__eq__`)
- Path reconstruction

---

## 📈 Possible Extensions

- Generalized grid input
- Visual grid rendering
- Diagonal movement support
- Weighted edges
- Comparison with BFS / Dijkstra
- Interactive maze input

---

## 📌 Notes

This project is intended as a concise demonstration of A* search in Python.# a-star-pathfinding-python
