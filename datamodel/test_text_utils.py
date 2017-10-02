
# -*- coding: utf-8 -*-

import unittest
from unicode_tools import normalize, ext_concat


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

    def test_ext_concat(self):
        self.assertEqual(ext_concat('a', 'b'), 'ab')
        self.assertEqual(ext_concat(['je', 'il'], ' parle'),
                         ['je parle', 'il parle'])
        self.assertEqual(ext_concat('parl', ['e', 'es', 'ons']),
                         ['parle', 'parles', 'parlons'])
        p1 = ['e', 'es', 'e', 'ons', 'ez', 'ent']
        self.assertEqual(ext_concat('parler', '~~', p1),
                         ['parle', 'parles', 'parle', 'parlons',
                          'parlez', 'parlent'])
                          
    def test_replace(self):
        s = 'ext'
        t = s.replace('e', '')
        self.assertEqual(s, 'ext')
        self.assertEqual(t, 'xt')

if __name__ == '__main__':
    unittest.main()
