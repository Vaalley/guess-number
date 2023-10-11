import random
import time

# Function to prompt the user for exiting the game
def exit_game_prompt():
    print("Exiting in 3 seconds...")
    time.sleep(3)
    exit()

# Function to start the game
def start_game():
    # Initialize the number of correct answers to 0
    correct_answers = 0
    
    # Start the timer
    start_time = time.time()
    
    for _ in range(10):
        # Generate two random numbers between 1 and 100
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        # Generate a random operator (+, -, *)
        operator = random.choice(['+', '-', '*'])
        
        # Calculate the correct answer
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            # Generate two different random numbers between 1 and 10 for multiplication
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            correct_answer = num1 * num2
            
        # Create the equation string
        equation = f"{num1} {operator} {num2}"
        
        # Ask the user to solve the equation
        user_answer = int(input(f"Solve the equation: {equation} = "))
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("✅ Correct!")
            correct_answers += 1
        else:
            print("❌ Incorrect!")
    
    # Calculate the time taken to answer the questions
    end_time = time.time()
    time_taken = end_time - start_time
    
    if correct_answers == 10:
        print("🏆 You got all the equations correct!")
    elif correct_answers > 5:
        print(f"🎉 You got {correct_answers} out of 10 equations correct!")
    else:
        print(f"😔 You got only {correct_answers} out of 10 equations correct!")
    
    # Display the time taken
    print(f"⏰ Time taken: {time_taken:.2f} seconds")

if __name__ == "__main__":
    print("Hi and welcome to guess the number! In this game, you'll have to answer 10 math equations correctly as fast as possible.")
    print("Are you ready to start the game? (y/n)")
    user_input = input("")
    
    if user_input == "y":
        start_game()
    elif user_input == "n":
        exit_game_prompt()
    else:
        print("Invalid input, please try again")