# Exercise 8 – Word Counter
sentence = "python is easy and python is powerful"

words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
#1. Count frequency of each word
#2. Store results in dictionary
print("Word frequency:", word_count)
