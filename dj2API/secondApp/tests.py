from django.test import Client, TestCase
from secondApp.api import views

class RateLimiterTestCase(TestCase):
    
    def test_accuracy(self):
        limit = 5
        c = Client()
        for i in range(10):
            response = c.get('/second-app/second/')
            if(i < limit):
                self.assertEqual(response.status_code, 200)
            else:
                self.assertEqual(response.status_code, 403)

# Create your tests here.
