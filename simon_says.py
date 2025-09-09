import random
import time
import os

def clear_screen():
    # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_sequence(length):
    print(f"Repeat the sequence by entering the letters (no spaces):")
    user_input = input(">")
    return user_input.lower()

def play():
    colors = ['r', 'g', 'b', 'y']  # red, green, blue, yellow
    color_names = {'r': 'Red', 'g': 'Green', 'b': 'Blue', 'y': 'Yellow'}
    sequence = []
    round_num = 1

    print("=== Simon Says Memory Game ===")
    print("Repeat the sequence of letters shown.")
    print("r=Red, g=Green, b=Blue, y=Yellow")
    print("Press Enter to start...")
    input()

    while True:
        clear_screen()
        print(f"Round {round_num}!")
        # Add a new random color to the sequence
        sequence.append(random.choice(colors))
        print("Watch the sequence:")
        for c in sequence:
            print(f"{color_names[c]}")
            time.sleep(0.8)
            clear_screen()
            time.sleep(0.2)
        # Get user input
        user_seq = get_user_sequence(len(sequence))
        if user_seq != ''.join(sequence):
            print("Wrong sequence! Game Over.")
            print(f"You reached round {round_num}.")
            print(f"The correct sequence was: {''.join(sequence)}")
            break
        else:
            print("Correct!")
            time.sleep(1)
            round_num += 1

if __name__ == "__main__":
    play()
