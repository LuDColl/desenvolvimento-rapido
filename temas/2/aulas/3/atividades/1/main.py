number = 1
file = open('crescente.txt', 'a')
while number <= 100:
    file.write(str(number) + ';')
    number += 1
file.close()
