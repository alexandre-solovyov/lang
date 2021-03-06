﻿
# -*- coding: utf-8 -*-

import unittest
import os
import codecs
from eg_base import EG_Base
from eg_one import EG_One
from eg_trans import EG_Trans


class TestGenerators(unittest.TestCase):

    def __init__(self, arg):
        super(TestGenerators, self).__init__(arg)
        self.generators = [EG_One(), EG_Trans()]
        self.mode = 0

    def gen(self, line):
        g = self.generators[self.mode - 1]
        ex = g.generate(line, 'fr', 'ru', '')
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

    def test_tags(self):
        self.mode = 2
        self.assertEqual(self.gen(u"[просьба] s'il vous plaît = пожалуйста"),
                         [u"s'il vous plaît (пожалуйста) [fr, ru] #просьба",
                          u"пожалуйста (s'il vous plaît) [ru, fr] #просьба"])

    def test_syn(self):
        self.assertEqual(self.gen(u"accessible ~ disponible"),
                         [u"~ accessible (disponible) [fr, fr]",
                          u"~ disponible (accessible) [fr, fr]"])

    def test_ant(self):
        self.assertEqual(self.gen(u"clair != foncé"),
                         [u"!= clair (foncé) [fr, fr]",
                          u"!= foncé (clair) [fr, fr]"])

    def test_def_tag(self):
        g = EG_Base()
        self.assertEqual(g.tag, '')
    
    def test_tags(self):
        g = EG_Base()
        self.assertEqual(g.set_tag('abc'), 'abc')
        self.assertEqual(g.tag, '')
        self.assertEqual(g.set_tag('abc [f]gh'), 'abc gh')
        self.assertEqual(g.tag, 'f')
        self.assertEqual(g.set_tag('[f]gh'), 'gh')
        self.assertEqual(g.tag, 'f')
        self.assertEqual(g.set_tag('ab [fg]'), 'ab ')
        self.assertEqual(g.tag, 'fg')
        self.assertEqual(g.set_tag('test [f] test [g]'), 'test  test [g]')
        self.assertEqual(g.tag, 'f')
        
if __name__ == '__main__':
    unittest.main()

