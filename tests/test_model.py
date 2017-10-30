
# -*- coding: utf-8 -*-

import unittest
import os
import codecs
from model import Model, Line, line_cmp
from statistics import Stat


def load(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # print dir_path
    path = os.path.join(dir_path, '..', 'testdata', filename)
    model = Model()
    model.load(path)
    return model


class TestModel(unittest.TestCase):

    def test_load(self):
        model = load('test1.lang')
        self.assertEqual(len(model.lines), 4)
        self.assertEqual(model.lines[1].text, u'un modèle = модель')
        self.assertEqual(model.lines[1].context,
                         {'category': 'basic', 'date': 'June, 29',
                          'lang': 'fr, ru'})
        self.assertEqual(model.lines[2].text, u'un problème = проблема')
        self.assertEqual(model.lines[2].context,
                         {'category': 'basic', 'date': 'June, 29',
                          'lang': 'fr, ru'})
        self.assertEqual(model.lines[3].text, u'parler = говорить')
        self.assertEqual(model.lines[3].context,
                         {'category': 'verbs', 'date': 'June, 29',
                          'lang': 'fr, ru'})
        self.assertEqual(model.language(), ['fr', 'ru'])

    def test_load_unexisting_file(self):
        model = Model()
        self.assertEqual(model.load('some_not_existing'), False)

    def test_save(self):
        model = load('test1.lang')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '..', 'testresults',
                            'test1_copy.lang')
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
        self.assertEqual(model.value(model.lines[1], 'category'),
                         'basic')
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
        self.assertEqual(model.add('   a   = b'), False)
        # the second time the model does not add the same item

        self.assertEqual(len(model.lines), 1)
        self.assertEqual(model.add(' c d  ', {'date': '-'}), True)
        self.assertEqual(len(model.lines), 2)
        self.assertEqual(model.lines[1].text, 'c d')
        self.assertEqual(model.lines[1].context, {'date': '-'})
        self.assertEqual(model.add(' e  ', {'test': '0'}), True)
        self.assertEqual(len(model.lines), 3)
        self.assertEqual(model.lines[2].text, 'e')
        self.assertEqual(model.lines[2].context,
                         {'date': '-', 'test': '0'})

    def test_exercises(self):
        model = load('test2.lang')
        self.assertEqual(model.values('category'), ['basic'])
        self.assertEqual(len(model.lines), 7)
        self.assertEqual(len(model.exercises), 1)
        self.assertEqual(len(model.exercises['basic']), 12)
        e = model.exercises['basic'][5]
        self.assertEqual(e.question, u'une scène')
        self.assertEqual(e.answer, u'сцена')

    def test_stat(self):
        model = load('test2.lang')
        s = Stat(model)
        self.assertEqual(s.exercises, 12)
        self.assertEqual(len(s.words), 17)
        self.assertEqual(len(s.fwords), 14)
        self.assertEqual(len(s.swords), 7)

    def test_compare_lines(self):
        model = Model()
        model.short_ignore = ['une', 'un']

	line1 = Line('*un poste', {'category': 'basic'}, model)
	line2 = Line(u'une île = остров', {'category': 'basic'}, model)
	self.assertEqual(line1.text < line2.text, True)
	self.assertEqual(line_cmp(line1, line2), 1)

	line1 = Line('abc', {'category': 'basic'}, model)
	line2 = Line(u'def', {'category': 'basic'}, model)
	self.assertEqual(line1.text < line2.text, True)
	self.assertEqual(line_cmp(line1, line2), -1)

	line1 = Line('*une ville', {'category': 'basic'}, model)
	line2 = Line('artifice', {'category': 'basic'}, model)
	self.assertEqual(line1.text < line2.text, True)
	self.assertEqual(line_cmp(line1, line2), 1)

	line1 = Line('[Pl] lieu', {'category': 'basic'}, model)
	line2 = Line('artifice', {'category': 'basic'}, model)
	self.assertEqual(line1.text < line2.text, True)
	self.assertEqual(line_cmp(line1, line2), 1)

if __name__ == '__main__':
    unittest.main()

