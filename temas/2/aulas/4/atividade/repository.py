import json


def init():
    try:
        file = open('students.json', 'xt')
    except FileExistsError:
        file = open('students.json', 'wt')
    finally:
        file.write('[]')
        file.close()


def getStudents():
    try:
        file = open('students.json', 'r')

    except FileNotFoundError:
        init()
        file = open('students.json', 'r')

    jsonString = file.read()
    file.close()

    students = json.loads(jsonString)
    return students


def showStudent(student):
    print(f'\nnome: {student["name"]}')
    print(f'email: {student["email"]}')
    print(f'curso: {student["course"]}\n')


def showStudents():
    students = getStudents()
    if (len(students) == 0):
        return print('Nenhum aluno cadastrado.')

    for student in students:
        showStudent(student)


def registerStudent():
    name = input('Digite o nome do aluno: ')
    email = input('Digite o email do aluno: ')
    course = input('Digite o curso do aluno: ')

    student = {'name': name, 'email': email, 'course': course}

    students = getStudents()
    students.append(student)
    studentsJson = json.dumps(students)

    file = open('students.json', 'w')
    file.write(studentsJson)
    print('\nAluno criado com sucesso:\n')
    showStudent(student)
    file.close()


def searchStudent():
    students = getStudents()
    name = input('Digite o nome do estudante: ')
    selectedStudent = {}
    for student in students:
        if (name in student['name']):
            selectedStudent = student
            break

    if (len(selectedStudent) == 0):
        return print('Estudante em falta')

    showStudent(selectedStudent)
