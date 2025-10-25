print("НОМЕР 4: МИНУТЫ - ЧЧ:ММ")
min = int(input())
hours = min//60
minutes = min%60
print(f"{hours:02d}:{minutes:02d}")
