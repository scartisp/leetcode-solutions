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
        
        def traversNeighbors(node: Optional['Node']):
            if node not in myDict:
                newNode = Node(val=node.val)
                myDict[node] = newNode
            else:
                newNode = myDict[node]
            
            for neighbor in node.neighbors:
                if neighbor in myDict:
                    neighborNode = myDict[neighbor]
                    newNode.neighbors.append(neighborNode)
                else:
                    neighborNode = Node(val=neighbor.val)
                    newNode.neighbors.append(neighborNode)
                    myDict[neighbor] = neighborNode
                    traversNeighbors(neighbor)

        if not node:
            return None
        myDict = {}
        traversNeighbors(node)
        return myDict[node]
