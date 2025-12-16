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
