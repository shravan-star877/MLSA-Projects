# Ultimate Quiz Game
# multiple questions
# score tracking
# difficulty levels
# timer per question
# show fun fact after each question

import time

questions = [
    {"q": "What is the capital of France?", "a": "Paris", "fact": "Paris is called the City of Light."},
    {"q": "2 + 2 = ?", "a": "4", "fact": "Basic math builds strong logic skills."},
    {"q": "Who wrote Hamlet?", "a": "Shakespeare", "fact": "Shakespeare wrote 37 plays in total."}
]

score = 0

for q in questions:
    print(q["q"])
    start = time.time()
    ans = input("Your answer: ")
    end = time.time()

    if end - start > 10:
        print("⏰ Time’s up!")
    elif ans.strip().lower() == q["a"].lower():
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

    print("Fun fact:", q["fact"])
    print()

print(f"Your final score: {score}/{len(questions)}")