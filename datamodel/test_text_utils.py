
# -*- coding: utf-8 -*-

import unittest
from unicode_tools import normalize


class TestTextUtils(unittest.TestCase):

    def __init__(self, arg):
        super(TestTextUtils, self).__init__(arg)

    def test_normalize(self):
        self.assertEqual(normalize(u""),         u"")
        self.assertEqual(normalize(u"abc"),      u"abc")
        self.assertEqual(normalize(u"parler"),   u"parler")
        self.assertEqual(normalize(u"parle/"),   u"parlé")
        self.assertEqual(normalize(u"parle'"),   u"parlé")
        self.assertEqual(normalize(u"de'cide'"), u"décidé")
        self.assertEqual(normalize(u"a` Lyon"),  u"à Lyon")

    def test_answer_compare(self):
        # TODO
        pass

if __name__ == '__main__':
    unittest.main()
