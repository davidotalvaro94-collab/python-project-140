
from brain_games.cli import welcome_user


def es_primo(n):
    if n < 2:
        return False, None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False, i  # devolvemos el divisor encontrado
    return True, None


def brain_prime():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while True:  # el juego se reinicia si hay un error
        aciertos = 0
        while aciertos < 3:
            numero = random.randint(1, 100)
            print(f"Question: {numero}")
            respuesta = input("Your answer: ").strip().lower()

            primo, divisor = es_primo(numero)

            if (primo and respuesta == "yes") or (not primo and respuesta == "no"):
                print("Correct!")
                aciertos += 1
            else:
                print(f"'{respuesta}' is wrong answer ;(. Let's try again, {name}!")
                if not primo:
                    if divisor:
                        print(f"Explanation: {numero} is not prime because it is divisible by {divisor}.")
                    else:
                        print(f"Explanation: {numero} is not prime because numbers less than 2 are not prime.")
                break  # rompe el ciclo y reinicia el juego

        if aciertos == 3:
            print(f"Congratulations, {name}!")
            break  # finaliza el juego al ganar


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
   

if __name__ == "__main__":
    main()