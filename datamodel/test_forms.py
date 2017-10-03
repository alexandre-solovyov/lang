
# -*- coding: utf-8 -*-

import os
import unittest
from unicode_tools import normalize, ext_concat
from forms import Forms


class TestForms(unittest.TestCase):

    def __init__(self, arg):
        super(TestForms, self).__init__(arg)
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = 'forms.lang'
        path = os.path.join(dir_path, '..', 'testdata', filename)
        
        self.f1 = Forms(True)
        self.f1.load(path)
        self.f2 = Forms(False)
        self.f2.load(path)

    def test_pr_ind_I_gr(self):
        self.assertEqual(self.f1.forms(u"parler", "PrInd"),
                         ['parle', 'parles', 'parle', 'parlons', 'parlez', 'parlent'])
        self.assertEqual(self.f2.forms(u"parler", "PrInd"),
                         ['parle', 'parles', 'parlons', 'parlez', 'parlent'])
        self.assertEqual(self.f1.init_forms(u"parle"), ['parler'])
        self.assertEqual(self.f2.init_forms(u"parle"), ['parler'])
        self.assertEqual(self.f1.init_forms(u"parlons"), ['parler'])
        self.assertEqual(self.f2.init_forms(u"parlons"), ['parler'])

if __name__ == '__main__':
    unittest.main()
