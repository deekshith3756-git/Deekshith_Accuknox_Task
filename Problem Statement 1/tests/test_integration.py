import requests
import unittest


class TestIntegration(unittest.TestCase):

    def test_frontend_to_backend(self):
        # Replace this URL with the actual Minikube service URL for the frontend
        frontend_url = 'http://127.0.0.1:51955'

        response = requests.get(frontend_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello from the Backend!', response.text)


if __name__ == '__main__':
    unittest.main()
