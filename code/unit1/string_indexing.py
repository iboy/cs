# String handling - String indexing

sentence = "Hello World"

# square brackets let us access the letter at an index. This behaves like lists in Python

first_letter = sentence[0]
last_letter = sentence[-1]

index_of_first_O = sentence.find("o")
print(index_of_first_O) #  >> 4

index_of_first_O = sentence.index("o")
print(index_of_first_O) #  >> 4

index_of_first_e = sentence.find("e")
print(index_of_first_e) #  >> 1 What about the second one? 

index_of_X = sentence.find("X")
print(index_of_X) #  >> 4

index_of_X = sentence.index("X")
print(index_of_X) #  >> 4