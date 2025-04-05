class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__heap_array = args[0]
        else:
            self.__heap_array = []

    def insert(self, value):
        """
        원소 삽입하기 - 스며올리기 사용

        :param value:
        :return:
        """
        self.__heap_array.append(value) # 배열의 뒤에 요소를 추가
        self.__percolate_up(len(self.__heap_array) - 1) # 배열의 맨 뒤 요소부터 스며올리기

    def delete_max(self):
        """
        원소 삭제하기 - 스며 내리기

        :return:
        """
        if not self.is_empty():
            max = self.max() # 최대 값
            self.__heap_array[0] = self.__heap_array.pop() # 배열의 마지막 요소를 pop 하여 할당
            self.__percolate_down(0) # 스며내리기
            return max
        else:
            return None

    def max(self):
        return self.__heap_array[0]

    def build_heap(self) -> None:
        for i in range(len(self.__heap_array) - 2 // 2, -1, -1): # 역순으로 갈 때 최초의 부모노드는 (n-2)//2 노드이다.
            self.__percolate_down(i)

    def size(self) -> int:
        return len(self.__heap_array)

    def is_empty(self) -> bool:
        return len(self.__heap_array) == 0

    def clear(self) -> None:
        self.__heap_array = []

    def print_heap(self):
        pass

    def __percolate_up(self, index:int):
        """
        스며올리기

        :param index:
        :return:
        """
        parent_index = (index - 1) // 2

        # 스며올리기를 할 index 가 0 보다 크다. => 0은 루트 노드의 인덱스 (경계 조건, 종료 조건)
        # 자식 노드(index)와 부모 노드를 비교하여 자식 노드가 크다면 교환한다.(올리기)
        if index > 0 and self.__heap_array[index] > self.__heap_array[parent_index]:
            self.__heap_array[index], self.__heap_array[parent_index] = self.__heap_array[parent_index], self.__heap_array[index]
            # 부모 노드의 인덱스로 스며올리기 실행
            self.__percolate_up(parent_index)

    def __percolate_down(self, index:int):
        """
        스며내리기

        :param index:
        :return:
        """
        left_child = 2 * index + 1 # 왼쪽 자식
        right_child = 2 * index + 2 # 오른쪽 자식

        if left_child <= len(self.__heap_array) - 1: # 왼쪽 자식 존재 여부 확인 => 없다면 리프 노드 (종료 조건)
            # 자식 노드간 값 비교 -> 더 작은 값을 가진 자식 노드와 부모 노드를 비교 하기 위해서
            if right_child <= len(self.__heap_array) - 1 and self.__heap_array[left_child] > self.__heap_array[right_child]:
                left_child = right_child # right_child 가 작은 값을 가질 떄 교환
            # 부모 노드와의 교환
            if self.__heap_array[index] < self.__heap_array[left_child]:
                self.__heap_array[index], self.__heap_array[left_child] = self.__heap_array[left_child], self.__heap_array[index]
                self.__percolate_down(left_child) # 스며 내리기
