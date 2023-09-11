import re
from collections import defaultdict

def word_frequency(sentence):
    word_count = defaultdict(int)  # Initialize a dictionary with default values of 0
    words = re.findall(r'\w+', sentence.lower())  # Find all words in the sentence
    
    for word in words:
        word_count[word] += 1  # Increment the count for each word
    
    return dict(word_count)  # Convert the defaultdict to a regular dictionary

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
