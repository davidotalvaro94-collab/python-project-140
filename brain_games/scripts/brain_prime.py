import random

from brain_games.cli import welcome_user


def es_primo(n):
    if n < 2:
        return False, None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False, i
    return True, None


def brain_prime(name):

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while True:
        aciertos = 0
        while aciertos < 3:
            numero = random.randint(1, 100)
            print(f"Question: {numero}")
            respuesta = input("Your answer: ").strip().lower()

            primo, divisor = es_primo(numero)

            if ((primo and respuesta == "yes") or
                (not primo and respuesta == "no")):
                print("Correct!")
                aciertos += 1
            else:
                if (primo):
                    rta = "yes"

                if (not primo):
                    rta = "no"

                print((
                    f"'{respuesta}' is wrong answer ;(. "
                    f"Correct answer was '{rta}'."
                ))
                print(f"Let's try again, {name}!")
                exit()

        if aciertos == 3:
            print(f"Congratulations, {name}!")
            break


def main():
    name = welcome_user()
    brain_prime(name)
   

if __name__ == "__main__":
    main()