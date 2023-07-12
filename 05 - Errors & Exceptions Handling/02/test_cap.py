import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result,"Python") #there won't be an error
        
    def test_multiple_words(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result,"Monty Python") #there will be an error
        
if __name__ == "__main__":
    unittest.main()
