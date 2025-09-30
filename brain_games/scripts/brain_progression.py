import random

from brain_games.cli import welcome_user


def arithmetic_progression_game(name):

    rounds = 3
    print("What number is missing in the progression?")

    for _ in range(rounds):
        length = random.randint(5, 10)  
        start = random.randint(1, 20)
        diff = random.randint(1, 9)  

        prog = [start + i * diff for i in range(length)]
        missing_index = random.randint(0, length - 1)

        display_prog = []
        for i, v in enumerate(prog):
            if i == missing_index:
                display_prog.append("..")
            else:
                display_prog.append(str(v))

        print("Question:", " ".join(display_prog))
        answer = input("Your answer: ").strip()

        correct = prog[missing_index]

        try:
            user_ans = int(answer)
        except ValueError:
            user_ans = None

        if user_ans == correct:
            print("Correct!")
        else:
            print("Question:", " ".join(display_prog))
            print(f"Your answer: {answer}")
            print((
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            ))
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    arithmetic_progression_game(name)


if __name__ == "__main__":
    main()