class Node:
  def __init__(self,data = None,left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
    
class BST:
  def __init__(self):
    self.root = None
  
  def traverse(self):
    if self.root is None:
      print("BST is empty")
    
    else:
      n = self.root
      temp_left = n.left
      temp_right = n.right
      
      if temp_left is None and temp_right is None:
        print(n.data)
      else:
        while temp_left is not None and temp_right is not None:
          print(temp_left.data)
          print(temp_right.data)
          
          temp_left = temp_left.left
          temp_right = temp_right.right
        
  def insert_in_bst(self,data):
    if self.root is None:
      new_node = Node(data = data)
      self.root = new_node
    
    else:
      temp = self.root 
      while temp.left is not None and temp.right is not None:
        if data > temp.data:
          new_node_right = Node(data = data)
          temp.right = new_node_right
        
        else:
          new_node_left = Node(data = data)
          temp.left = new_node_left
        
        
      
bst = BST()

bst.insert_in_bst(10)
bst.insert_in_bst(20)
print(10)
bst.traverse()