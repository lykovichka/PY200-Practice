from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        self.next = None  # TODO установить значение следующего узла с помощью метода set_next
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
       # TODO метод проверки корректности связываемого узла
        if not isinstance(node, (Node,type(None))):
            raise TypeError ('valid')

    def set_next(self, next_: Optional["Node"] = None) -> None:
        # TODO метод должен проверять корректность узла и устанавливать значение атрибуту next
        if not isinstance(next_, (Node, type(None))):
            raise TypeError ('next')
        self.is_valid(next_)
        self.next = next_


if __name__ == '__main__':
    # TODO инициализируйте два узла с любыми значеними
    node_1 = Node(1)
    node_2 = Node(2)

    # TODO свяжите первый узел со вторым
    node_1.set_next(node_2)
    print(node_1)
    print(node_2)
