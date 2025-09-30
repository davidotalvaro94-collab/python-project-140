import random

from brain_games.cli import welcome_user


def par_o_impar(name):

    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while n < 3: 
        i = random.randint(1, 100)
        print("Question: " + str(i))
        answer = input("Your answer: ")

        if i % 2 == 0:
            if answer == "yes":
        
                print("Correct!")
                n += 1
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}")
                exit()
        else:
            if answer == "no":
        
                print("Correct!")
                n += 1
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                exit()

    print("Congratulations, " + name + "!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    par_o_impar(name)


if __name__ == "__main__":
    main()