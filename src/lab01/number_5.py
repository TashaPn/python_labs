print("НОМЕР 5: ИНИЦИАЛЫ И ДЛИНА СТРОКИ")
full_name = input()
words = full_name.strip().split()
cleanwords = " ".join(words)
initials = ''.join(word[0].upper() for word in words) + '.'
print("ФИО:", full_name)
print("Инициалы:",initials)
print("Длина (символов):", len(cleanwords))
