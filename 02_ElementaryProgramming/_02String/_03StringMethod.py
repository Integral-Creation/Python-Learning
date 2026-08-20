"""Splitting String"""
text = "Python is Easy"

word = text.split()
print(word)
# Output: ['Python', 'is', 'Easy']

text = "Java,Python,C,C++"
word = text.split(",")
print(word)
# Output: ['Java', 'Python', 'C', 'C++']


"""Joining String"""
text = ['Java', 'Python', 'C', 'C++']
word = " ".join(text)
print(word)
# Output: Java Python C C++


"""Removing Character"""
text = "####HELLO####"
words = text.strip("#")
print(words)
# Output: HELLO