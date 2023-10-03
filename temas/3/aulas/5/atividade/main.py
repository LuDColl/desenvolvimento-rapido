import repository
import helper

repository.init()
choices = [repository.registerStudent,
           repository.showStudents, repository.searchStudent]


while True:
    helper.clear()
    try:
        choice = input(
            """1 - Cadastrar novo aluno;
2 - Listar alunos cadastrados;
3 - Buscar um aluno pelo nome;

0 - Sair\n\n"""
        )
    except KeyboardInterrupt:
        helper.clear()
        print('Escolha a opção 0 caso queira sair.')
        helper.enterToContinue()
        continue

    helper.clear()
    choice = choice.strip()

    try:
        choice = int(choice)
    except ValueError:
        print(f'{choice} não é um escolha.')
        helper.enterToContinue()
        continue

    if (choice == 0):
        print('Saindo...')
        break

    try:
        selectedChoice = choices[choice - 1]
        selectedChoice()
        helper.enterToContinue()
    except IndexError:
        print(f'{choice} não é uma escolha válida.')
        helper.enterToContinue()
