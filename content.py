import random

QUOTES = [
    "Believe in yourself and keep going.",
    "Small steps lead to big achievements.",
    "Never stop learning.",
    "Success comes from consistent effort.",
    "Every day is a new opportunity."
]

JOKES = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why was the math book sad? Because it had too many problems!",
    "What do computers eat? Microchips!",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake!"
]

FACTS = [
    "A day on Venus is longer than its year.",
    "Honey can remain preserved for a very long time.",
    "The human brain contains billions of neurons.",
    "Octopuses have three hearts.",
    "The Sun is a star."
]

def get_random_quote():
    return random.choice(QUOTES)

def get_random_joke():
    return random.choice(JOKES)

def get_random_fact():
    return random.choice(FACTS)
