# Simon Says - Python Memory Game

This is a simple command-line "Simon Says" memory game written in Python. The game challenges you to remember and repeat an ever-growing sequence of colors using the keyboard.

## How to Play

1. **Run the game**:  
   ```bash
   python simon_says.py
   ```

2. **Instructions**:
   - The game will display a sequence of colors (Red, Green, Blue, Yellow), represented by their first letters:  
     - `r` = Red  
     - `g` = Green  
     - `b` = Blue  
     - `y` = Yellow  
   - Watch the sequence as it appears, and try to memorize the order.
   - After the sequence is shown, type the sequence back using the letters (no spaces) and press Enter.
   - Each round, the sequence gets longer. See how many rounds you can survive!

3. **End of Game**:
   - The game ends when you enter the wrong sequence. Your final score (the round you reached) will be displayed.

## Example

```
=== Simon Says Memory Game ===
Repeat the sequence of letters shown.
r=Red, g=Green, b=Blue, y=Yellow
Press Enter to start...

Round 1!
Watch the sequence:
Red

Repeat the sequence by entering the letters (no spaces):
> r

Correct!
...
```

## Requirements

- Python 3.x

## Notes

- This game runs in the terminal/command prompt.
- Works cross-platform (Windows, macOS, Linux).

## License

This project is provided for educational purposes.

