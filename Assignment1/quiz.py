import json
import os
import random



def load_questions(category):
    """Load questions from a JSON file based on category."""
    with open("quiz_questions.json", "r") as file:
        all_questions = json.load(file)
    return all_questions.get(category, [])


def ask_question(question_data, lifeline_used):
    """Ask a multiple-choice question and return score and lifeline status."""

    print("\n" + question_data["question"])

    options = question_data["options"].copy()

    for option in options:
        print(option)

    while True:
        answer = input("Enter your answer (a, b, c, d) or type 50 for 50/50: ").lower()

        if answer == "50":

            if lifeline_used:
                print("50/50 already used!")
                continue

            correct = question_data["answer"]

            wrong = [o[0] for o in options if o[0] != correct]

            remove = random.sample(wrong, 2)

            print("\nRemaining options:")

            for option in options:
                if option[0] not in remove:
                    print(option)

            lifeline_used = True
            continue

        if answer in ['a', 'b', 'c', 'd']:
            break

        print("Invalid choice. Please enter a, b, c, d, or 50.")

    if answer == question_data["answer"]:
        print("Correct!", question_data["explanation"])
        return 1, lifeline_used
    else:
        print(f"Incorrect. The correct answer is {question_data['answer']}.", question_data["explanation"])
        return 0, lifeline_used


def save_high_scores(scores):
    """Save high scores to a file."""
    with open("high_scores.json", "w") as file:
        json.dump(scores, file)


def load_high_scores():
    """Load high scores from a file."""
    if not os.path.exists("high_scores.json"):
        return {}

    with open("high_scores.json", "r") as file:
        return json.load(file)


def run_quiz():
    """Run the quiz game."""

    username = input("Enter your username: ")
    scores = load_high_scores()

    categories = {"1": "Hawaii", "2": "UH Manoa"}

    print("Choose a quiz category:")
    for key, value in categories.items():
        print(f"{key}. {value}")

    while True:
        category_choice = input("Enter the number of your choice: ")

        if category_choice in categories:
            category = categories[category_choice]
            break

        print("Invalid choice. Please enter 1 or 2.")

    questions = load_questions(category)

    score = 0
    lifeline_used = False

    for q in questions:
        points, lifeline_used = ask_question(q, lifeline_used)
        score += points

    print(f"\nQuiz Complete! Your final score: {score}/{len(questions)}")

    # Update high scores
    if username in scores:
        scores[username] = max(scores[username], score)
    else:
        scores[username] = score

    save_high_scores(scores)

    # Display grand champion
    grand_champion = max(scores, key=scores.get)
    print(f"Grand Champion: {grand_champion} with {scores[grand_champion]} points!")


if __name__ == "__main__":
    run_quiz()



# save score history
def save_score(score, total):
    
    with open("score_history.txt", "a") as file:
        file.write(f"Score: {score}/{total}\n")

