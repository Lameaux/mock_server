import json

from tests.test_base import BaseTestCase, API_HEADERS


class MainTestCase(BaseTestCase):
    def test_404(self):
        response = self.client.get('/wrong/url', headers=API_HEADERS)
        self.assertEqual(response.status_code, 404)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status_code'], 404)
        self.assertTrue('error' in json_response)
