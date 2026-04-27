import random

def simulate_interest():
    responses = [
        ("Interested", random.randint(75, 100)),
        ("Neutral", random.randint(40, 70)),
        ("Not Interested", random.randint(0, 30))
    ]

    return random.choice(responses)