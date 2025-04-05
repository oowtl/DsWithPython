from heap.heap import Heap

h1 = Heap()
h1.build_heap()
h1.clear()
h1.insert(7)
h1.insert(5)
h1.insert(9)
h1.insert(4)
h1.insert(11)
h1.insert(19)
h1.insert(20)
h1.insert(21)
h1.insert(11)
h1.insert(9)

print(h1.delete_max())