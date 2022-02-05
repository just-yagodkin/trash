import requests
with open('dataset.txt', 'r') as res:
    url = res.readline().strip()
    #print(url)

res = requests.get(url)
#print(res)                                                     if 200 - good!
lines = res.text.splitlines()

#print(lines)
#print(len(lines))

with open('answer.txt', 'w') as answer:
    answer.write(str(len(lines)))
