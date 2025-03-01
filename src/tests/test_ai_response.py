import unittest
from src.services.ai_reply import generate_ai_response

class TestAIResponse(unittest.TestCase):
    def test_response(self):
        comment = "Nice product!"
        response = generate_ai_response(comment)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

if __name__ == "__main__":
    unittest.main()
