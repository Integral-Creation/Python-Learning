"""
    String method are built-in method that you can use on string
"""

name = "nikolaTesla"

"""Change Case"""
print(name.upper())
# Output: NIKOLATESLA

print(name.lower())
# Output: nikolatesla

print(name.capitalize())
# Output: Nikolatesla

print(name.title())
# Output: Nikolatesla

print(name.swapcase())
# Output: NIKOLAtESLA

"""Removing Spaces"""
text = "   Hello World "

print(text.strip())
# Output: Hello World
print(text.lstrip())
# Output: Hello World
print(text.rstrip())
# Output:    Hello World

"""Finding & Counting"""
print(text.find("World"))
# Output: 9
print(text.count("l"))
# Output: 3

"""Replace"""
text = "I like Java Programming"
print(text.replace("Java","Python"))
# Output: I like Python Programming

"""Checking the content"""
print("hello".startswith("he"))
# Output: True
print("hello".endswith("lo"))
# Output: True
print("123".isdigit())
# Output: True
print("abc".isalpha())
# Output: True
print("abc123".isalnum())
# Output: True
print("hello".islower())
# Output: True
print("HELLO".isupper())
# Output: True
print(" ".isspace())
# Output: True