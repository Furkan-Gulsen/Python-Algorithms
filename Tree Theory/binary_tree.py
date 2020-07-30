class Node:
	"""
	binary tree nodes
	"""
	def __init__(self,key):
		"""
		constructor
		"""
		self.val = key
		self.right = None
		self.left = None



"""
Create Node

		a
	   / \
	  b   c
     /
    d
"""
root = Node('A')
root.left = Node('B')
root.left.left = Node('D')
root.right = Node('C')