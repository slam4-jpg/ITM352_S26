#Quiz game. Fifth Version.
#Name: Sidney Lam
#Date: February 24,2026
# Make a list with the questions and correct answers
# Make questions a dictionary with questions as keys and correct answers as values
#Allow the user tp select the correct answer by a label 
# Improve look and useabloty. Keepy track of correct ansers 

from string import ascii_lowercase

questions = {
    "What is the airspeed of an unladen swallow in miles/hr? ": ["12", "10", "15"],
    "What is the capital of Texas? ": ["Austin", "Houston", "Dallas"],
    "The Last Supper was painted by which Artist? ": ["Da Vinci", "Michelangelo", "Raphael"],
}

num_correct = 0
for num, (question, options) in enumerate(questions.items(), start=1):
    print(f"Question {num}:")
    print(question)
    correct_answer = options[0] # The First option is the correct answer
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(options))) # Label the options with letters
    for label, alternative in labeled_alternatives.items():
        print(f"{label}. {alternative}")
    
    answer_label = input("Choice? ")
    answer = labeled_alternatives[answer_label] # Get the answer based on the label
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:   
        print(f"Incorrect. The correct answer is {correct_answer!r} not {answer!r}")  

print(f"You got {num_correct} out of {len(questions)} correct.")      
                    
   