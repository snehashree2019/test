##creating tree with input from list
class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None

    def get_list(self):
        my_list = []

        list_size = input("Enter the number of elements of a binary search tree ")
        list_size = int(list_size)
        for k in range(0,list_size):
            var = input()
            my_list.append(int (var))

        print("Elements entered : ")
        print(my_list)
        return my_list

    def insert_all(self):
        my_list = self.get_list()
        for ele in my_list:
            self.insert(ele)

    def insert(self,ele):
        if self.data:
            if ele < int(self.data):
                if self.left == None:
                    self.left = Node(ele)
                else:
                    self.left.insert(ele)

            elif ele >= int(self.data):
                if self.right == None:
                    self.right=Node(ele)
                else:
                    self.right.insert(ele)
        else:
             print("Empty root")


##printing tree ,post order traversal
    def print_tree(self):
        if self.data:
            if self.left:
                self.left.print_tree()
            if self.right:
                self.right.print_tree()
        print(self.data)

root_node = input("Enter the value of root node ")
root = Node(root_node)
root.insert_all()
root.print_tree()
