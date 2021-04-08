import unittest

def zeroMatrix(matrix): 

    indexZero = []
    zero = False
    # for x in matrix: 
    #     for num in range(0, len(x)):
    #         if x[num] == 0: 
    #             indexZero.append(num)
    #             zero = True
    #         #check if current index is in index zero
            

    #     x = [0 for x in range(0, len(x))]
    #     zero = False
    turnZero = False
    zeroIndexes = [False for x in range(0, len(matrix[1]))]

    for x in range(0, len(matrix)): 
        newRow = []
        for y in range(0, len(matrix[x])): 
            if zeroIndexes[y] and matrix[x][y] != 0:
                matrix[x][y] = 0

            elif matrix[x][y] == 0: 
                turnZero = True
                zeroIndexes[y] = True
        if turnZero: 
            matrix[x] = [0 for x in range(0, len(matrix[x]))]
            turnZero = False
    return matrix 

class TestZeroMatrix(unittest.TestCase): 
    test_cases = [([[1,2,0], [3,4,5]], [[0,0,0], [3,4,0]]), 
    (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )]

    def test_zero_matrix(self): 
        for matrix, expected in self.test_cases: 
            result = zeroMatrix(matrix)
            self.assertEqual(result, expected, f"ERROR: {matrix} returned {result} when {expected}")

unittest.main()
