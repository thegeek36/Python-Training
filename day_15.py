#Create a linked List for 1->2->3->4->5->8->7->6->3.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,index,data):
        if index == 1:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
        else:
            newnode = Node(data)
            temp = self.head
            count = 1
            while(temp is not None):
                count = count + 1
                temp = temp.next
                if count  == index:
                    break
            newnode.next = temp.next
            temp.next = newnode

    def print(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,end="->")
            temp = temp.next
    def isCycle(self):
        slow = self.head
        fast = self.head
        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                print("Cycle detected")
                return slow
        return None
    
    def findcycle(self,ptr):
        if(ptr== None):
            print("No Cycle detected")
            return 
        start  = self.head
        while(start != ptr):
            ptr = ptr.next
            start = start.next
        print("Cycle detected at",ptr.data)
    




            
            
list = LinkedList()
list.head = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)
l6 = Node(6)
l7 = Node(7)
l8 = Node(8)
list.head.next = l2 
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l8
l8.next = l7
l7.next = l6
l6.next = l3
#list.print()
ptr=list.isCycle()
list.findcycle(ptr)





