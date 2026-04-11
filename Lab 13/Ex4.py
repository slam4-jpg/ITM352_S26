from flask import Blueprint, render_template, request

quiz_route = Blueprint('quiz_route', __name__, template_folder='templates')

questions = [
    {
        "question": "What is the capital of Hawaii?",
        "options": ["Maui", "Honolulu", "Hilo", "Kauai"],
        "answer": "Honolulu"
    },
    {
        "question": "What is the state fish of Hawaii?",
            "options": ["a) Ahi", "b) Humuhumunukunukuapua'a", "c) Mahimahi", "d) Moi"],
            "answer": "Humuhumunukunukuapua",
    }
]

@quiz_route.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            selected = request.form.get(f"q{i}")
            if selected == q["answer"]:
                score += 1
        return render_template("quiz_result.html", score=score, total=len(questions))
    return render_template("quiz.html", questions=questions)