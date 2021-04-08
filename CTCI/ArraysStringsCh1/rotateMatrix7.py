import unittest

def rotateMatrix(a): 
    
    #converts 2d array to one string
    strA = str(a).replace("[", "").replace("]", "").replace(" ", "")
    #gets how many rows in the 2d array; save data for later grouping later
    lenMatrix = len(a)



    newArr = []

    #creates a new list of numbers and converts from chars to ints 
    
    listNums = list(map(int, strA.split(",")))
    temp = listNums.copy()

    count = 0
    #will be updated differently 
    n = len(a)
    skip = len(a)
    while len(listNums) > 0: 
        #can't have skip reach 0 => causes error
        if skip == 0: 
            skip = 1

        for x in range(n - 1, len(listNums), skip): 

            val = listNums[x]
            #adds from unaltered list nums
            newArr.append(val)

            #deletes from temp list that will become listNums only after done getting all the values
            temp.remove(val)

        listNums = temp.copy()
        n -= 1
        skip -= 1

    matrix = []
    start = 0
    for x in range(1, lenMatrix+1 ): 
        matrix.append(newArr[start:x * lenMatrix])
        start += lenMatrix


    return matrix

class TestRotateMatrix(unittest.TestCase): 
    test_cases = [
                ([[1, 2, 3],  [4, 5, 6], [7, 8, 9]], [[3, 6, 9], [2, 5, 8], [1, 4, 7]]), 
                ([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]), 
                ([
                    [1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25],
                ],
                [
                    [21, 16, 11, 6, 1],
                    [22, 17, 12, 7, 2],
                    [23, 18, 13, 8, 3],
                    [24, 19, 14, 9, 4],
                    [25, 20, 15, 10, 5],
                ])]

    def test_rotate_matrix(self): 
        for inputMatrix, expected in self.test_cases: 
            result = rotateMatrix(inputMatrix)
            self.assertEqual(result, expected, f"Causes error with test case: {expected}, got {result}")

unittest.main()