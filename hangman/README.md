# Hangman (CLI)

A command-line Hangman game — guess a randomly chosen word one letter
at a time before you run out of lives.

## How to Run

```bash
docker build -t hangman .
docker run -it --rm hangman
```

You have 6 lives. Each wrong guess costs one life and reveals more
of the hangman art. Guess the full word to win.

## Notes

- Core fundamentals: variables, lists, loops, and conditionals
- Using `while`/`for` loops to manage game state and build output
- String methods (`.lower()`, `.isalpha()`, `.join()`) for input handling
- Importing from a local module (`hangman_art.py`)
- Containerizing a Python app with Docker
