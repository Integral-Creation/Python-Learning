"""
    String 
    In Python, String is a sequence of character used to represent text.
"""

""" 1. Creating String"""
name = "Nikola"
message = "Hello Python"

print(name)
print(message)

""" 2. Accessing String"""
word = "Nikola Tesla"

print(word[7]) # Output-> T
# Negative indexes count from end
print(word[-3]) # Output-> s

""" 3. String are Immutable"""
# word[0] = 'O' # TypeError: 'str' object does not support item assignment

""" 4. String method"""
name = "ada lovelace"
print(name.title()) # Ada Lovelace
print(name.lower()) # ada lovelace
print(name.upper()) # ADA LOVELACE

""" 5. String Concatenation"""
first_name = "Albert"
last_name = "Einstein"
full_name = first_name + " " + last_name

print("Hello, " + full_name + "!") # Hello, Albert Einstein!

""" Adding WhiteSpace"""
print("\tPython")   #        Python

# newLine
print("Language:\nPython\nC\nJava")
    # Language:
    # Python
    # C
    # Java

""" 6. Striping WhiteSpace"""
lang = "python "
print(lang.rstrip()) # 'python'