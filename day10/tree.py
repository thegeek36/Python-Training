class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(node,data):
    if node is None:
        return Node(data)
    if data <= node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)
    return node
     
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data)+"->",end="")
        inorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data)+"->",end="")
#Depth First Search
def preorder(root):
    if root:
        print(str(root.data)+"->",end="")
        preorder(root.left)
        preorder(root.right)
def deleteNode(root,data):
    if root is None:
        return root
    if data < root.data:
        root.left = deleteNode(root.left,data)
    elif data > root.data:
        root.right = deleteNode(root.right,data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp


root  = None
root = insert(root,10)
root = insert(root,11)
root = insert(root,12)
root = insert(root,13)
root = insert(root,14)
root = insert(root,15)
root = insert(root,16)
root = insert(root,17)
root = insert(root,18)
root = insert(root,19)
inorder(root)

