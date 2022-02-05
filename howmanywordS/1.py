d = {}
ind = 0
count = 0
memory = ''

text = open('data.txt', 'r')
lines = text.readlines()
for i in range(len(lines)):             # for line in lines:
    lines[i] = lines[i].lower().split()         # line = line.lower()              ПОЧЕМУ НЕ РАБОТАЕТ!?!?!??

for string in lines:
    for word in string:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

for c in d:
    if d[c] > count:
        count = d[c]

for c in d:
    if d[c] == count and c > memory:        # Не лучшая реализация, можно оптимизировать, но минэ до пiздi
        memory = c


answer = open('answer.txt', 'w')
answer.write(memory)
answer.write(' ')
answer.write(str(count))