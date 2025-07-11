import random
from app.questions import get_questions
from app.utils import ask_question, show_score

def start_game():
    print("\n🧠 Welcome to the Python Trivia Game! 🐍\n")
    questions = get_questions()
    total_questions = 5
    score = 0
    selected_questions = random.sample(list(questions.items()), total_questions)

    for idx, (question, answer) in enumerate(selected_questions, 1):
        print(f"Question {idx}:")
        if ask_question(question, answer):
            score += 1

    show_score(score, total_questions)