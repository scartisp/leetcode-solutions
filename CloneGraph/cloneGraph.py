"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def travers(node):
            if node in seen:
                return seen[node]
            
            newNode = Node(node.val)
            seen[node] = newNode

            for neighbor in node.neighbors:
                if neighbor not in seen:
                    newNode.neighbors.append(travers(neighbor))
                else:
                    newNode.neighbors.append(seen[neighbor])
            
            return newNode


        if not node:
            return None
        seen = {}
        return travers(node)
