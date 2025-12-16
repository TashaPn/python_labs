# Лабораторная работа 10
## Структуры данных: Stack, Queue, Linked List и бенчмарки
### Задание A : Реализовать Stack и Queue 
```python
class Stack:
    def __init__(self):
        """
        внутреннее хранилище стека
        """
        self._data = []

    def push(self, item):
        """
        добавление элемента в конец стека
        """
        self._data.append(item)

    def pop(self):
        """
        удаление последнего элемента и его вывод
        """
        if len(self._data) == 0:
            raise IndexError("стек пустой")
        result = self._data[-1]
        del self._data[-1]
        return result

    def peek(self):
        """
        вывод последнего элемента стека
        """
        if len(self._data) == 0:
            raise IndexError("стек пустой")  # либо return None
        result = self._data[-1]
        return result

    def is_empty(self) -> bool:
        """
        проверка на пустоту стека
        """
        if len(self._data) == 0:
            return True
        return False

    def __len__(self) -> int:
        """
        возвращает количество элементов в стеке
        работает, когда делают len(st)
        """
        return len(self._data)


class Queue:
    def __init__(self):
        """
        внутреннее хранилище очереди
        """
        self._data = []

    def enqueue(self, item):
        """
        вставка элемента в конец очереди
        """
        self._data.insert(0, item)

    def dequeue(self):
        """
        получения первого элемента очереди и его удаление
        """
        if len(self._data) == 0:
            raise IndexError("очередь пустая")
        result = self._data[-1]
        del self._data[-1]
        return result

    def peek(self):
        """
        получение первого элемента очереди
        """
        if len(self._data) == 0:
            raise IndexError("очередь пустая")  # либо return None
        result = self._data[-1]
        return result

    def is_empty(self) -> bool:
        """
        проверка на пустоту очереди
        """
        if len(self._data) == 0:
            return True
        return False

    def __len__(self) -> int:
        """
        возвращает количество элементов в очереди
        работает, когда делают len(qe)
        """
        return len(self._data)
```

![](/images/Lab_10/structures.PNG)
![](/images/Lab_10/structures2.PNG)
![](/images/Lab_10/structures3.PNG)
![](/images/Lab_10/structures4.PNG)


### Задание B : Реализовать SinglyLinkedList
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)

        # Если список пустой, создаем новую ноду в self.head
        if self.head == None:
            self.head = new_node
            self._size += 1
        else:

            # Если не пустой, берем первую ноду из self.head
            current_node = self.head

            # Начинаем идти по всем .next, пока там не будет None
            # Это значит, что мы нашли последнюю ноду в списке, за ней ничего нет
            while current_node.next != None:
                current_node = current_node.next

            # В последнюю ноду в .next сохраняем новую ноду
            current_node.next = new_node
            self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу — неполная реализация, есть ошибки"""
        if idx < 0:
            raise IndexError("negative index is not supported")

        if idx == 0:
            self.prepend(value)
            return

        if idx > self._size:
            raise IndexError("too big index is not supported")

        new_node = Node(value)

        current_node = self.head
        for step in range(idx - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

        self._size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

    def remove(self, value) -> None:
        """
        удалить первое вхождение значения value
        """
        current_node = self.head
        previuos_node = None
        found = False

        while current_node is not None:
            if current_node.value == value:
                found = True
                break

            previuos_node = current_node
            current_node = current_node.next

        if found:
            next_node = current_node.next
            previuos_node.next = next_node
            self._size -= 1
```

![](/images/Lab_10/linked_list.PNG)
![](/images/Lab_10/linked_list2.PNG)
![](/images/Lab_10/linked_list3.PNG)


### Результаты тестов и работы программы
```python
import pytest

from src.lab10.structures import Stack


def test_one_push_and_peek():
    st = Stack()
    st.push("YES")
    result = st.peek()
    assert result == "YES"


def test_three_push_and_peek():
    st = Stack()
    st.push("YES")
    st.push("NO")
    st.push("MAYBE")

    result = st.peek()
    assert result == "MAYBE"


def test_two_pop():
    st = Stack()
    st.push("YES")
    st.push("NO")
    st.push("MAYBE")

    st.pop()
    result = st.pop()
    assert result == "NO"


def test_len():
    st = Stack()
    st.push("YES")
    st.push("NO")
    st.push("MAYBE")

    assert len(st) == 3


def test_is_empty():
    st = Stack()
    result = st.is_empty()
    assert result == True


def test_full_is_empty():
    st = Stack()
    st.push(2025)
    result = st.is_empty()
    assert result == False


def test_peek_error():
    st = Stack()
    with pytest.raises(IndexError):
        st.peek()


def test_pop_error():
    st = Stack()
    with pytest.raises(IndexError):
        st.pop()
```

```python
import pytest

from src.lab10.linked_list import SinglyLinkedList


@pytest.fixture
def si():
    si = SinglyLinkedList()
    si.append(333)
    si.append("Yes")
    return si


def test_append_node():
    si = SinglyLinkedList()
    si.append(333)
    assert si._size == 1
    node = si.head
    assert node.value == 333


def test_four_append_node(si):
    si.append("No")
    si.append("Maybe")
    assert si._size == 4
    assert si.head.value == 333
    assert si.head.next.value == "Yes"
    assert si.head.next.next.value == "No"
    assert si.head.next.next.next.value == "Maybe"


def test_pretend_node(si):
    si.prepend("No")
    assert si.head.value == "No"
    assert si.head.next.value == 333
    assert si.head.next.next.value == "Yes"
    assert len(si) == 3


def test_insert_node(si):
    si.append("No")
    si.insert(1, "Maybe")
    assert si.head.value == 333
    assert si.head.next.value == "Maybe"
    assert si.head.next.next.value == "Yes"
    assert si.head.next.next.next.value == "No"
    assert len(si) == 4


def test_iter(si):
    si.append("No")

    nodes = list(si)
    assert nodes == [333, "Yes", "No"]


def test_remove_node(si):
    si.append("No")

    si.remove("Yes")
    assert si.head.value == 333
    assert si.head.next.value == "No"
    assert len(si) == 2


def test_remove_invalid_node(si):
    si.append("No")

    si.remove("Maybe")
    assert si.head.value == 333
    assert si.head.next.value == "Yes"
    assert si.head.next.next.value == "No"
    assert len(si) == 3
```
![](/images/Lab_10/test1.PNG)      ![](/images/Lab_10/test2.PNG)


![](/images/Lab_10/Снимок.PNG)



![](../../images/cat.gif)         
## Спасибо за внимание и просмотр всех моих лаб :3