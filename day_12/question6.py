'''
Write a python function, check_anagram() which accepts two strings and returns True, if one string is an anagram of another string. 
Otherwise returns False.
The two strings are considered to be an anagram if they 
contain repeating characters but none of the characters repeat at the same position.
The length of the strings should be the same.
'''
def check_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if sorted(word1) == sorted(word2):
        print("Anagram")      
    else:
        print("Not Anagram")  

check_anagram("Area","aare")