from lib.text import *

a = input()

norm = normalize(a)
token = tokenize(norm)
print("Всего слов:",len(token))
count = count_freq(token)
print("Уникальных слов:",len(count))
top = top_n(count)
print("Топ-5:")

for element in top:
    print(element[0],":",element[1])
