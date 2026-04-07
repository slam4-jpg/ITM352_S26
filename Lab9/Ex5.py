import json

quiz_questions = {
    "Hawaii": [
        {
            "question": "What is the capital of Hawaii?",
            "options": ["a) Maui", "b) Hilo", "c) Honolulu", "d) Lihue"],
            "answer": "c",
            "explanation": "Honolulu is the capital and largest city of Hawaii."
        },
        {
            "question": "What is the state fish of Hawaii?",
            "options": ["a) Ahi", "b) Humuhumunukunukuapua'a", "c) Mahimahi", "d) Moi"],
            "answer": "b",
            "explanation": "The Humuhumunukunukuapua'a is the official state fish of Hawaii."
        }
    ]
}

# Save dictionary to JSON file
with open("quiz_questions.json", "w") as file:
    json.dump(quiz_questions, file, indent=4)

print("Quiz questions saved to quiz_questions.json")