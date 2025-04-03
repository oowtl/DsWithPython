from .node import Node

class CircularLinkedList:
    """
    원형 연결 리스트

    구조

    1. tail
    """
    def __init__(self):
        self.__tail = Node('dummy', None)
        self.__tail.next = self.__tail # tail 의 다음 노드가 dummy head
        self.__size = 0 # 리스트 사이즈 할당

    def insert(self, index:int, item) -> None:
        """
        요소 삽입
        :param index: 삽입할 위치
        :param item: 삽입 요소
        :return: None
        """

        # 삽입할 위치가 0과 같거나 커야한다.
        # 삽입할 위치가 리스트의 크기와 같거나 작아야 한다. => 리스트 맨 뒤에 삽입할 때 필요하다.
        if 0 <= index <= self.__size:
            # prev 요소 찾기
            prev = self.get_node(index - 1)
            # 새로운 노드 생성, prev.next 와 연결
            new_node = Node(item, prev.next)
            # prev.next 연결
            prev.next = new_node

            # 첫 요소 삽입 시
            if index == self.__size:
                self.__tail = new_node

            # 리스트 사이즈 증가
            self.__size += 1
        else:
            raise IndexError("Index out of range")



    def get_node(self, index:int) -> Node:
        """
        접근 해야 하는 위치의 요소 반환
        :param index: 접근할 위치
        :return: Node
        """
        """
        1. index 번 순회한다.
        2. 순회하면서 next 를 한다.
        3. 순회 결과를 반환한다.
        
        만약에 순회하면서 None 이 나온다면? None 반환 => 별다른 처리할 필요 없음
        """

        # self.tail 은 더미 헤드
        curr = self.__tail.next

        for i in range(index+1):
            curr = curr.next

        return curr

    def append(self, new_item) -> None:
        pass

    def pop(self, index:int) -> Node:
        pass

    def remove(self, index:int) -> Node:
        pass

    def get(self, *args) -> Node:
        pass

    def index(self, item) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def size(self) -> int:
        pass

    def clear(self):
        pass

    def count(self, item) -> int:
        pass

    def extend(self, after):
        pass

    def copy(self)-> b'CircularLinkedList':
        pass

    def reverse(self) -> None:
        pass

    def sort(self) -> None:
        pass