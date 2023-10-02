import json
import helper
import validators
import re


def init():
    try:
        file = open('students.json', 'xt')
    except FileExistsError:
        file = open('students.json', 'wt')
    finally:
        file.write('[]')
        file.close()


def showStudents():
    students = __getStudents()
    if (len(students) == 0):
        return print('Nenhum aluno cadastrado.')

    for student in students:
        __showStudent(student)


def registerStudent():
    registration = helper.inputWithValidation(
        'Digite a matricula do aluno: ', __registrationValidator)
    name = helper.inputWithValidation(
        'Digite o nome do aluno: ', __nameValidator)
    email = helper.inputWithValidation(
        'Digite o email do aluno: ', validators.required('Email obrigatorio.'))
    course = helper.inputWithValidation(
        'Digite o curso do aluno: ', validators.required('Curso obrigatorio.'))

    student = {'registration': registration,
               'name': name, 'email': email, 'course': course}

    students = __getStudents()
    students.append(student)
    studentsJson = json.dumps(students)

    file = open('students.json', 'w')
    file.write(studentsJson)
    print('\nAluno criado com sucesso:\n')
    __showStudent(student)
    file.close()


def searchStudent():
    students = __getStudents()
    name = input('Digite o nome do estudante: ')
    selectedStudent = {}
    for student in students:
        if (name in student['name']):
            selectedStudent = student
            break

    if (len(selectedStudent) == 0):
        return print('Estudante em falta')

    __showStudent(selectedStudent)


def __getStudents():
    try:
        file = open('students.json', 'r')
    except FileNotFoundError:
        init()
        file = open('students.json', 'r')

    jsonString = file.read()
    file.close()

    students = json.loads(jsonString)
    return students


def __showStudent(student):
    print(f'\nmatricula: {student["registration"]}')
    print(f'nome: {student["name"]}')
    print(f'email: {student["email"]}')
    print(f'curso: {student["course"]}\n')


def __registrationValidator(name: str):
    requiredValidator = validators.required('Matricula obrigatoria.')
    error = requiredValidator(name)
    if (error != None):
        return error

    match = re.match(r'\D', name)
    if (match != None):
        return 'Matricula não pode conter letras.'


def __nameValidator(name: str):
    requiredValidator = validators.required('Nome obrigatorio.')
    error = requiredValidator(name)
    if (error != None):
        return error

    match = re.match(r'\d', name)
    if (match != None):
        return 'Nome não pode conter numeros.'
