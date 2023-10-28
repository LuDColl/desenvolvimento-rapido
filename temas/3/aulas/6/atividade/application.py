import repository
import helper

_choices = [repository.registerStudent,
            repository.showStudents, repository.searchStudent]


def start():
    while True:
        close = _execution()
        if close:
            break


def _execution():
    try:
        return choice()
    except KeyboardInterrupt:
        helper.clear()
        print('Escolha a opção 0 caso queira sair.')
        helper.enterToContinue()


def choice() -> bool:
    choice = input(
        """
1 - Cadastrar novo aluno;
2 - Listar alunos cadastrados;
3 - Buscar um aluno pelo nome;

0 - Sair

"""
    )

    helper.clear()
    choice = choice.strip()

    try:
        choice = int(choice)
    except ValueError:
        print(f'{choice} não é um escolha.')
        helper.enterToContinue()
        return

    if (choice == 0):
        print('Saindo...')
        return True

    try:
        selectedChoice = _choices[choice - 1]
        selectedChoice()
        helper.enterToContinue()
    except IndexError:
        print(f'{choice} não é uma escolha válida.')
        helper.enterToContinue()
