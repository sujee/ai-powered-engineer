import unittest
from zipcode import extract_zip_codes

class TestExtractZipCodes(unittest.TestCase):
    def test_single_zip_code(self):
        text = "Beverly Hills, 90210"
        self.assertEqual(extract_zip_codes(text), ['90210'])

    def test_multiple_zip_codes(self):
        text = "Locations: 90210, 10001, 62704"
        self.assertEqual(extract_zip_codes(text), ['90210', '10001', '62704'])

    def test_no_zip_codes(self):
        text = "No zip codes in this text"
        self.assertEqual(extract_zip_codes(text), [])

    def test_zip_codes_at_boundaries(self):
        text = "12345 is at start and end 67890"
        self.assertEqual(extract_zip_codes(text), ['12345', '67890'])

    def test_invalid_zip_formats(self):
        text = "1234 123456 12345"  # 4 digits, 6 digits, valid zip
        self.assertEqual(extract_zip_codes(text), ['12345'])

    def test_zip_in_longer_numbers(self):
        text = "1234567890 0123456789"
        self.assertEqual(extract_zip_codes(text), [])

    def test_edge_cases(self):
        self.assertEqual(extract_zip_codes(""), [])
        self.assertEqual(extract_zip_codes("12345"), ['12345'])
        self.assertEqual(extract_zip_codes("!@#$%"), [])

if __name__ == '__main__':
    unittest.main()