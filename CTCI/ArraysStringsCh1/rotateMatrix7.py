import itertools 

def rotateMatrixForward(matrix): 

    a = [[1, 2, 3],  [4, 5, 6], [7, 8, 9]]
    n = len(a) - 1
        
    newArr = []

    strA = str(a).replace("[", "").replace("]", "").replace(" ", "")
    listNums = strA.split(",")

    temp = listNums.copy()
    print(temp)

    nu = len(listNums)
    for x in range(n, nu, n + 1): 
        print(x)

    while nu > 0: 
        for x in range(n, nu, n + 1): 
            print(x)
            print(listNums)
            aNum = listNums[x]
            rem = temp.remove(aNum)
            newArr.append(aNum)
        nu = len(listNums)
        n -= 1
        listNums = temp
    print(listNums)
    print(listNums)

def rotateMatrixBackward(a): 
    a = [[1, 2, 3],  [4, 5, 6], [7, 8, 9]]
    n = len(a) - 1
        
    newArr = []

    strA = str(a).replace("[", "").replace("]", "").replace(" ", "")
    listNums = strA.split(",")

    temp = listNums.copy()
    lenAMinN = len(a) - (n + 1)
    get = len(a) - 1
    
    count = 0
    while len(temp) > 0 : 
        x = listNums[get]
        temp.remove(x)
        newArr.append(x)
        
        get -= n 
        count += 1
        if count == 10: 
            break
        

rotateMatrixBackward([1,2,3])