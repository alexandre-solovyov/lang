
"""Module for exercises generator of marked words"""

from exercise import Exercise
from unicode_tools import simplify_spaces
from eg_base import EG_Base
import re


class EG_One(EG_Base):
    """The exercises generator of marked words"""

    def __init__(self):
        """Constructor"""
        super(EG_One, self).__init__()
        self.pattern = re.compile(r'(\*?\w+|\*)', re.UNICODE)

    @staticmethod
    def marks():
        """Used marks for words"""
        return ['*']

    def get_words(self, line):
        """Get all words in the given line"""
        line = simplify_spaces(line)
        parts = re.split(self.pattern, line)
        parts = filter(None, parts)
        # print 'parts =', parts
        return parts

    def generate(self, line, lang1, lang2, category):
        """Generate exercises from the given line"""
        line = self.set_tag(line)
        exercices = []
        parts = self.get_words(line)
        for i in xrange(0, len(parts)):
            if len(parts[i]) > 0 and parts[i][0] == self.marks()[0]:
                question = ''.join(parts[:i])
                question = question + Exercise.placeholder()
                question = question + ''.join(parts[i + 1:])
                question = question.replace(self.marks()[0], '')
                answer = parts[i][1:]
                exercices.append(
                    Exercise('', question, answer, lang1, lang1,
                             category, self.tag))

        return exercices
