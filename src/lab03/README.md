# Лабораторная работа 3
## Задание A
### Normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Преобразование строки s в norm(s):
    """
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё","е").replace("Ё","Е")
    text = text.replace("\r"," ").replace("\t"," ")
    text = text.strip()
    text = text.split()
    text = " ".join(text)
    return text
```

![](/images/Lab_03/normalize_1.png "функция normalize")
![](/images/Lab_03/normalize_2.png "функция normalize")

### Tokenize
```python
def tokenize(text: str) -> list[str]:
    """
    Множество слов — это все подстроки, удовлетворяющие шаблону \w+(?:-\w+)*
    """
    return re.findall("[\w-]+", text)
```

![](/images/Lab_03/tokenize_1.png "функция tokenize")
![](/images/Lab_03/tokenize_2.png "функция tokenize")

### Count_Freq
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Для списка токенов T = [t₁, …, tₙ] частота слова w равна f(w) = |{ i : tᵢ = w }|
    """
    result = {}

    for token in tokens:
        if token in result:
            result[token]+=1
        else:
            result[token]=1

    return result
```

![](/images/Lab_03/count_freq_1.png "функция count_freq")
![](/images/Lab_03/count_freq_2.png "функция count_freq")

### Top_N
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Отсортировать пары (слово, частота) по ключу (-частота, слово) и взять первые N
    """
    result = []
    for key in freq:
        value = freq[key]
        element = (key, value)
        result.append(element)
    result = sorted(result, reverse=True, key=lambda n: n[1])[:n]

    return result
```

![](/images/Lab_03/top_n_1.png "функция top_n")
![](/images/Lab_03/top_n_2.png "функция top_n")

## Задание B
```python
import sys 

from lib.text import *


a = sys.stdin.read()

norm = normalize(a)
token = tokenize(norm)
print("Всего слов:", len(token))

count = count_freq(token)
print("Уникальных слов:", len(count))

top = top_n(count)
print("Топ-5:")


for element in top:
    print(element[0], ":", element[1])

```

![](/images/Lab_03/number_B.png "задание_B")
![](/images/Lab_03/number_B2.png "задание_B")