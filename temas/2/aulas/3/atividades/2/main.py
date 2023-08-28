import json

file = open('students.json', 'w')
file.write('[]')
file.close()


def getStudents():
    file = open('students.json', 'r')
    jsonString = file.read()
    students = json.loads(jsonString)
    file.close()
    return students


def showStudent(student):
    print(student['name'])
    print('email: ' + student['email'])
    print('curso: ' + student['course'])


def showStudents():
    students = getStudents()
    for student in students:
        showStudent(student)

    input()


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
    input()


run = True


def close():
    global run
    run = False


choices = [close, registerStudent, showStudents, searchStudent]
while run:
    choice = input(
        """
1 - Cadastrar novo aluno;
2 - Listar alunos cadastrados;
3 - Buscar um aluno pelo nome;

0 - Sair

"""
    )
    selectedChoice = choices[int(choice)]
    selectedChoice()
