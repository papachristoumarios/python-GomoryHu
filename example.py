from gomory_hu import GomoryHuTree


graph = [[0, 1, 7, 0, 0, 0],
         [1, 0, 1, 3, 2, 0],
         [7, 1, 0, 0, 4, 0],
         [0, 3, 0, 0, 1, 6],
         [0, 2, 4, 1, 0, 2],
         [0, 0, 0, 6, 2, 0]]

# Construct GomoryHuTree
tree = GomoryHuTree(graph)

# Print Tree Contents
print(tree)

# Query for min cut between 0 and 4
print(tree.query(2, 0))
print(tree.query(0, 2))

# Print the edge (0, 3)
print(tree[0, 3])
