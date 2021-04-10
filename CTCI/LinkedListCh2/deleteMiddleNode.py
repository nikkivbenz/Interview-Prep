from LinkedList import LinkedList, Node
import unittest

def deleteMiddle(linkedList): 
    middle = current = linkedList.head
    count = 1
    while current != None: 
        count += 1
        if count % 2 == 1: 
            middle = middle.next_node
        current = current.next_node

    return middle.data

x  = deleteMiddle(LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))))
y = deleteMiddle(LinkedList(Node(1, Node(2, Node(3)))))

class TestDeleteMiddle(unittest.TestCase): 
    test_cases = [((LinkedList(1).createLinkedList[2,3,4,5,6, 7]), 4)
                (LinkedList(1).createLinkedList[2,3], 2)]

    def test_delete_middle(self): 
        for testList, expected in self.test_cases: 
            result = deleteMiddle(testList)
            self.assertEqual(result, expected, f"ERROR for {testList} got {result} when expected: {expected}")

unittest.main()