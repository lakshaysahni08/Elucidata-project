from django.test import TestCase

# Create your tests here.

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_filter_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/filter')
        self.assertEqual(response.status_code, 301)
        
    def test_round_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/round')
        self.assertEqual(response.status_code, 301)

    def test_mean_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/mean')
        self.assertEqual(response.status_code, 301)         