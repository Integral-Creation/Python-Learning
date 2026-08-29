# Python quiz game

quiz_questions = (
        "Which of the following data types is immutable?",
        "What is the correct way to start a function definition in Python?",
        "What does the 'len()' function do?",
        "Which keyword is used to handle exceptions in Python?",
        "What is the output of print(2 ** 3)?",
)


options = (("A) List", "B) Dictionary", "C) Tuple", "D) Set"),
           ("A) def myFunction():", "B) function myFunction()", "C) create myFunction():", "D) define myFunction()"),
           ("A) Returns the data type", "B) Returns the number of items in an object", "C) Converts an item to a string", "D) Rounds a number"),
           ("A) catch", "B) throw", "C) try", "D) except"),
           ("A) 6", "B) 8", "C) 9", "D) 5"))

answer = ("C", "A", "B", "D", "B")
guesses = []

score = 0
question_num = 0

for question in quiz_questions:
    print("-"*30)
    print(question)

    for option in options[question_num]:
        print(option)

    guess =  input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answer[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answer[question_num]} is correct answer")
    question_num += 1

print(f"Your Score is {score} / 5")