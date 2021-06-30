import unittest
from Bitcoin import getBitcoindata, parseJson, convertJson, addtoPriceIndex

class TestFileName(unittest.TestCase):
    def test_url_connection(self):
        self.assertEqual(getBitcoindata().status_code, 200)


    def test_convertJson(self):
        self.assertTrue(len(convertJson(getBitcoindata())) > 0)
        self.assertNotEqual(parseJson(convertJson(getBitcoindata())), "")


    def test_parse_json(self):
        self.assertEqual(len(parseJson(convertJson(getBitcoindata()))), 4)
        vals = parseJson(convertJson(getBitcoindata()))
        self.assertNotEqual(vals[0], "")
        self.assertNotEqual(vals[1], "")
        self.assertNotEqual(vals[2], "")
        self.assertNotEqual(vals[3], "")
        self.assertTrue(len(vals[0]) == 25)
        self.assertTrue(len(vals[1]) >= 10)  # Assumes BTC will never crash
        self.assertTrue(len(vals[2]) >= 10)  # below $1000 dollars
        self.assertTrue(len(vals[3]) >= 10)


if __name__ == '__main__':
    unittest.main()
