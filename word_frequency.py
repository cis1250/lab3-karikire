#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

#My code starts here
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

words = user_sentence.split()

uniqueWords = []
frequencyOfWords = []

for word in words:
    words = word.strip(",.!?").lower()
    if word in uniqueWords:
        index = uniqueWords.index(word)
        frequencyOfWords[index] += 1
    else:
        uniqueWords.append(word)
        frequencyOfWords.append(1)


for i in range(len(uniqueWords)):
    print(f"{uniqueWords[i]}: {frequencyOfWords[i]}")

    
