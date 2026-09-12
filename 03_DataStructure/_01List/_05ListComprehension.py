# List of consonant character
str = input('Enter string: ')

consonants = [x for x in str if x not in "AEIOUaeiou"]
print(f"consonant list: {consonants}")

"""
Output:
        Enter string: NikolaTesla
        consonant list: ['N', 'k', 'l', 'T', 's', 'l']
"""