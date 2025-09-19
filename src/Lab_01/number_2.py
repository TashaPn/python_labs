print("НОМЕР 2.СУММА И СРЕДНЕЕ")
a = input()
b = input()
if a.count(",")==1:
    a = a.replace(",",".")
if b.count(",")==1:
    b = b.replace(",",".")
a1 = float(a)
b1 = float(b)
summ = a1+b1
avg = summ/2
print("sum =",summ,";avg =",avg)

