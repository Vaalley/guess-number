import random
import time
import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

def generate_and_check_equation():
    # Generate a random operator (+, -, *)
    operator_symbol = random.choice(list(OPERATORS.keys()))

    # Generate two random numbers
    # For multiplication, numbers are between 1 and 10
    # For addition and subtraction, numbers are between 1 and 100
    if operator_symbol == '*':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

    # Calculate the correct answer
    correct_answer = OPERATORS[operator_symbol](num1, num2)

    # Create the equation string
    equation = f"{num1} {operator_symbol} {num2}"

    # Ask the user to solve the equation
    while True:
        try:
            user_answer = int(input(f"Solve the equation: {equation} = "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Check if the user's answer is correct
    return user_answer == correct_answer


def start_game():
    # Initialize the number of correct answers to 0
    correct_answers = 0

    # Start the timer
    with Timer() as t:
        for _ in range(10):
            if generate_and_check_equation():
                print("✅ Correct!")
                correct_answers += 1
            else:
                print("❌ Incorrect!")

    print_result(correct_answers, t.elapsed)

def print_result(correct_answers, time_taken):
    # Print the results
    if correct_answers == 10:
        print("🏆 You got all the equations correct!")
    elif correct_answers > 5:
        print(f"🎉 You got {correct_answers} out of 10 equations correct!")
    else:
        print(f"😔 You got only {correct_answers} out of 10 equations correct!")
    print(f"⏰ Time taken: {time_taken:.2f} seconds")

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.elapsed = self.end - self.start

if __name__ == "__main__":
    print("Hi and welcome to guess the number! In this game, you'll have to answer 10 math equations correctly as fast as possible.")
    while True:
        user_input = input("Are you ready to start the game? (y/n) ")
        if user_input.lower() == "y":
            start_game()
        elif user_input.lower() == "n":
            print("Exiting in 3 seconds...")
            time.sleep(3)
            break
        else:
            print("Invalid input, please try again")
