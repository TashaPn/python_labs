print("НОМЕР 7: ЗАДАНИЕ СО ЗВЁЗДОЧКОЙ")
start = input()
end = ""

first_index = None
for i in range(len(start)):
    if start[i].isupper():
        first_index = i
        break

first_2_index = None
for i in range(first_index + 1, len(start)):
    if start[i].isdigit():
        first_2_index = i
        break

step = (first_2_index + 1) - first_index


for i in range(first_index, len(start), step):
    end += start[i]
    if start[i] == '.':  
        break

print("in:",start)
print("out:",end)
