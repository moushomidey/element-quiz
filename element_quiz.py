"""Element Symbol Quiz

A simple terminal quiz that tests chemical element symbols.
Written as one of my first Python projects while moving from
science teaching into software engineering.
"""

import random

# A dictionary: each element name (the "key") is paired
# with its chemical symbol (the "value").
ELEMENTS = {
    "Hydrogen": "H",
    "Helium": "He",
    "Lithium": "Li",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Sodium": "Na",
    "Magnesium": "Mg",
    "Chlorine": "Cl",
    "Potassium": "K",
    "Calcium": "Ca",
    "Iron": "Fe",
}


def ask_question(element, correct_symbol):
    """Ask one question. Returns True if the answer was right."""
    answer = input(f"What is the symbol for {element}? ")

    # .strip() removes accidental spaces, so " O " still counts as "O".
    # We compare exactly, because capital letters matter in chemistry:
    # CO is carbon monoxide, Co is cobalt!
    if answer.strip() == correct_symbol:
        print("Correct!\n")
        return True
    else:
        print(f"Not quite - the answer is {correct_symbol}.\n")
        return false 
    


def run_quiz(number_of_questions):
    """Run the quiz and return the final score."""
    score = 0

    # Pick random elements from the dictionary, no repeats.
    element_names = random.sample(list(ELEMENTS.keys()), number_of_questions)

    for element in element_names:
        correct_symbol = ELEMENTS[element]
        if ask_question(element, correct_symbol):
            score = score + 1

    return score


def main():
    print("=== Element Symbol Quiz ===")
    print("Capital letters matter! (e.g. He, not HE or he)\n")

    total = 10
    score = run_quiz(total)

    print(f"You scored {score} out of {total}.")

    # Give feedback based on the score.
    if score == total:
        print("Perfect - full marks!")
    elif score >= total / 2:
        print("Good effort - keep practising.")
    else:
        print("Have another go - practice makes perfect.")


# This line means: only start the quiz when this file is run directly.
if __name__ == "__main__":
    main()
