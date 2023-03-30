'''
Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words. 
The task is to find the unknown words (other than the words they already know) from the given text. 
Write a python function which accepts the text and the known list of words and returns the set of unknown words found.
Return -1 if there are no unknown words. Estimated Time: 20 minutes
Sample Input
Text: "the sun rises in the east"
Vocabulary: ["sun", "in", "east", "doctor", "day"]
Expected Output
{'rises','the'}
'''
text = input("Enter the text: ")
#vocabulary = list(map(input().split()))
vocabulary = ["sun", "in", "east", "doctor", "day"]
def fun(text, vocabulary):
    l = []
    for i in text.split():
        if i not in vocabulary:
            l.append(i)
    if len(l) == 0:
        return -1
    else:
        return set(l)    
print(fun(text, vocabulary))
