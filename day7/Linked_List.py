#Linked List
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.next
                     
list = SLinkedList()
list.headval = Node("Hi")
list.headval = Node("Hello")
list.listprint()

    