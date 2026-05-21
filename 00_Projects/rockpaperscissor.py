import random

choices = ['Rock', 'Paper', 'Scissor']

print("🎮 Welcome to Rock Paper Scissors Game 🎮")

while True:
    usercount = 0
    computercount = 0

    start = int(input("""
Do you want to start the game?
1. YES
2. NO | EXIT
>>> """))

    if start != 1:
        print("Thanks for playing! 👋")
        break

    win_points = int(input("\nEnter points needed to WIN the game: "))
    print(f"\n🔥 First player to reach {win_points} points wins the game! 🔥\n")

    round_no = 1

    while usercount < win_points and computercount < win_points:
        print(f"\n--- Round {round_no} ---")

        userInput = int(input("""
Enter your choice:
1. Rock
2. Paper
3. Scissor
>>> """))

        if userInput not in [1, 2, 3]:
            print("❌ Invalid choice! Try again.")
            continue

        userChoice = choices[userInput - 1]
        computerChoice = random.choice(choices)

        print(f"Computer chose: {computerChoice}")
        print(f"You chose: {userChoice}")

        if userChoice == computerChoice:
            print("🤝 It's a Tie!")
        elif (userChoice == 'Rock' and computerChoice == 'Scissor') or \
             (userChoice == 'Paper' and computerChoice == 'Rock') or \
             (userChoice == 'Scissor' and computerChoice == 'Paper'):
            print("🎉 You WIN this round!")
            usercount += 1
        else:
            print("💥 You LOSE this round!")
            computercount += 1

        print(f"📊 Score → You: {usercount} | Computer: {computercount}")

        # Suspense messages
        if usercount == win_points - 1:
            print("🔥 MATCH POINT! One more point to WIN!")
        elif computercount == win_points - 1:
            print("⚠️ Computer is at MATCH POINT! Be careful!")

        round_no += 1

    # Final Result
    print("\n🏁 GAME OVER 🏁")
    if usercount > computercount:
        print("🏆 CONGRATULATIONS! You won the game!")
    else:
        print("😢 Sorry! Computer won the game.")

    print(f"Final Score → You: {usercount} | Computer: {computercount}")
    print("Thanks for playing! 👋\n")