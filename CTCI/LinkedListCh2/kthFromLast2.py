import unittest 
from LinkedList import LinkedList, Node

def kthFromlast(linkedList, k):
    sizeList = linkedList.size()
    count = 0
    stop = sizeList - k
    start = linkedList.head
    while count != stop: 
        start = start.next_node
        count += 1
    return start.data

class TestKthFromlast(unittest.TestCase): 
    test_cases = [(LinkedList(Node(1, Node(2, Node(3, Node(4))))), 2, 3)]
    def test_kth_from_last(self): 
        for linkList, k, exptected in self.test_cases: 
            result = kthFromlast(linkList, k)
            self.assertEqual(result, exptected, f"Error at {linkList} got {result} instead of {exptected}")
kthFromlast(LinkedList(Node(1, Node(2, Node(3, Node(4))))), 2)
unittest.main()