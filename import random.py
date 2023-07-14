import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer = num1 // num2  # Use integer division to avoid float answers
    
    question = f"What is {num1} {operator} {num2}?"
    return question, answer

def main():
    print("Welcome to the Maths Game!")
    score = 0

    while True:
        question, correct_answer = generate_question()
        print(question)
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
            print(f"Your final score: {score}")
            break
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Your final score: {score}")
            break

if __name__ == "__main__":
    main()
