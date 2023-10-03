import os


def clear():
    os.system('clear')


def enterToContinue():
    input('\nDigite Enter para continuar...')


def inputWithValidation(text, validator):
    while True:
        value = input(text)
        error = validator(value)
        if (error == None):
            break

        print(f'\n{error}\n')

    return value
