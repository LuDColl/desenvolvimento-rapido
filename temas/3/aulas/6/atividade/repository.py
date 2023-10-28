import json
from typing import Any
import helper
import validators
import re
import dbcontext


def init() -> None:
    dbcontext.connect()
    sql = '''
        CREATE TABLE IF NOT EXISTS students(
            registration INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
        )
        
        CREATE TABLE IF NOT EXISTS notes(
            item INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
            value REAL NOT NULL,
            registration INTEGER NOT NULL,
            FOREIGN KEY(registration) REFERENCES students(registration)
        )
    '''
    dbcontext.commit(sql)


def showStudents() -> None:
    students = _getStudents()
    if (len(students) == 0):
        return print('Nenhum aluno cadastrado.')

    for student in students:
        _showStudent(student)


def registerStudent() -> None:
    name = helper.inputWithValidation(
        'Digite o nome do aluno: ', _nameValidator)
    email = helper.inputWithValidation(
        'Digite o email do aluno: ', validators.required('Email obrigatorio.'))
    course = helper.inputWithValidation(
        'Digite o curso do aluno: ', validators.required('Curso obrigatorio.'))

    sql = f'''
        INSERT INTO students(name, email, course)
        VALUES ('{name}', '{email}', '{course}')
    '''
    dbcontext.commit(sql)

    sql = f'SELECT * FROM students WHERE registration = {registration}'
    student = dbcontext.find(sql)
    _showStudent(student)


def searchStudent() -> None:
    name = helper.inputWithValidation(
        'Digite o nome do estudante: ', _nameValidator)
    sql = f"SELECT * FROM students WHERE name LIKE '%{name}%'"
    student = dbcontext.find(sql)
    if (student == None):
        return print('Estudante em falta')

    _showStudent(student)


def registerNote() -> None:
    registration = helper.inputWithValidation(
        'Digite a matricula do aluno: ', _registrationValidator)

    sql = 'SELECT * FROM students WHERE register = ${registration}'
    student = dbcontext.find(sql)
    if student == None:
        return print('Estudante não encontrado')
    
    sql = 'INSERT INTO'
    dbcontext.commit()


def _getStudents() -> list[Any]:
    students = dbcontext.select('SELECT * FROM students')
    return students


def _showStudent(student) -> None:
    print(f'\nmatricula: {student[0]}')
    print(f'nome: {student[1]}')
    print(f'email: {student[2]}')
    print(f'curso: {student[3]}\n')


def _registrationValidator(name: str) -> str:
    requiredValidator = validators.required('Matricula obrigatoria.')
    error = requiredValidator(name)
    if (error != None):
        return error

    match = re.match(r'\D', name)
    if (match != None):
        return 'Matricula não pode conter letras.'


def _nameValidator(name: str) -> str:
    requiredValidator = validators.required('Nome obrigatorio.')
    error = requiredValidator(name)
    if (error != None):
        return error

    match = re.match(r'\d', name)
    if (match != None):
        return 'Nome não pode conter numeros.'
