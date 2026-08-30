"""
    Random
    In python Random is a built-in module used to generate the random numbers and make a random selections.
"""
import random

""" 1. random.randint()"""
num = random.randint(1, 10)
print(num) # it generate numbers from 1 to 10

""" 2. random.randrange()"""
num = random.randrange(1, 10)
print(num) # it generate number from 1 to 9 (10 is inclusive)

skip_num = random.randrange(0, 20, 2)
print(skip_num) # possible values 0 , 2, 4, 6,..., 18

""" 3. random.random()"""
num = random.random()
print(num) # returns float btw 0.0 and 1.0

""" 4. random.choice()"""
options = ("rock", "paper", "scissors")
choice = random.choice(options)
print(choice)

""" 5. random.shuffle()"""
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)

print(cards) # ['2', '8', '4', '3', '9', 'A', 'Q', '7', 'K', '6', '10', 'J', '5'] it shuffles the cards

""" 6. random.sample"""
sample = random.sample(cards, 4)
print(sample) # ['K', '10', '6', '2'] # it selects the multiple items randomly