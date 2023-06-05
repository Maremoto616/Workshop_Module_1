# Write a Python function called is_palindrome that checks if a given word is a
# palindrome. The function should have proper error handling and be tested with
# unittest.

import unittest

def is_palindrome(palabra):
    palabra = palabra.lower()  
    palabra = palabra.replace(" ", "") 
    return palabra == palabra[::-1]

class PalindromeTest(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("somos o no somos"))
        self.assertFalse(is_palindrome("palindrome"))
        self.assertTrue(is_palindrome("Se laminan animales"))

    def test_input_palindrome(self):
        self.assertTrue(is_palindrome(input("Ingrese una palabra: ")))
    

if __name__ == '__main__':
    unittest.main()


