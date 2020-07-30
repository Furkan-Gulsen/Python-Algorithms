# Binary Tree

- Node's are called structures with a maximum of 2 children.
- Since the number of children will be maximum 2, their names are identified as left and right.
- Like left child and right child.
- The maximum number of nodes at a given level is 2 ^ (l-1), l = level number.
- For example, the maximum number of nodes in the third level 2 ^ 3 = 8.
- height = the total number of paths from the desired node to the leaf below.
- root height = 3 = height tree.
- leaves height = 0

## Some important tree types

- **Full Binary Tree**: Each node has 0 or 2 children.
- **Complete Binary**: Either all their levels will be full, or at least their nodes will be on the left as much as possible.
- **Perfect Binary Tree**: All nodes will have 2 children plus all leaves will be in the same level.
- **A degenerate (or pathological) tree**: If each node has 1 child. As you may have noticed, it looks very similar to the linked list.

<img src="https://miro.medium.com/max/16000/1*CMGFtehu01ZEBgzHG71sMg.png" width="500" />

# Binary Seach Tree
- It requires that all values ​​that can be reached on each node from its left arm are smaller than the value of the node and that all values ​​that can be reached from the right arm must be greater than the value of that node.
And of course it also has to be a binary tree.
- Because of ordering in BST, search is done fast.
- In the worst case, the time complexity of searching and inserting operations is O(h). (h=height).