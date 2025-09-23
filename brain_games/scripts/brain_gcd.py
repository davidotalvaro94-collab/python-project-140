import math
import random


from brain_games.cli import welcome_user


def MDC(rounds=3):

    name = input("Welcome to the Brain Games!\nMay I have your name? ").strip()

    if not name:
        name = "Player"
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    for _ in range(rounds):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        correct = math.gcd(a, b)

        print(f"Question: {a} {b}")
        answer = input("Your answer: ").strip()

        try:
            user_ans = int(answer)
        except ValueError:
            user_ans = None

        if user_ans == correct:
            print("Correct!")
        else:
            print(f"Question: {a} {b}")
            print(f"Your answer: {answer}")
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    #MCD(name)


if __name__ == "__main__":
    main()