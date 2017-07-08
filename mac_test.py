import xml.etree.ElementTree as ET
import unittest
from mock import patch
import mac


class SetupInput(unittest.TestCase):
    def setUp(self):
        self.play = ET.parse('macbeth.xml').getroot()

    def tearDown(self):
        self.play = None


class MacTest(SetupInput):
    @patch('mac.speeches')
    def test_speeches_called(self, mock): #check 'speeches' is called for all 5 acts
        mac.acts(self.play)
        self.assertEqual(mock.call_count, 5)
