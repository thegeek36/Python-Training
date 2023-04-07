class BakeHouse:
    def __init__(self):
        self.__occupied_table_list = list

    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def allocate(self):
        l = []
        for i in range(11):
            if i in self.__occupied_table_list:
                l.append(i)

    def deallocate_table(self, table_number):
        if table_number not in self.__occupied_table_list:
            print("The Table is already vaccant")
        else:
            self.__occupied_table_list.remove(table_number)
            
    def display(self):
        print(self.__occupied_table_list)

resturant = BakeHouse()
resturant.allocate()
print("Allocation")
resturant.display()
resturant.deallocate_table(6)
resturant.allocate()
print("After Deallocation")
resturant.display()



