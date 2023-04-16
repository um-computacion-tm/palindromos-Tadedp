import unittest
from palindrome import isPalindrome, isPalindromeRecursive
from palindromePhrase import isPalindromePhrase

class TestPalindrome(unittest.TestCase):
    def testVoid(self):
        result = isPalindrome("")
        self.assertEqual(result, True)
     
    def testSimple(self):
        result = isPalindrome("ala")
        self.assertEqual(result, True)
    
    def testComplex(self):
        result = isPalindrome("Neuquen")
        self.assertEqual(result, True)
    
    def testSuperComplex(self):
        result = isPalindrome("SomEtEMOS")
        self.assertEqual(result, True)
    
    def testVoidRecursive(self):
        result = isPalindromeRecursive("")
        self.assertEqual(result, True)
    
    def testSimpleRecursive(self):
        result = isPalindromeRecursive("ala")
        self.assertEqual(result, True)
    
    def testComplexRecursive(self):
        result = isPalindromeRecursive("Neuquen")
        self.assertEqual(result, True)
    
    def testSuperComplexRecursive(self):
        result = isPalindromeRecursive("SomEtEMOS")
        self.assertEqual(result, True)
        
    def testVoidPhrase(self):
        result = isPalindromePhrase("")
        self.assertEqual(result, True)

    def testSimplePhrase(self):
        result = isPalindromePhrase("Neu/que n")
        self.assertEqual(result, True)

    def testComplexPhrase(self):
        result = isPalindromePhrase("Agita falsos usos la fatiga.")
        self.assertEqual(result, True)
    
if __name__ == '__main__':
    unittest.main()