'''
The central library at Mysore has a set of very interesting books and journals. The books are arranged in the alphabetical order of their author names. 
So it is very easy for the readers to search for the book.
The library has got a set of new books. The librarian wants to arrange them in order too. As some books are already 
arranged in the order, find a suitable way of arranging the new set of books amidst them.

Write a python program to arrange all the books in the  alphabetical order of the author names.
sort_item_list_by_author(): Accepts the new list of books  and returns it sorted in the alphabetical order of their author names.
add_new_items(): Accepts the new list of books, sorts it and merges it with the existing books in the library.
Hint - Use sort_item_list_by_author() method for sorting the books.
sort_items_by_published_year(): Sorts the list of books (item_list) based on the increasing order of their published years.
 If there are multiple items that are published in the same year, then sort them based on the alphabetical order of their author names.
Note: While sorting the author names in alphabetical order, ignore the special characters including space, if there are any.

Library:

- item_list
_init_(item_list)
+ get_item_list()
+ sort_item_list_by_author(new_item_list)
+ add_new_items(new_item_list)
+ sort_items_by_published_year()

Item:
- item_name
- author_name
- published_year
_init_(item_name,author_name,published_year)
+ get_item_name()
+ get_author_name()
+ get_published_year()
_str_()
'''