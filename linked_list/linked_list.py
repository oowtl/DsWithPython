from .node import Node

class LinkedList:
    """
    LinkedList

    구성요소 : 1. head - 노드 객체

    ADT 리스트

    1. 삽입 : insert, append
    2. 삭제 : pop, remove
    3. 접근
    4. 검색 : index
    """
    def __init__(self) :
        # head node = dummy
        self.__head = Node('dummy_head', None)
        # list size
        self.__size = 0

    def insert(self, index: int, new_item):
        """
        insert
        방법 1. 하나로 삽입하기 => 더미 노드를 헤드로 둔다.
        방법 2. 두개의 경우로 나눠서 삽입하기 => 헤드 노드에 삽입하는 상황과 아닌 상황을 나누기

        1. 가능한 인덱스 인지 확인한다.
        2. 인자로 받은 인덱스의 이전 노드를 찾는다. => prev (노드 구성요소 : next, item)
        3. prev.next 를 다음 노드로 가리키는 노드를 생성한다.=> new_node
        4. prev.next 를 new_node 로 변경한다.
        """
        if 0 <= index <= self.__size: # 1. 가능한 인덱스 인지 확인한다. => index 의 범위를 지정
            # 2. 인자로 받은 인덱스의 이전 노드를 찾는다. => prev (노드 구성요소 : next, item)
            prev = self.__get_node(index - 1)
            # 3. prev.next 를 다음 노드로 가리키는 노드를 생성한다.=> new_node
            new_node = Node(new_item, prev.next)
            # 4. prev.next 를 new_node 로 변경한다.
            prev.next = new_node
            # 5. 리스트의 크기를 1 늘린다.
            self.__size += 1
        else:
            print("index out of range")

    def append(self, new_item):
        """
        append : 맨 끝의 요소 삽입

        1. 연결리스트의 맨 뒤의 요소 할당 => prev
        2. 새로운 노드 생성 => new_node
        3. prev.next 에 new_node 할당
        4. 리스트 사이즈 증가
        """
        # 1. 연결리스트의 맨 뒤의 요소 할당 => prev
        prev = self.__get_node(self.__size - 1)
        # 2. 새로운 노드 생성 => new_node
        new_node = Node(new_item, None)
        # 3. prev.next 에 new_node 할당
        prev.next = new_node
        # 4. 리스트 사이즈 증가
        self.__size += 1

    def pop(self, index:int):
        """
        pop : 인자로 받은 인덱스의 요소 삭제하기

        1. 받은 인덱스의 이전 요소 할당 => prev, pop_item
        2. prev.next 를 prev.next.next 로 변경
        3. 리스트의 크기 -1
        4. prev.next 반환
        """
        # 1. 받은 인덱스의 이전 요소 및 반환할 요소 할당  => prev, pop_item
        prev = self.__get_node(index - 1)
        pop_item = prev.next
        # 2. prev.next 를 prev.next.next 로 변경
        prev.next = prev.next.next
        # 3. 리스트의 크기 -1
        self.__size -= 1
        # 4. pop_item 반환
        return pop_item

    def remove(self, item):
        """
        remove : 인자로 넣은 요소와 일치하는 요소를 삭제

        1. item 과 일치하는 노드를 찾는다. => __find_node
        2. curr 이 None 인지 아닌지로 찾는다. => 예외 처리를 여기에서 한다?!
        3. curr != None, 삭제
        4. curr == None, None 반환
        5. 리스트의 크기 -1
        """
        # 1. item 에 해당하는 노드 찾기
        prev, curr = self.__find_node(item)

        # 2. curr 이 None 인지 아닌지로 찾는다. => 예외 처리를 여기에서 한다?!
        if curr != None:
            prev.next = curr.next
            # 5. 리스트의 크기 -1
            self.__size -= 1
            return curr
        # 4. curr == None, None 반환
        return None

    def index(self, item) -> int:
        """
        :param item:
        :return: item 이 해당하는 index

        1. loop 를 돌면서 item 과 비교
        2. 일치 시 현재 인덱스 반환
        3. 미 일치 시 curr 의 다음노드로 이동
        4. loop 종료 후 안쓰는 인덱스 반환
        """
        curr = self.__head
        # 1. loop 를 돌면서 item 과 비교
        for i in range(self.__size):
            # 2. 일치 시 현재 인덱스 반환
            if curr.item == item:
                return i
            # 3. 미 일치 시 curr 의 다음노드로 이동
            curr = curr.next
        # 4. loop 종료 후 안쓰는 인덱스 반환
        return -2

    def __get_node(self, index) -> Node:
        """
        __get_node : 해당 인덱스에 맞는 노드 찾기
        1. 헤드 노드 할당 => curr
        2. 이동 해야 하는 index 만큼 for loop
        3. loop 횟수 만큼 이동
        4. curr 반환
        """
        # 1. 헤드 노드 할당 => curr
        curr = self.__head
        # 2. 이동 해야 하는 index 만큼 for loop
        for i in range(index + 1):
            # 3. loop 횟수 만큼 이동
            curr = curr.next
        # 4. curr 반환
        return curr

    def __find_node(self, item) -> (Node, Node):
        """
        item 과 일치하는 노드를 반환하는 메서드

        :param item:
        :return: (prev, curr)

        1. 연결 리스트의 마지막 까지 순회한다.
        2. item 과 일치하는지 비교
        3. 일치하면 반환
        4. 일치하지 않으면 prev, curr에 다음 노드를 할당한다.
        5. 반환된 것이 없다면 None 을 반환한다.
        """

        curr = self.__head
        prev = None

        # 1. 연결 리스트의 마지막 까지 순회한다.
        while curr != None:
            # 2. item 과 일치하는지 비교
            if curr.item == item:
                # 3. 일치하면 반환
                return prev, curr
            # 4. 일치하지 않으면 prev, curr에 다음 노드를 할당한다.
            else :
                prev = curr
                curr = curr.next

        # 5. 반환된 것이 없다면 None 을 반환한다.
        return None, None


