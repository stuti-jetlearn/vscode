import tkinter as tk

# Questions and answers
questions = [
    ("What is 7 + 5?", "12"),
    ("What is 9 - 4?", "5"),
    ("What is 6 × 3?", "18"),
    ("What is 15 ÷ 3?", "5"),
    ("What is 10 + 8?", "18")
]

current_question = 0
score = 0

def check_answer():
    global current_question, score
    user_answer = entry.get()
    
    # Check answer
    if user_answer == questions[current_question][1]:
        result_label.config(text="Correct! 🎉", fg="green")
        score += 1
    else:
        result_label.config(text=f"Wrong ❌ (Answer: {questions[current_question][1]})", fg="red")
    
    # Move to next question
    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        end_quiz()

def show_question():
    entry.delete(0, tk.END)  # clear entry
    question_label.config(text=questions[current_question][0])

def end_quiz():
    question_label.config(text="Quiz Over!")
    entry.destroy()
    submit_button.destroy()
    result_label.config(text=f"Your Score: {score}/{len(questions)}", fg="blue")

# Create main window
root = tk.Tk()
root.title("Math Quiz App")

# Question Label
question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start quiz
show_question()

root.mainloop()
