
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
        ex = g.generate(line)
        exs = [unicode(e) for e in ex]
        return exs
        
    def test_eg_one(self):
        self.mode = 1
        self.assertEqual(self.gen(''),
                         [])
        self.assertEqual(self.gen('couper'),
                         [])
        self.assertEqual(self.gen('couper *une pomme'),
                         ['couper ... pomme (une)'])
        self.assertEqual(self.gen('couper   *une    pomme'),
                         ['couper ... pomme (une)'])
        self.assertEqual(self.gen('couper *une pomme *en deux parties'),
                         ['couper ... pomme en deux parties (une)',
                          'couper une pomme ... deux parties (en)'])
        self.assertEqual(self.gen('*a *b *c *d *'),
                         ['... b c d (a)',
                          'a ... c d (b)',
                          'a b ... d (c)',
                          'a b c ... (d)',
                          'a b c d ... ()'])
        self.assertEqual(self.gen('*a, *b!'),
                         ['..., b! (a)',
                          'a, ...! (b)'])
        self.assertEqual(self.gen(u"c'est *un éternel mécontent"),
                         [u"c'est ... éternel mécontent (un)"])
        self.assertEqual(self.gen(u"c'est un *éternel mécontent"),
                         [u"c'est un ... mécontent (éternel)"])
        self.assertEqual(self.gen('aller *en Italie'),
                         ['aller ... Italie (en)'])
        self.assertEqual(self.gen('aller *au Japon'),
                         ['aller ... Japon (au)'])

    def test_eg_trans(self):
        self.mode = 2
        self.assertEqual(self.gen(u'*une scène = сцена'),
                         [u'une scène (сцена)',
                          u'сцена (une scène)'])
        self.assertEqual(self.gen(u'prévenir = предупредить'),
                         [u'prévenir (предупредить)',
                          u'предупредить (prévenir)'])

if __name__=='__main__':
    unittest.main()
