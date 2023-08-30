questions = (
    "What is the chemical symbol for the element with atomic number 1?: ",
    "Who wrote the novel '1984,' which is a dystopian exploration of totalitarianism and surveillance?: ",
    "Which river is the longest in the world?: ",
    "Which ancient wonder is known for its colossal size and historical significance, situated in Giza, Egypt?"
)

options = (
    ("A. Cl", "B. He", "C. O", "D. H"),
    ("A. George Orwell", "B. Aldous Huxley", "C. Ray Bradbury", "D. J.R.R. Tolkien"),
    ("A. Amazon River", "B. Nile River", "C. Yangtze River", "D. Mississippi River"),
    ("A. The Colosseum", "B. The Parthenon", "C. The Great Pyramid of Giza", "D. The Hanging Gardens of Babylon")
)

correct_answers = ("D", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    while True:
        guess = input("Enter (A, B, C, D): ").upper()

        if guess in ["A", "B", "C", "D"]:
            guesses.append(guess)
            if guess == correct_answers[question_num]:
                score += 1
                print("Correct")
                break
            else:
                print("Incorrect")
                print(f"{correct_answers[question_num]} is the correct answer")
                break
        else:
            print("Invalid input. Please enter A, B, C, or D.")

    question_num += 1

print("--------------------")
print("      RESULTS       ")
print("--------------------")

print("correct answers: ", end="")
for answer in correct_answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = (score / len(questions)) * 100
print(f"Your score is: {score_percentage:.2f}%")
