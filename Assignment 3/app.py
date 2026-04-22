from flask import Flask, render_template, request, redirect, url_for, session
import json
import random
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'
QUESTIONS_FILE = DATA_DIR / 'questions.json'
LEADERBOARD_FILE = BASE_DIR / 'scores.json'
LEGACY_LEADERBOARD_FILE = DATA_DIR / 'leaderboard.json'
TEMPLATES_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'

app = Flask(__name__, template_folder=str(TEMPLATES_DIR), static_folder=str(STATIC_DIR))
app.secret_key = 'supersecretkey'
app.permanent_session_lifetime = timedelta(days=7)

def build_hint(question):
    hint = question.get('hint')
    if hint:
        return hint

    explanation = question.get('explanation', '').strip()
    if explanation:
        return explanation

    answer = question.get('answer', '').strip()
    if answer:
        return f"The correct choice starts with '{answer}'."

    return "Think carefully about the choices and eliminate the least likely answers."

def build_hint(question):
    # If a hint is provided in JSON, use it
    hint = question.get('hint')
    if hint:
        return hint

    # Otherwise generate a generic hint that does NOT reveal the answer
    difficulty = question.get('difficulty', 'Medium')

    if difficulty == "Easy":
        return "Think about common knowledge or well-known facts."

    elif difficulty == "Medium":
        return "Consider what you learned in class or general background knowledge."

    elif difficulty == "Hard":
        return "This question may require specific knowledge or careful reasoning."

    return "Try eliminating the least likely answers."

# Load all categories and difficulty levels from JSON
def load_questions(category, difficulty):
    with QUESTIONS_FILE.open() as f:
        all_categories = json.load(f)

    questions = all_categories.get(category, [])

    # Only keep questions that match the selected difficulty
    filtered = [
        q for q in questions
        if q.get('difficulty', '').strip().lower() == difficulty.strip().lower()
    ]

    random.shuffle(filtered)

    for q in filtered:
        q['hint'] = build_hint(q)
        random.shuffle(q['options'])

    return filtered

def load_leaderboard():
    try:
        with LEADERBOARD_FILE.open() as f:
            return json.load(f)
    except Exception:
        try:
            with LEGACY_LEADERBOARD_FILE.open() as f:
                return json.load(f)
        except Exception:
            return []

def save_leaderboard(lb):
    with LEADERBOARD_FILE.open('w') as f:
        json.dump(lb, f, indent=4)

@app.route('/')
def index():
    username = session.get('username')
    selected_category = session.get('category')
    selected_difficulty = session.get('difficulty', 'Easy')
    with QUESTIONS_FILE.open() as f:
        all_categories = json.load(f)
    categories = sorted(all_categories.keys())
    return render_template(
        'index.html',
        username=username,
        categories=categories,
        selected_category=selected_category,
        selected_difficulty=selected_difficulty
    )

@app.route('/set_username', methods=['POST'])
def set_username():
    session.permanent = True
    session['username'] = request.form['username']
    session['category'] = request.form['category']
    session['difficulty'] = request.form['difficulty']
    session['questions'] = load_questions(session['category'], session['difficulty'])

    if not session['questions']:
        session.pop('questions', None)
        return redirect(url_for('index'))

    session['q_index'] = 0
    session['score'] = 0
    session['hint_used'] = False
    return redirect(url_for('quiz'))

@app.route('/start_quiz')
def start_quiz():
    username = session.get('username')
    category = session.get('category')
    difficulty = session.get('difficulty', 'Easy')

    if not username or not category:
        return redirect(url_for('index'))

    session['questions'] = load_questions(category, difficulty)

    if not session['questions']:
        session.pop('questions', None)
        return redirect(url_for('index'))

    session['q_index'] = 0
    session['score'] = 0
    session['hint_used'] = False
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    q_index = session.get('q_index', 0)
    questions = session.get('questions', [])

    if q_index >= len(questions):
        return redirect(url_for('result'))

    question = questions[q_index]
    progress = (q_index / len(questions)) * 100

    return render_template('quiz.html',
                           question=question,
                           q_index=q_index,
                           total_questions=len(questions),
                           progress=progress)

@app.route('/next', methods=['POST'])
def next_question():
    questions = session.get('questions', [])
    q_index = session.get('q_index', 0)
    selected_answer = request.form.get('selected_answer')

    if q_index < len(questions):
        correct_answer = questions[q_index].get('answer')
        if selected_answer == correct_answer:
            session['score'] += 1

    session['q_index'] += 1
    return redirect(url_for('quiz'))

@app.route('/use_hint')
def use_hint():
    if not session.get('hint_used'):
        session['hint_used'] = True
        session['score'] = max(0, session['score'] - 1)
    return ('', 204)

@app.route('/result')
def result():
    username = session.get('username', 'Anonymous')
    score = session.get('score', 0)
    questions = session.get('questions', [])
    total = len(questions)

    leaderboard = load_leaderboard()
    leaderboard.append({'username': username, 'score': score})
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    leaderboard = leaderboard[:10]
    save_leaderboard(leaderboard)

    return render_template('result.html',
                           username=username,
                           score=score,
                           total=total,
                           leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
