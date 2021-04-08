import unittest

#turn enture row and columns 0 if element is == 0

def zeroMatrix(matrix): 
    #is this row meant to be all 0's 
    turnZero = False

    #for keeping track which columns are 0
    zeroIndexes = [False for x in range(0, len(matrix[1]))]

    for x in range(0, len(matrix)): 
        newRow = []
        for y in range(0, len(matrix[x])): 

            #makes sure that the elem isn't zero because then the column needs to be marked 
            if zeroIndexes[y] and matrix[x][y] != 0:
                matrix[x][y] = 0

            elif matrix[x][y] == 0: 
                #makes sure to turn row to all 0
                turnZero = True
                zeroIndexes[y] = True

        #makes sure to only convert row to zeros until all elements have been iterated through in the row
        if turnZero and y == len(matrix[x]) - 1: 
            matrix[x] = [0 for x in range(0, len(matrix[x]))]
            turnZero = False
    return matrix 

class TestZeroMatrix(unittest.TestCase): 
    test_cases = [([[1,2,0], [3,4,5]], [[0,0,0], [3,4,0]]), 
    (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 0, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 0, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 0, 0],
            ],
        )]

    def test_zero_matrix(self): 
        for matrix, expected in self.test_cases: 
            result = zeroMatrix(matrix)
            self.assertEqual(expected, result, f"ERROR: {matrix} returned {result} when {expected}")

unittest.main()
