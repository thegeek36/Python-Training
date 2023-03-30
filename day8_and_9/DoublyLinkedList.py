class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.headval = None
    
    def traverse(self):
        if self.headval is None:
            print("List is empty")
            return
        else:
            temp = self.headval
            while temp is not None:
                print(temp.data)
                temp = temp.next

    def isEmpty(self):
        if self.headval is None:
            return True
        else:
            return False
        
    def get_length(self):
        temp = self.headval 
        cnt = 0
        while temp is not None:
            temp = temp.next
            cnt += 1
        return cnt
    
    def insert_at_begining(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.headval = new_node
        else:    
            new_node.next = self.headval
            self.headval.prev = new_node
            self.headval = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.insert_at_begining(data)
        else:    
            temp = self.headval
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_at_position(self, data,pos):
        if pos == 1:
            self.insert_at_begining(data)
        else:
            temp = self.headval
            cnt = 1
            while cnt < pos-1:
                temp = temp.next
                cnt += 1
            new_node = Node(data)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node   
            temp.next = new_node

    def delete_at_Start(self):
        if self.headval is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.headval.next is None:
            self.headval = None
            return
        self.headval = self.headval.next
        self.start_prev = None

    def delete_at_end(self):
        # Check if the List is empty
        if self.headval is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.headval.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    
    def delete_at_position(self,pos):
        if self.headval is None:   
            print("The Linked list is empty, no element to delete")
            return
        elif pos == 1:
            self.delete_at_Start()
            return
        cnt = 1
        temp = self.headval
        while temp.next and cnt < pos:
            temp = temp.next
            cnt += 1
        if cnt < pos:
            print("Index out of range")
            return
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None

doublell = DoublyLinkedList()
doublell.headval = Node(9)
doublell.insert_at_end(11)
doublell.insert_at_end(12)
doublell.insert_at_end(13)
doublell.insert_at_position(10,2)
print("Length:",doublell.get_length())
doublell.traverse()
doublell.delete_at_position(2)
print("Length:",doublell.get_length())
doublell.traverse()


        
        
