from random import randint as rand

cases = int(input("Gerar quantos casos? -> "))

for number in range(22, cases+22):
    file = open('../input/' + str(number), 'w')
    S = rand(1,200)
    file.write(str(S) + '\n')
    for i in range(S):
        file.write(str(rand(2, 1e12)) + '\n')
    file.close()
