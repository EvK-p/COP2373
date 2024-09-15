# Set python for the random module
import random

# Define the responses for the 8ball
def responses_file():
    responses = [
        "Yes, of course!", 
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]

    # Create and write the '8ball_responses.txt' file
    with open('8ball_responses.txt', 'w') as file:
        for response in responses:
            file.write(response + '\n')

# Simulate the 8ball
def magic_8_ball():
    # Read responses from the file
    with open('8ball_responses.txt', 'r') as file:
        responses = file.readlines()

    print('Welcome to 8Ball! Ask the 8Ball your yes or no question, or type "quit" to quit the program. \n')

    while True:
        question = input("What will you ask the 8ball?: ")

        if question.lower() == 'quit':
            print('Thank you for playing 8ball!')
            break

        # Randomize a response
        response = random.choice(responses)
        print(f"8Ball says:\n {response}\n")

# Call back to the mains
responses_file()
magic_8_ball()








