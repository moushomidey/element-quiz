# element-quiz

A terminal-based chemistry quiz written in Python — one of my first coding
projects as I move from science teaching into software engineering.

The quiz asks 5 random element symbol questions, checks answers (capital
letters matter — CO is carbon monoxide, Co is cobalt!), keeps score, and
gives feedback at the end.

## How to run

```bash
python element_quiz.py
```

No installation needed — it only uses Python's built-in `random` module.

## What it uses

- A **dictionary** to store elements and their symbols
- **Functions** to keep the code organised
- A **for loop** to work through the questions
- **if/elif/else** to check answers and choose feedback
- `random.sample` to pick questions without repeats

## Why I built it

As a chemistry teacher I quizzed students on element symbols constantly.
Building the tool myself was a way to practise Python fundamentals on a
problem I understood inside out.

## Next steps

- Let the player choose how many questions to answer
- Add a "hard mode" going the other way (symbol → name)
- Keep a high score between games by saving to a file
