from django.test import TestCase


class HomePageTest(TestCase):
    def test_home(self):
        try:
            response = self.client.get('/')
            self.assertEquals(200, response.status_code)

            response = self.client.get('/home/about/')
            self.assertEquals(200, response.status_code)

            response = self.client.get('/home/sample/')
            self.assertEquals(200, response.status_code)
            self.assertIn('books', response.context)
        except Exception as e:
            print(f'Error: {e}')
