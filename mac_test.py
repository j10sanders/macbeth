import xml.etree.ElementTree as ET
import unittest
from mock import patch
import mac

class MacTest(unittest.TestCase):
    @patch('mac.get_input', return_value=['error'])
    def test_answer_yes(self, input):
        self.assertEqual(mac.parse_play(), ['error'])

    @patch('builtins.input', side_effect=['gibberish'])
    def test_bad_url(self, input):
    	self.assertEqual(mac.get_input(), ["Invalid URL 'gibberish': No schema supplied. Perhaps you meant http://gibberish?"])

    @patch('builtins.input', side_effect=['https://google.com'])
    def test_bad_xml(self, input):
    	self.assertEqual(mac.get_input(), ["That url doesn't have the right xml format :("])

    @patch('mac.get_input', return_value=ET.parse('macbeth.xml').getroot())
    def test_parse_play(self, input):
        self.assertEqual(mac.parse_play()[0], 'Macbeth has 719')
        self.assertEqual(mac.parse_play()[1], 'Lady Macbeth has 265')