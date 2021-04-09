import unittest
from LinkedList import LinkedList, Node


def deleteDuplicates(linkedList): 
    head = linkedList.head
    allData = [head.data] 
    newLinkedList = LinkedList(Node(head.data))

    while head != None: 
        if head.data not in allData: 
            newLinkedList.addNode(Node(head.data))
            allData.append(int(head.data))


        head = head.next_node
    return newLinkedList

def deleteDuplicatesAlternative(linkedList):
    prev = None
    head = linkedList.head
    allData = [] 

    while head != None: 
        if head.data in allData: 
            prev.next_node = head.next_node
            head = prev.next_node

        else: 
            allData.append(head.data)
            prev = head
            head = head.next_node
            
    return linkedList



class TestDeleteDuplicates(unittest.TestCase): 
    test_cases = [
        (LinkedList(Node(1, Node(2, Node(3, Node(4, Node(1, Node(2))))))),
        LinkedList(Node(1, Node(2, Node(3, Node(4))))))
        ]


    def test_delete_duplicates(self): 
        for linkedList, expected in self.test_cases: 
            result = deleteDuplicates(linkedList)
            result2 = deleteDuplicatesAlternative(linkedList)
            self.assertEqual(result.toString(), expected.toString(), f"error caused at {linkedList.toString()} got {result.toString()} instead of {expected.toString()}")
            self.assertEqual(result2.toString(), expected.toString(), f"ALTERNATIVE error caused at {linkedList.toString()} got {result.toString()} instead of {expected.toString()}")


unittest.main()