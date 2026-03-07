#Quiz game. Third Version.
#Name: Sidney Lam
#Date: February 24,2026
# Make a list with the questions and correct answers
# Make questions a dictionary with questions as keys and correct answers as values

questions = {
    "What is the airspeed of an unladen swallow in miles/hr? ": ["12", "10", "15"],
    "What is the capital of Texas? ": ["Austin", "Houston", "Dallas"],
    "The Last Supper was painted by which Artist? ": ["Da Vinci", "Michelangelo", "Raphael"],
}

for question, options in questions.items():
    correct_answer = options[0] # The First option is the correct answer
    for alternative in options:
        print(f"- {alternative}")

    answer = input(question +":")
    if answer == correct_answer:
        print("Correct!")
    else:   
        print(f"Incorrect. The correct answer is {correct_answer!r} not {answer!r}")


