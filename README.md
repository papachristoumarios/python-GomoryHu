# Gomory-Hu Tree Data Structure Implementation in Python

## Description

This repository contains a simple implementation of the [Gomory-Hu tree data structure](https://en.wikipedia.org/wiki/Gomory%E2%80%93Hu_tree) that allows for efficient computation of minimum s-t cuts in a network via precomputing a tree.

It constructs a tree by doing minimum cuts in the original network splitting it gradually into components. Finally, when the tree is constructed, one can query a minimum cut by doing a tree traversal on the Gomory-Hu Tree and keeping the minimum cost from s to t.  

## Implementation

This is a very simple implementation of the data structure and the algorithm used in constructing it. The Ford-Fulkerson algorithm is used to compute maximum flow / minimum cut. There are also faster flow algorithms available (e.g. Edmonds-Karp, Dinic). The algorihtm can also be parallelized for faster computation. 

## Installation

The code can be installed with `distutils` via:

```bash
python3 setup.py install
```

## Usage

 1. See `example.py` for instructions on using the GomoryHuTree class for constructing Gomory-Hu trees.
 2. The API docs are accesible via the `help(gomory_hu)` command in a python prompt.
