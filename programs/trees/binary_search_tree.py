## create a node class 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def insert_node(self,data):
##compare the value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

## function to print tree, in-order traversal
    def print_tree(self):
          if self.left:
              self.left.print_tree()
          print(self.data)
          if self.right:
              self.right.print_tree()


root = Node(12)
##root.print_tree()
root.insert_node(6)
root.insert_node(14)
root.insert_node(3)
root.insert_node(1)
root.insert_node(20)
root.print_tree()
