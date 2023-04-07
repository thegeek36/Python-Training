'''
Write a python function which accepts two linked lists containing integer data and an integer, 
n and merges the two linked lists,such that list2 is merged with list1 after n number of nodes. 
Assume that value of n will always be less than or equal to the number of nodes in list1.
sample Input :
list1 = 1->2->3->4->5
list 2 = 9->8->11
n = 2
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class LinkedList:

#     def __init__(self):
#         self.head = None

#     # Insert at the beginning
#     def insertAtBeginning(self, new_data):
#         new_node = Node(new_data)

#         new_node.next = self.head
#         self.head = new_node

#     # Insert after a node
#     def insertAfter(self, prev_node, new_data):

#         if prev_node is None:
#             print("The given previous node must inLinkedList.")
#             return

#         new_node = Node(new_data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node

#     # Insert at the end
#     def insertAtEnd(self, new_data):
#         new_node = Node(new_data)

#         if self.head is None:
#             self.head = new_node
#             return

#         last = self.head
#         while (last.next):
#             last = last.next
#         last.next = new_node

#     # Print the linked list
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(str(temp.data) + " ", end="")
#              temp = temp.next

def merge_list(list1,list2,n):
    if n == 0:
        return list2
    curr  = list1
    count = 1
    while curr is not None and count < n:
        curr = curr.next
        count += 1
    nxt_node  = curr.next
    curr.next = list2

    while list2.next is not None:
        list2 = list2.next
    list2.next = nxt_node

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)
list1.next.next.next = Node(3)
list1.next.next.next.next = Node(5)

#the second linked list
list2 = Node(9)
list2.next = Node(8)
list2.next.next = Node(11)


merge_list(list1, list2, 2)
merged_list = list1
# Print the merged linked list
current = merged_list
while current is not None:
    print(current.data, end="->")
    current = current.next



