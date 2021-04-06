import unittest

def urlify(string, lenString):
    strSplit = string.split()
    return "%".join(strSplit)

def testing(): 
    print(urlify("howdy  there", 14))
    print(urlify("no nose goes", 1))

class URLifyTestCase(unittest.TestCase):
    test_cases = [("idk how  this works", "idk%how%this%works"), 
    ("Forever a l one", "Forever%a%l%one")]

    def test_urlify(self): 
        for test_string, expected in self.test_cases:
            testCaseOutput = urlify(test_string, 0)
            assert testCaseOutput == expected
        
unittest.main()


