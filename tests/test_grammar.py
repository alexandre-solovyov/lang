
# -*- coding: utf-8 -*-

import os
import unittest
from grammar import Rule
from model import Model, CATEGORY

class TestGrammar(unittest.TestCase):

    def __init__(self, arg):
        super(TestGrammar, self).__init__(arg)
        
    def test_rule(self):
        r = Rule("~er >> ~e, ~es, ~e, ~ons, ~ez, ~ent", "PrInd")
        self.assertEqual(r.input, '~er')
        self.assertEqual(r.output, ['~e', '~es', '~e', '~ons', '~ez', '~ent'])
        self.assertEqual(r.match('parler'), (True, 'parl'))
        self.assertEqual(r.match('er'), (True, ''))
        self.assertEqual(r.match('finir'), (False, ''))
        self.assertEqual(r.transform('parler'), ['parle', 'parles', 'parle', 'parlons', 'parlez', 'parlent'])
        self.assertEqual(r.transform('finir'), [])
        r2 = Rule("~cer >> ~ce, ~ces, ~ce, ~cons, ~cez, ~cent", "PrInd")
        self.assertEqual(r.includes(r2), True)
        self.assertEqual(r2.includes(r), False)

    def test_word_parts(self):
        r = Rule("~eu >> ~eux", "Pl")
        self.assertEqual(r.match('lieu'), (True, 'li'))
        self.assertEqual(r.match('heure'), (False, ''))
        self.assertEqual(r.transform('heure'), [])
        
    def test_compl_word_rule(self):
        r = Rule("aller >> vais, vas, va, allons, allez, vont", "PrInd")
        self.assertEqual(r.input, 'aller')
        self.assertEqual(r.output, ['vais', 'vas', 'va', 'allons', 'allez', 'vont'])
        self.assertEqual(r.match('aller'), (True, 'aller'))
        self.assertEqual(r.match('parler'), (False, ''))
        self.assertEqual(r.transform('aller'), ['vais', 'vas', 'va', 'allons', 'allez', 'vont'])
    
    def test_load(self):
        filename = 'test3.lang'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '..', 'testdata', filename)
        
        m = Model()
        self.assertEqual(m.load(path), True)
        
        self.assertEqual(m.forms.forms('parler', 'PrInd'), ['parle', 'parles', 'parle', 'parlons', 'parlez', 'parlent'])
        self.assertEqual(m.forms.init_forms('parle'), ['parler'])
        
        
if __name__ == '__main__':
    unittest.main()

