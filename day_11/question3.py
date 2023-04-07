'''
Replace the maximum element count of the linked list with any number/element.
Sample Input:
12->95->56->60->90->140->100
Output:
12->95->56->60->90->150->100
The maximum element is '140' which is replaced by '150'
'''
#Question
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.headval = None

def replace_max(list):
    max_val = list.data 
    temp = list
    curr = list.next
    while curr is not None:
        if curr.data > max_val:
            max_val = curr.data
            temp = curr
        curr = curr.next
    temp.data = 100
  
list = Node(12)
list.next = Node(95)
list.next.next = Node(140)
list.next.next.next = Node(110)
list.next.next.next.next = Node(40)
list.next.next.next.next.next = Node(500)
replace_max(list)

while list is not None:
    print(list.data, end="->")
    list = list.next

#Chat GPT
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def replace_max(self, new_num):
        if self.head is None:
            print("List is empty")
            return
        max_val = self.head.data
        max_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_node.data > max_val:
                max_val = current_node.data
                max_node = current_node
            current_node = current_node.next
        max_node.data = new_num

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Example usage
my_list = LinkedList()
my_list.append(3)
my_list.append(7)
my_list.append(2)
my_list.append(9)
my_list.append(5)

print("Original list:")
my_list.print_list()

my_list.replace_max(10)

print("List after replacing maximum value with 10:")
my_list.print_list()

'''
            
    


