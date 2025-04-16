# Week 9 Session 1 Standard Problem Set Version 1
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root



# PROBLEM TWO
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    # iteratively using a deque
    # base case -- tree is empty
    if not design:
        return []
    
    # create empty deque and visited list
    dq = deque()
    visited = [] 

    # add the root into queue
    dq.append(design)
    
    # while queue is not empty
    while (dq):
        poppedNode = dq.popleft() # get first element
        visited.append(poppedNode) # add to visted list

        # if poppedNode is None, dont bother appending children
        if poppedNode:
            # add children to queue
            dq.append(poppedNode.left)
            dq.append(poppedNode.right)
    # dq would be empty at end of while loop
    
    # make nice list
    printList = []
    for node in visited:
        if node:
            printList.append(node.val)
    print(printList)
    

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche) # ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']