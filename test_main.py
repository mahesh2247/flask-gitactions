import json
import unittest
from main import app

class HelloApiTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_hello_endpoint(self):
        response = self.app.get("/")
        self.assertEqual(
            response.data,
            b'{"message":"Welcome to my app"}\n'
        )
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()