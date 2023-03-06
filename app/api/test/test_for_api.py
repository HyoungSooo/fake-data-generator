from django.test import TestCase, Client
import json
import unittest

class TestParsing(unittest.TestCase):
    
    def setUp(self) -> None:
        self.c = Client()
        return 
    
    def test_get_random_names_api_with_country(self):
        for i in ['it_IT', 'en_US', 'ja_JP']:
            res = self.c.get(f'/api/single_value/names?country={i}')

            data = json.loads(res.content)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(data), 1)

    def test_get_random_names_many(self):
        for i in [10,20,30]:
            res = self.c.get(f'/api/single_value/names?count={i}')
            data = json.loads(res.content)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(data), i)

    def test_get_random_names_without_any_query(self):
        res = self.c.get(f'/api/single_value/names')

        self.assertEqual(len(json.loads(res.content)), 1)

    def test_get_random_names_split_first_last(self):
        res = self.c.get(f'/api/single_value/names?split=True')
        data = json.loads(res.content)
        self.assertEqual(len(data), 1)
        for key, value in data.items():          
          self.assertEqual(len(data[key]), 2)
            
    def test_get_random_address(self):
        url = '/api/single_value/address'
        for i in [10,20,30]:
            res = self.c.get(url + f'?count={i}')
            data = json.loads(res.content)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(len(data), i)

        category = ['city', 'city__suffix', 'country', 'country__code', 'street_name']
        
        for i in category:
          res = self.c.get(url + f'?category={i}')

          self.assertEqual(res.status_code, 200)
          self.assertEqual(len(json.loads(res.content)), 1)

    def test_get_random_license_plate(self):
        url = '/api/single_value/licenseplate?count=10'
        res = self.c.get(url)

        data = json.loads(res.content)

        self.assertEqual(len(data), 10)
        self.assertEqual(res.status_code, 200)



    
    


