import random
import time # We'll use this for a dramatic pause!

def magic_eight_ball():
    ## 1. Define the possible answers
    # Create a list of eight ball responses
    responses = [
        "Yes, absolutely!",
        "It is decidedly so.",
        "Without a doubt.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]

    print("🔮 Welcome to the Magic Eight Ball! 🔮")
    print("Ask a YES or NO question (e.g., 'Will I have pizza tonight?').")

    # Start an infinite loop that runs until the user types 'exit'
    while True:
        ## 2. Get User Input
        question = input("\nYour Question (or type 'exit' to quit): ")

        if question.lower() == 'exit':
            print("Thanks for playing! Goodbye.")
            break # Exit the while loop

        if len(question.strip()) == 0:
            print("Please ask a question!")
            continue # Go back to the start of the loop

        ## 3. Choose and Display the Answer
        
        # 3a. Add dramatic flair!
        print("Shaking the ball...")
        time.sleep(1.5) # Pause the program for 1.5 seconds

        # Use random.choice() to pick one answer from the list
        answer = random.choice(responses)

        # 3b. Display the result
        print(f"\n✨ The Magic Eight Ball says: **{answer}**")

# Run the game
magic_eight_ball()
