import json
import helper
import validators
import re
import dbcontext


def init():
    dbcontext.connect()
    sql = '''
        CREATE TABLE IF NOT EXISTS students(
            registration INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            course TEXT
        )
    '''
    dbcontext.commit(sql)


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

    sql = f'''
        INSERT INTO students(registration, name, email, course)
        VALUES ({registration}, '{name}', '{email}', '{course}')
    '''
    dbcontext.commit(sql)

    sql = f'SELECT * FROM students WHERE registration = {registration}'
    student = dbcontext.find(sql)
    __showStudent(student)


def searchStudent():
    name = helper.inputWithValidation(
        'Digite o nome do estudante: ', __nameValidator)
    sql = f"SELECT * FROM students WHERE name LIKE '%{name}%'"
    student = dbcontext.find(sql)
    if (student == None):
        return print('Estudante em falta')

    __showStudent(student)


def __getStudents():
    students = dbcontext.select('SELECT * FROM students')
    return students


def __showStudent(student):
    print(f'\nmatricula: {student[0]}')
    print(f'nome: {student[1]}')
    print(f'email: {student[2]}')
    print(f'curso: {student[3]}\n')


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
