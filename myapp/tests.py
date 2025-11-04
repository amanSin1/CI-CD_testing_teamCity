from django.test import TestCase, Client

class SimpleTest(TestCase):
    def test_hello_endpoint(self):
        client = Client()
        response = client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
    
    def test_health_endpoint(self):
        client = Client()
        response = client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['health'], 'OK JAANU Ji')