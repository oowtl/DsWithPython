from .node import Node

class CircularLinkedList:
    """
    원형 연결 리스트

    구조

    1. tail
    """
    def __init__(self):
        self.__tail = Node('dummy', None)
        self.__tail.next = self.__tail # tail 의 다음 노드가 dummy head => 여기에서 할당된 dummy head 가 계속 사용된다.
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
        new_node = Node(new_item, self.__tail.next) # __init__ 메서드에서 초기화된 dummy head 가 쓰인다.
        self.__tail.next = new_node
        self.__tail = new_node
        self.__size += 1

    def pop(self, *args) -> Node:
        # 가변 파라미터 : 인자가 없거나 -1이면 마지막 원소로 처리하기 위함.
        if self.is_empty(): # 비어 있는 경우
            return None

        if len(args) != 0:
            index = args[0] # pop() 해야할 인덱스 i 결정

        if len(args) == 0 or index == -1:
            index = self.__size - 1 # pop() 에 인자가 없거나 -1 이 들어 있다면 맨 끝 인덱스 할당

        # index 에 해당하는 요소 삭제
        if 0 <= index <= self.__size - 1:
            # 이전 노드 찾기
            prev = self.get_node(index -1)
            # 삭제 요소
            ret_item = prev.next.item
            # 삭제
            prev.next = prev.next.next
            # 마지막 노드일 때 tail 노드 설정해주기
            if index == self.__size - 1:
                self.__tail = prev
            # 리스트 사이즈 줄이기
            self.__size -= 1
            # 삭제된 요소 반환
            return ret_item
        else:
            return None

    def remove(self, x) -> Node:
        (prev, curr) = self.__find_node(x)
        if curr != None: # curr 이 존재
            prev.next = curr.next # 연결을 끊음 (curr 과 prev 가 같이 있어서 가능)
            if curr == self.__tail: # tail 노드일 떄 분기
                self.__tail = prev
                return x
        else:
            return None

    def get(self, *args) -> Node:
        if self.is_empty():
            return None

        if len(args) != 0:
            index = args[0]

        if len(args) == 0 or index == -1:
            index = self.__size - 1

        if 0 <= index <= self.__size - 1:
            return self.get_node(index).item

        pass

    def index(self, item) -> int:
        cnt = 0
        for element in self:
            if element == item:
                return cnt
            cnt += 1
        return -12345

    def is_empty(self) -> bool:
        return self.__size == 0

    def size(self) -> int:
        return self.__size

    def clear(self):
        self.__tail = Node('dummy', None)
        self.__tail.next = self.__tail
        self.__size = 0

    def count(self, item) -> int:
        cnt = 0
        for element in self:
            if element == item:
                cnt += 1
        return cnt

    def extend(self, after):
        for x in after:
            self.append(x)

    def copy(self)-> b'CircularLinkedList':
        after = CircularLinkedList()
        for element in self:
            after.append(element)
        return after

    def reverse(self) -> None:
        __head = self.__tail.next # 더미 헤드
        prev = __head; curr = prev.next; next = curr.next
        curr.next = __head; __head.next = self.__tail; self.__tail = curr
        for i in range(self.__size - 1):
            prev = curr; curr = next; next = next.next
            curr.next = prev

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a. sort()
        self.clear()
        for element in a:
            self.append(element)

    def __find_node(self, x) -> (Node, Node):
        __head = prev = self.__tail.next # 더미 헤드
        curr = prev.next # 0번 노드
        while curr != __head:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr; curr = curr.next
        return (None, None)

    def __iter__(self):
        return CircularLinkedListIterator(self)

class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1) # 더미 헤드
        self.iter_position = self.__head.next # 0번 노드

    def __next__(self):
        if self.iter_position == self.__head: # 순환 끝
            raise StopIteration
        else: # 현재 원소를 반환 하면서 다음 원소로 이동
            item = self.iter_position.item
            self.iter_position = self.iter_position.next
            return item
