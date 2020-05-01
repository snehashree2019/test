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
    def print_in_order(self):
          if self.left:
              self.left.print_in_order()
          print(self.data)
          if self.right:
              self.right.print_in_order()

## function to print_tree, pre-order traversal
    def print_pre_order(self):
        if self.data:
            print(self.data)
            if self.left:
                self.left.print_pre_order()
            if self.right:
                self.right.print_pre_order()

#function to print_tree , post-order traversal
    def print_post_order(self):
        if self.data:
            if self.left:
                self.left.print_post_order()
            if self.right:
                self.right.print_post_order()

        print(self.data)


#function to search node, divide & conquer method
    def search_node(self,num):
        if self.data:
            if self.data == num:
                print("number found")
            else:
                if num < self.data and self.left:
                    self.left.search_node(num)

                if num > self.data and self.right:
                    self.right.search_node(num)
        else:
            print("Empty tree")
