import os


def clear() -> None:
    os.system('clear')


def enterToContinue() -> None:
    input('\nDigite Enter para continuar...')


def inputWithValidation(text, validator) -> str:
    while True:
        value = input(text)
        error = validator(value)
        if (error == None):
            break

        print(f'\n{error}\n')

    return value
