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

