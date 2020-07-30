class Node:
	def __init__(self,key):
		"""
		constructor
		"""
		self.val = key
		self.left = None
		self.right = None


def insert(root,node):
	if root in None:
		root = node
	else:
		if root.val < node.val:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

"""
		8
	  /   \
	 5     11
	/ \    / \
   2   7  9   18
"""
r = Node(8)
insert(r, Node(5))
insert(r, Node(2))
insert(r, Node(7))
insert(r, Node(9))
insert(r, Node(18))
insert(r, Node(11))

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)
	else:
		return None

inorder(r)