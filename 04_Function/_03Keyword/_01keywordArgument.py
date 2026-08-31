"""
    keyword argument
        an argument preceded by an identifier
        helps with readability 
        order of argument doesn't matter
"""

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", first="Nikola", last="Tesla") # Hello Mr.Nikola Tesla
# here `title` is keyword argument