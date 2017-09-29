
# -*- coding: utf-8 -*-

import unittest
import os
import codecs
from eg_one import EG_One
from eg_trans import EG_Trans

class TestGenerators(unittest.TestCase):
    def __init__(self, arg):
        super(TestGenerators, self).__init__(arg)
        self.generators = [EG_One(), EG_Trans()]
        self.mode = 0
        
    def gen(self, line):
        g = self.generators[self.mode-1]
        ex = g.generate(line, 'fr', 'ru')
        exs = [unicode(e) for e in ex]
        return exs
        
    def test_eg_one(self):
        self.mode = 1
        self.assertEqual(self.gen(''),
                         [])
        self.assertEqual(self.gen('couper'),
                         [])
        self.assertEqual(self.gen('couper *une pomme'),
                         ['couper ... pomme (une) [fr, fr]'])
        self.assertEqual(self.gen('couper   *une    pomme'),
                         ['couper ... pomme (une) [fr, fr]'])
        self.assertEqual(self.gen('couper *une pomme *en deux parties'),
                         ['couper ... pomme en deux parties (une) [fr, fr]',
                          'couper une pomme ... deux parties (en) [fr, fr]'])
        self.assertEqual(self.gen('*a *b *c *d *'),
                         ['... b c d (a) [fr, fr]',
                          'a ... c d (b) [fr, fr]',
                          'a b ... d (c) [fr, fr]',
                          'a b c ... (d) [fr, fr]',
                          'a b c d ... () [fr, fr]'])
        self.assertEqual(self.gen('*a, *b!'),
                         ['..., b! (a) [fr, fr]',
                          'a, ...! (b) [fr, fr]'])
        self.assertEqual(self.gen(u"c'est *un éternel mécontent"),
                         [u"c'est ... éternel mécontent (un) [fr, fr]"])
        self.assertEqual(self.gen(u"c'est un *éternel mécontent"),
                         [u"c'est un ... mécontent (éternel) [fr, fr]"])
        self.assertEqual(self.gen('aller *en Italie'),
                         ['aller ... Italie (en) [fr, fr]'])
        self.assertEqual(self.gen('aller *au Japon'),
                         ['aller ... Japon (au) [fr, fr]'])

    def test_eg_trans(self):
        self.mode = 2
        self.assertEqual(self.gen(u'*une scène = сцена'),
                         [u'une scène (сцена) [fr, ru]',
                          u'сцена (une scène) [ru, fr]'])
        self.assertEqual(self.gen(u'prévenir = предупредить'),
                         [u'prévenir (предупредить) [fr, ru]',
                          u'предупредить (prévenir) [ru, fr]'])

if __name__=='__main__':
    unittest.main()
