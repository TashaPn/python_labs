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
        del(self._data[-1])
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
        del(self._data[-1])
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