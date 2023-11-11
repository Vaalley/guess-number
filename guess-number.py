import random
import time
from operator import add, sub, mul

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul
}

NUMBER_RANGES = {
    '*': (1, 10),
    '+': (1, 100),
    '-': (1, 100)
}

def generate_random_number(operator):
    return random.randint(*NUMBER_RANGES[operator])

def get_user_answer(equation):
    while True:
        try:
            return int(input(f"Solve the equation: {equation} = "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(num1, num2, operator_symbol, user_answer):
    correct_answer = OPERATORS[operator_symbol](num1, num2)
    return user_answer == correct_answer, correct_answer

def game_round():
    operator_symbol = random.choice(list(OPERATORS.keys()))
    num1 = generate_random_number(operator_symbol)
    num2 = generate_random_number(operator_symbol)
    equation = f"{num1} {operator_symbol} {num2}"
    user_answer = get_user_answer(equation)
    is_correct, correct_answer = check_answer(num1, num2, operator_symbol, user_answer)
    if is_correct:
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect! The correct answer was {correct_answer}.")
    return is_correct

def start_game():
    print("Hi and welcome to guess the number! In this game, you'll have to answer 10 math equations correctly as fast as possible.")
    input("Press Enter when you are ready to start...")

    correct_answers = 0
    with Timer() as t:
        for _ in range(10):
            if game_round():
                correct_answers += 1

    print_result(correct_answers, t.elapsed)

def print_result(correct_answers, time_taken):
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

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = self.end - self.start

if __name__ == "__main__":
    start_game()