import json

from tests.test_base import BaseTestCase, API_HEADERS


class ExamplesTestCase(BaseTestCase):
    def test_random(self):
        response = self.client.get('/random', headers=API_HEADERS)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertTrue('random' in json_response)

    def test_timestamp(self):
        response = self.client.get('/timestamp', headers=API_HEADERS)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertTrue('timestamp' in json_response)
