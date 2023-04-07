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

# Find the inorder successor
def minValueNode(node):
    current = node
    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left
    return current

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
        # Delete the inorder successor
        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)
        root.data = temp.data
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)
    return root

root  = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,10)
root = insert(root,1)
root = insert(root,6)
root = insert(root,14)
root = insert(root,4)
root = insert(root,7)

print("InOrder")
inorder(root)
print()
print("PreOrder")
preorder(root)
print()
print("PostOrder")
postorder(root)

deleteNode(root,8)
print()
print("After Deletion")
print("InOrder")
inorder(root)
print()
print("PreOrder")
preorder(root)
