sentence =input("Enter a sentence: ")   

#1. turn the string into a list of words
words = sentence.split(" ")
print("List of words:", words)
#2. Reverse the list 
words.reverse()
print("Reversed list of words:", words)

#3. Join the list of words back into a single string
new_sentence = " ".join(words)
print("Reversed sentence:", new_sentence)