
# -*- coding: utf-8 -*-

import unittest
import os
import codecs
from eg_one import EG_One

class TestGenerators(unittest.TestCase):
    def __init__(self, arg):
        super(TestGenerators, self).__init__(arg)
        self.g = EG_One()
        
    def gen(self, line):
        ex = self.g.generate(line)
        exs = [repr(e) for e in ex]
        return exs
        
    def test_eg_one(self):
        
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

if __name__=='__main__':
    unittest.main()
