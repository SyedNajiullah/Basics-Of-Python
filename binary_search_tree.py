#Binary Search Tree
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert_node(self, value):
        if self.root == None:
            self.root = Node(value, None, None)
        else:
            current_node = self.root
            while True:
                if value < current_node.data:
                    if current_node.left == None:
                        current_node.left = Node(value, None, None)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right == None:
                        current_node.right = Node(value, None, None)
                        break
                    else:
                        current_node = current_node.right
                        
    def search_value(self, value):
        if self.root == None:
            return False
        elif self.root.data == value:
            return True
        else:
            current_node = self.root
            while True:
                if value == current_node.data:
                    return True
                
                elif value < current_node.data:
                    if current_node.left == None:
                        return False
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right == None:
                        return False
                    else:
                        current_node = current_node.right
            
    
    def INORDERDISPLAY(self, current_node):
        if current_node == None:
            return
        else:
            self.INORDERDISPLAY(current_node.left)
            print(current_node.data, end = ", ")
            self.INORDERDISPLAY(current_node.right)
    def inorder_display(self):
        if self.root != None:
            self.INORDERDISPLAY(self.root)
        else:
            print("BST is empty")
        
    def PREORDERDISPLAY(self, current_node):
        if current_node == None:
            return
        else:
            print(current_node.data, end = ", ")
            self.PREORDERDISPLAY(current_node.left)
            self.PREORDERDISPLAY(current_node.right)
    def preorder_display(self):
        if self.root != None:
            self.PREORDERDISPLAY(self.root)
        else:
            print("BST is empty")
        
    def POSTORDERDISPLAY(self, current_node):
        if current_node == None:
            return
        else:
            self.POSTORDERDISPLAY(current_node.left)
            self.POSTORDERDISPLAY(current_node.right)
            print(current_node.data, end = ", ")
    def postorder_display(self):
        self.POSTORDERDISPLAY(self.root)
        
    def POSTORDERDISPLAY(self, current_node):
        if current_node == None:
            return
        else:
            self.POSTORDERDISPLAY(current_node.left)
            self.POSTORDERDISPLAY(current_node.right)
            print(current_node.data, end = ", ")
    def postorder_display(self):
        if self.root != None:
            self.POSTORDERDISPLAY(self.root)
        else:
            print("BST is empty")
        
    def DESTROYBST(self, current_node):
        if current_node == None:
            return
        else:
            self.DESTROYBST(current_node.left)
            self.DESTROYBST(current_node.right)
            print(f"Destroying: {current_node.data}")
            current_node.left = None
            current_node.right = None
            current_node.data = None
            del current_node
    def destroy_bst(self):
        if self.root != None:
            self.DESTROYBST(self.root)
            self.root = None
        
        
binary_search_tree = BST()

binary_search_tree.insert_node(100)
binary_search_tree.insert_node(-50)
binary_search_tree.insert_node(150)
binary_search_tree.insert_node(-5)
binary_search_tree.insert_node(500)
binary_search_tree.insert_node(-5)
binary_search_tree.insert_node(800)

binary_search_tree.inorder_display()
print()
binary_search_tree.preorder_display()
print()
binary_search_tree.postorder_display()
print()

result = binary_search_tree.search_value(800)
if result:
    print("Found")
else:
    print("Not Found")
    
result = binary_search_tree.search_value(98)
if result:
    print("Found")
else:
    print("Not Found")
    
binary_search_tree.destroy_bst()
binary_search_tree.inorder_display()
