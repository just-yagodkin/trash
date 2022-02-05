import requests

URLmain = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset.txt', 'r') as URL:
    URL = URL.readline().strip()

word1 = URL.split()[0]
newURL = URL

while word1 != 'We':
    newURL = URLmain + requests.get(newURL).text
    word1 = requests.get(newURL).text.split()[0]
    #print(newURL)

#print(word1)                                   # первое слово в файле
#print(requests.get(newURL).text)               # содержимое файла

with open('answer.txt', 'w') as ans:
    ans.write(requests.get(newURL).text)