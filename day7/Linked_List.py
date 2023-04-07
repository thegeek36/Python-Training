#Linked List
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        if self.headval is None:
            print("List has no Element")
            return 
        else:
            printval = self.headval
            while printval is not None:
                print(printval.data)
                printval = printval.next

    def At_Begining(self,data):
        newnode = Node(data)
        newnode.next = self.headval
        self.headval = newnode
    
    def at_Ending(self,data):
        newnode = Node(data)
        if self.headval is None:
            self.headval = newnode
        newnode.next = None
        temp = self.headval
        while  temp.next is not None:
            temp = temp.next
        temp.next = newnode 
        
    def insert_at_index(self,index,data):
        if self.headval is None:
            print("List has no Element")
            return 
        if index == 0:
            self.At_Begining(data)
        elif index == self.get_count():
            self.at_Ending(data)
        else:
            newnode = Node(data)
            newnode.next = self.headval
            self.headval = newnode

    def delete_at_start(self):
        if self.headval is None:
            print("List has no Element")
            return 
        else:
            temp = self.headval
            self.headval = self.headval.next
            temp.next = None
    def delete_at_end(self):
        if self.headval is None:
            print("List has no Element")
            return 
        else:
            temp = self.headval
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_element_by_value(self, value):
        if self.headval is None:
            print("List has no Element")
            return 
        if self.headval.data == value:
            self.headval = self.headval.next
        temp = self.headval
        while temp.next is not None:
            if temp.next.data == value:
                break
            temp = temp.next
        if temp.next is None:
            print("List has no Element with value: " + value)
        else:
            temp.next = temp.next.next
    def get_count(self):
        if self.headval is None:
            print("List has no Element")
            return 0
        else:
            count = 1
            temp = self.headval
            while temp.next is not None:
                count = count + 1
                temp = temp.next
            return count
    def reverse(self):
        if self.headval is None:
            print("List has no Element")
            return 
        else:
            temp = self.headval
            prev = None
            while temp.next is not None:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            self.headval = prev
'''
list = LinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("wed")
e4 = Node("Thrus")
#Linking the first val to node
list.headval.next = e2
e2.next = e3
e3.next = e4
list.listprint()
print()
list.At_Begining("Sun")
list.at_Ending("Friday")
list.at_Ending("Saturday")
list.listprint()
print("---------------------")
print("Deleting from Start...")
list.delete_at_start()
list.listprint()
print("---------------------")
print("Deleting from End...")
list.delete_at_end()
list.listprint()
print("---------------------")
print("Deleting by value...")
list.delete_element_by_value("Tue")
list.listprint()
print(list.get_count())
'''

list = LinkedList()
even_list = LinkedList()
odd_list = LinkedList()
list.headval = Node(2)
e2 = Node(3)
list.headval.next = e2
list.insert_at_index(2,4)
list.insert_at_index(3,5)
list.insert_at_index(4,6)
list.insert_at_index(5,7)
list.insert_at_index(6,8)
list.listprint()
temp = list.headval
while temp.next is not None:
    if temp.data % 2 == 0:
        even_list.At_Begining(temp.data)
    else:
        odd_list.At_Begining(temp.data)
    temp = temp.next
print("Even list")
even_list.listprint()
print("odd list")
odd_list.listprint()

    