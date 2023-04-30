
import random

while True:
    u_c= input("Enter a choice (rock, paper, scissor): ")
    p_c = ["rock", "paper", "scissor"]
    c_c = random.choice(p_c)
    print(f"\nYou chose {u_c}, computer chose {c_c}.\n")

    if u_c == c_c:
        print("It's a tie!")
    elif u_c == "rock":
        if c_c == "scissor":
            print("Rock smashes scissor, You win!")
        else:
            print("Paper covers rock,You lose.")
    elif u_c == "paper":
        if c_c== "rock":
            print("Paper covers rock,You win!")
        else:
            print("Scissor cuts paper,You lose.")
    elif u_c == "scissor":
        if c_c == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors,You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
print("Thanks For Playing")