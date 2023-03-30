'''
A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.

Train:
(- Private)
(+ Public)

- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()

Write a python program to implement the following:
count_compartments()- returns the total number of compartments
in the train.

check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where 
data in each node refers to a compartment.
'''
#Node 
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node
        
#Linked List 
class LinkedList:
    def __init__(self):
        self.__head=None

    def get_head(self):
        return self.__head
    
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=new_node
        else:
            self.__tail.set_next(new_node)

    def insert_at_end(self,data):
        newnode = Node(data)
        if self.headval is None:
            self.headval = newnode
        newnode.next = None
        temp = self.headval
        while  temp.next is not None:
            temp = temp.next
        temp.next = newnode 

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                new_node.insert_at_end(data)
        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()

    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None   
   
class Compartment:
    def __init__(self,compartment_name,no_of_passengers,total_seats):
        self.__compartment_name=compartment_name
        self.__no_of_passengers=no_of_passengers
        self.__total_seats=total_seats
    
    def get_compartment_name(self):
        return self.__compartment_name
    
    def get_no_of_passengers(self):
        return self.__no_of_passengers
    
    def get_total_seats(self):
        return self.__total_seats
    
class Train:
    def __init__(self,train_name,compartment_list): 
        self.__train_name=train_name 
        self.__compartment_list=compartment_list
    
    def get_train_name(self):
        return self.__train_name
    
    def count_compartments(self):
        temp = self.__compartment_list.get_head()
        count=0
        while(temp):
            count+=1
            temp=temp.get_next()
        return count

    def check_vacancy(self):
        count=0
        temp=self.__compartment_list.get_head()
        while(temp):
            percentage= (temp.get_data().get_total_seats() - temp.get_data().get_no_of_passengers())/temp.get_data().get_total_seats()
            if percentage>0.5:
                count+=1
            temp=temp.get_next()
        return count
    
#Use different values for compartment and test your program    
compartment1=Compartment("SL",250,400) 
compartment6=Compartment("CC",200,400)    
compartment2=Compartment("2AC",125,280)   
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)
compartment_list=LinkedList()
compartment_list.add(compartment1)
compartment_list.add(compartment2)
compartment_list.add(compartment3)
compartment_list.add(compartment4)
compartment_list.add(compartment5)
compartment_list.add(compartment6)
train1=Train("InterCity Express ",compartment_list)
count=train1.count_compartments()
print("Train Name:",train1.get_train_name())
print("The number of compartments in the train:",count)
vacancy_count=train1.check_vacancy()
print("The number of compartments which have more than 50% vacancy:",vacancy_count)


