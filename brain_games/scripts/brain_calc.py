import random

from brain_games.cli import welcome_user


def calculadora(name):

    operators = ["+", "-", "*"]

    correct_answers = 0

    while correct_answers < 3:
        
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(operators)

        expression = f"{num1} {operator} {num2}"

        correct_result = eval(expression)

        print("What is the result of the expression?")
        print(f"Question: {expression}")
        answer = input("Your answer: ")

        if (not answer.isdigit() and 
            not (answer.startswith('-') and answer[1:].isdigit())):
            print((
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_result}'."
            ))
            print(f"Let's try again, {name}!")
            return

        answer = int(answer)

        if answer == correct_result:
            print("Correct!")
            correct_answers += 1
        else:
            print((
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_result}'."
            ))
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    calculadora(name)


if __name__ == "__main__":
    main()