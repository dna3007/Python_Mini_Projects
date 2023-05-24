# List of questions and answers with points
questions = [
    ("What is the capital of France?", "Paris", 1),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci", 2),
    ("What is the largest planet in our solar system?", "Jupiter", 1),
    ("What is the boiling point of water in Celsius?", "100", 2),
    ("Which animal is known as the 'King of the Jungle'?", "Lion", 1),
    ("What is the chemical symbol for gold?", "Au", 2),
    ("Who wrote the novel 'Pride and Prejudice'?", "Jane Austen", 2),
    ("Which country is home to the kangaroo?", "Australia", 1),
    ("What is the tallest mountain in the world?", "Mount Everest", 2),
    ("Who is the Greek god of the sea?", "Poseidon", 1)
]


# Function to ask all the questions and calculate total points
def quiz():
    total_points = 0

    # Iterate through each question
    for question, answer, points in questions:
        # Prompt the user for an answer
        user_answer = input(question + " ")

        # Check the answer
        if user_answer.lower() == answer.lower():
            print("Correct! You earned", points, "point(s).")
            total_points += points
        else:
            print("Incorrect. The correct answer is:", answer)

    return total_points


# Main program
print("Welcome to the Quiz!")
print("Please answer the following questions:")
print()

total_points = quiz()

print("Thank you for playing the quiz!")
print("Your total points:", total_points ,"/15")
