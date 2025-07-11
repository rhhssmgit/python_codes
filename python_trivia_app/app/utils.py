def show_score(score, total):
    print("========================")
    print(f"🎯 Your Final Score: {score}/{total}")
    print("========================")

def ask_question(question, correct_answer):
    user_answer = input(f"{question}\nYour answer: ").lower().strip()
    if user_answer == correct_answer.lower():
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Wrong. The correct answer is: {correct_answer}\n")
        return False