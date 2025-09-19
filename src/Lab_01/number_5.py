print("НОМЕР 5: ИНИЦИАЛЫ И ДЛИНА СТРОКИ")
full_name = input()
while full_name.count(" ")!=3:
    full_name = full_name.replace("  "," ")
print(full_name)


