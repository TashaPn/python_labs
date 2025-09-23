# Лабораторная работа 1
## №1
```python
print("НОМЕР 1: ПРИВЕТ И ВОЗРАСТ")
name = input()
age = int(input())
print("Имя:", name)
print("Возраст:", age)
print("Привет,", name,"! Через год тебе будет", age+1,".")

```
![](images/Lab_01/задание%201.png "первый номер")

## №2
```python
print("НОМЕР 2: СУММА И СРЕДНЕЕ")
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
print("sum =",f"{summ:.2f}",";avg =",f"{avg:.2f}")

```

![](images/Lab_01/задание%202.png "первый номер")

## №3
```python
print("НОМЕР 3: ЧЕК: СКИДКА И НДС")
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print("База после скидки:", f"{base:.2f}","₽")
print("НДС:",f"{vat_amount:.2f}","₽")
print("Итого к оплате:",f"{total:.2f}","₽")

```

![](images/Lab_01/задание%203.png "первый номер")

## №4
```python
print("НОМЕР 4: МИНУТЫ - ЧЧ:ММ")
min = int(input())
hours = min//60
minutes = min%60
print("Минуты:",min)
print(hours,":",minutes,sep="")

```

![](images/Lab_01/задание%204.png "первый номер")

## №5
```python
print("НОМЕР 5: ИНИЦИАЛЫ И ДЛИНА СТРОКИ")
full_name = input()
words = full_name.strip().split()
cleanwords = " ".join(words)
initials = ''.join(word[0].upper() for word in words) + '.'
print("ФИО:", full_name)
print("Инициалы:",initials)
print("Длина (символов):", len(cleanwords))

```

![](images/Lab_01/задание%205.png "первый номер")

## №6
```python
print("НОМЕР 6: СО ЗВЁЗДОЧКОЙ")
n = int(input())
ochn = 0
zaochn = 0
for i in range(n):
    info = input()
    if info.count("True")==1:
        ochn+=1
    if info.count("False")==1:
        zaochn+=1
print("out:",ochn,zaochn)

```

![](images/Lab_01/задание%206.png "первый номер")

## №7
```python
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

```

![](images/Lab_01/задание%207.png "первый номер")
