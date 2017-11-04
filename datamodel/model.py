
# -*- coding: utf-8 -*-

"""Implementation of the LANG data model"""


import codecs
import copy
import os
import glob
from unicode_tools import simplify_spaces, to_latin
from eg_one import EG_One
from eg_trans import EG_Trans
from eg_grammar import EG_Grammar
from forms import Forms

ENCODING = 'utf-8'
DATA_FILES = '*.lang'
LANGUAGE = 'lang'
SEP = ', '
CATEGORY = 'category'
IGNORE_FILE = 'ignore'


class Line(object):
    """Line information"""

    def __init__(self, text, context, model):
        """Constructor"""
        self.text = text
        self.context = copy.deepcopy(context)
        self.model = model

    def __repr__(self):
        """Representation"""
        return self.text

    def __unicode__(self):
        """Unicode representation"""
        return self.text

    def cmp_repr(self):
        """Extended representation"""
        txt = self.model.short_simplify(self.text)
        txt = to_latin(txt)
        txt = txt.strip()
        return repr(self.context) + ' ' + txt


class Separator(object):
    """Separator information"""

    def __init__(self, filename):
        """Constructor"""
        self.filename = filename
        self.context = {}
        self.text = ''


def line_cmp(a, b):
    """Compare two lines"""
    ash = a.cmp_repr()
    bsh = b.cmp_repr()
    # print ash, bsh
    if ash < bsh:
        return -1
    else:
        return 1


class Model(object):
    """Model implementation"""

    def __init__(self):
        """Constructor"""
        self.lines = []
        self.context = {}
        self._language = []
        self.exercises = {}
        self.generators = [EG_One(), EG_Trans(), EG_Grammar(self)]
        self.ignore = []
        self.short_ignore = []
        self.forms = Forms(True)

    def language(self):
        """Get language of the model"""
        return self._language

    def load(self, filename):
        """Load the model from a file"""
        if not os.path.isfile(filename):
            return False

        mfile = codecs.open(filename, 'rb', ENCODING)
        lines = mfile.readlines()
        mfile.close()
        self.lines.append(Separator(filename))

        for line in lines:
            line = self.simplify(line)
            if len(line.text) > 0:
                self.lines.append(line)

        self.update_exercises()
        return True

    def all_files(self, dir_path):
        """Get all data files from given folder"""
        mask = os.path.join(dir_path, DATA_FILES)
        files = glob.glob(mask)
        return files

    def load_dir(self, dir_path):
        ok = True
        for f in self.all_files(dir_path):
            lok = self.load(f)
            ok = ok and lok

        fignore = os.path.join(dir_path, IGNORE_FILE)
        if os.path.isfile(fignore):
            mfile = codecs.open(fignore, 'rb', ENCODING)
            self.ignore = [l.strip().lower() for l in mfile.readlines()]
            # print self.ignore
            mfile.close()

        return ok

    def diff_context(self, old_context, new_context):
        diff = {}
        for key, value in new_context.iteritems():
            if key not in old_context or old_context[key] != value:
                diff[key] = value
        return diff

    def save(self, filename):
        self.filename = filename
        mfile = codecs.open(filename, 'wb', ENCODING)
        old_context = {}
        for line in self.lines:
            if isinstance(line, Separator):
                # TODO: to treat correctly the separator
                continue
            diff = self.diff_context(old_context, line.context)
            if len(diff) > 0:
                mfile.write('\n')
                for key, value in diff.iteritems():
                    mfile.write('//! %s: %s\n' % (key, value))
            old_context = line.context
            mfile.write(line.text + '\n')
        mfile.close()

    def simplify(self, line):
        line = simplify_spaces(line)
        line = self.comment(line)
        return line

    def comment(self, line):
        if '#' in line:
            index = line.index('#')
            length = 1
        elif '//' in line:
            index = line.index('//')
            length = 2
        else:
            return Line(line, self.context, self)

        comment = line[index + length:]
        if len(comment) > 0 and comment[0] == '!':
            # this is the interpreted comment
            comment = comment[1:]
            parts = comment.split(':')
            if len(parts) == 2:
                p1 = parts[0].strip()
                p2 = parts[1].strip()
                self.context[p1] = p2
                self.onContextChanged()

        text = line[:index]
        line = Line(text, self.context, self)
        return line

    def value(self, line, key):
        if key in line.context:
            return line.context[key]
        else:
            return None

    def values(self, key):
        values_set = set()
        for line in self.lines:
            line_value = self.value(line, key)
            if line_value is not None:
                values_set.add(line_value)
        values_lst = list(values_set)
        values_lst.sort()
        return values_lst

    def update_exercises(self):
        self.exercises = {}

        lang1 = ''
        lang2 = ''
        if len(self._language) > 0:
            lang1 = self._language[0]
        if len(self._language) > 1:
            lang2 = self._language[1]

        # print len(self.lines)
        for line in self.lines:
            if isinstance(line, Separator):
                for g in self.generators:
                    g.set_file(line.filename)
                continue

            # print line.text
            for g in self.generators:
                cat = line.context[CATEGORY]
                if cat not in self.exercises:
                    self.exercises[cat] = []

                ex = g.generate(
                    line.text, lang1, lang2, cat)
                for e in ex:
                    # print e.question, e.answer
                    self.exercises[cat].append(e)

    def add(self, text, context=None):
        text = simplify_spaces(text)
        if len(text) == 0:
            return False

        for line in self.lines:
            if line.text == text:
                return False
        if len(self.lines) > 0:
            cur_context = copy.deepcopy(self.lines[-1].context)
        else:
            cur_context = {}
        if context is not None:
            for key, value in context.iteritems():
                cur_context[key] = value
        new_line = Line(text, cur_context, self)
        self.lines.append(new_line)
        self.context = cur_context
        self.onContextChanged()
        return True

    def onContextChanged(self):
        if LANGUAGE in self.context:
            self._language = self.context[LANGUAGE].split(SEP)

    def short_simplify(self, line):
        txt = line
        while True:
            p1 = txt.find('[')
            p2 = txt.find(']')
            if p1 >= 0 and p2 >= 0:
                txt = txt[:p1] + txt[p2 + 1:]
                # print '>>'+txt+'<<'
            else:
                break

        for g in self.generators:
            for m in g.marks():
                txt = txt.replace(m, '')
        txt = txt.strip()
        for i in self.short_ignore:
            txt = txt.replace(i, '')
        return txt

    def sort(self):
        self.lines.sort(line_cmp)
