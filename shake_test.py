import xml.etree.ElementTree as ET
import unittest
from mock import patch
import shake

class SetupInput(unittest.TestCase):
    def setUp(self):
        self.play = ET.parse('macbeth.xml').getroot()

    def tearDown(self):
        self.play = None


class MacTest(SetupInput):
	@patch('shake.get_input', return_value=['error'])
	def test_answer_yes(self, input):
		self.assertEqual(shake.parse_play(), ['error'])

	@patch('shake.get_input', return_value=[])
	def test_no_imput(self, input):
		self.assertEqual(shake.parse_play(), ['Error: no argument for XML tree'])

	@patch('builtins.input', side_effect=['gibberish'])
	def test_bad_url(self, input):
		self.assertEqual(shake.get_input(), ["Invalid URL 'gibberish': No schema supplied. Perhaps you meant http://gibberish?"])

	@patch('builtins.input', side_effect=['https://google.com'])
	def test_bad_xml(self, input):
		self.assertEqual(shake.get_input(), ["That url doesn't have the right xml format :("])

	def test_tree_arg(self):
		self.assertEqual(shake.parse_play(self.play)[0], 'Macbeth has 719')
		self.assertEqual(shake.parse_play(self.play)[1], 'Lady Macbeth has 265')

	@patch('shake.get_input', return_value=ET.parse('macbeth.xml').getroot())
	def test_parse_play(self, input):
		self.assertEqual(shake.parse_play()[0], 'Macbeth has 719')
		self.assertEqual(shake.parse_play()[1], 'Lady Macbeth has 265')