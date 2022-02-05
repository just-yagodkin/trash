
avarage1 = 0
avarage = [0, 0, 0]

text = open('data.txt', 'r')
lines = text.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split(';')

with open('answer.txt', 'w') as answer:
    answer.write('')

for string in lines:
    for i in range(1,len(string)):
        avarage1 += int(string[i])
        avarage[i-1] += int(string[i])
    avarage1 /= 3
    #print(avarage1)
    with open('answer.txt', 'a') as answer:
        answer.write(str(avarage1))
        answer.write('\n')
    avarage1 = 0

with open('answer.txt', 'a') as answer:
    answer.write(str(avarage[0]/len(lines)))
    answer.write(' ')
    answer.write(str(avarage[1] / len(lines)))
    answer.write(' ')
    answer.write(str(avarage[2] / len(lines)))
    answer.write(' ')
#print(avarage[0]/len(lines), avarage[1]/len(lines), avarage[2]/len(lines), sep=' ', end='')
