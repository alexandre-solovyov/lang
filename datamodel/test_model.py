
# -*- coding: utf-8 -*-

import unittest
import os
import codecs
from model import Model
from statistics import Stat

def load(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #print dir_path
    path = os.path.join(dir_path, '..', 'testdata', filename)
    model = Model()
    model.load(path)
    return model
    
class TestModel(unittest.TestCase):
    def test_load(self):
        model = load('test1.lang')
        self.assertEqual(len(model.lines), 3)
        self.assertEqual(model.lines[0].text, u'un modèle = модель')
        self.assertEqual(model.lines[0].context,
                         {'category':'basic', 'date':'June, 29', 'lang':'fr, ru'})
        self.assertEqual(model.lines[1].text, u'un problème = проблема')
        self.assertEqual(model.lines[1].context,
                         {'category':'basic', 'date':'June, 29', 'lang':'fr, ru'})
        self.assertEqual(model.lines[2].text, u'parler = говорить')
        self.assertEqual(model.lines[2].context,
                         {'category':'verbs', 'date':'June, 29', 'lang':'fr, ru'})
        self.assertEqual(model.language(), ['fr', 'ru'])
    
    def test_load_unexisting_file(self):
        model = Model()
        self.assertEqual(model.load('some_not_existing'), False)

    def test_save(self):
        model = load('test1.lang')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '..', 'testresults', 'test1_copy.lang')
        model.save(path)
        mfile = codecs.open(path, 'rb', 'utf-8')
        file_contents = mfile.read()
        self.assertEqual(file_contents, u"""
//! lang: fr, ru
//! date: June, 29
//! category: basic
un modèle = модель
un problème = проблема

//! category: verbs
parler = говорить
""")

    def test_categories(self):
        model = load('test1.lang')
        self.assertEqual(model.values('category'), ['basic', 'verbs'])
        self.assertEqual(model.value(model.lines[1], 'category'), 'basic')
        self.assertEqual(model.value(model.lines[1], 'other'), None)

    def test_add(self):
        model = Model()
        self.assertEqual(len(model.lines), 0)
        self.assertEqual(model.add(''), False)
        self.assertEqual(len(model.lines), 0)
        self.assertEqual(model.add('   '), False)
        self.assertEqual(len(model.lines), 0)
        self.assertEqual(model.add(' a =  b  '), True)
        self.assertEqual(len(model.lines), 1)
        self.assertEqual(model.lines[0].text, 'a = b')
        self.assertEqual(model.lines[0].context, {})
        self.assertEqual(model.add('   a   = b'), False)  # the second time 
        self.assertEqual(len(model.lines), 1)
        self.assertEqual(model.add(' c d  ', {'date':'-'}), True)
        self.assertEqual(len(model.lines), 2)
        self.assertEqual(model.lines[1].text, 'c d')
        self.assertEqual(model.lines[1].context, {'date':'-'})
        self.assertEqual(model.add(' e  ', {'test':'0'}), True)
        self.assertEqual(len(model.lines), 3)
        self.assertEqual(model.lines[2].text, 'e')
        self.assertEqual(model.lines[2].context, {'date':'-', 'test':'0'})

    def test_exercises(self):
        model = load('test2.lang')
        self.assertEqual(model.values('category'), ['basic'])
        self.assertEqual(len(model.lines), 6)
        self.assertEqual(len(model.exercises), 12)
        e = model.exercises[5]
        self.assertEqual(e.question, u'une scène')
        self.assertEqual(e.answer, u'сцена')

    def test_stat(self):
        model = load('test2.lang')
        s = Stat(model)
        self.assertEqual(s.exercises, 12)
        self.assertEqual(s.words, 17)
        self.assertEqual(s.fwords, 16)
        self.assertEqual(s.swords, 7)

         
if __name__=='__main__':
    unittest.main()
