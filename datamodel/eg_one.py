
from exercise import Exercise
from tools import simplify_spaces
from eg_base import EG_Base
import re

class EG_One(EG_Base):
    def __init__(self):
        super(EG_One, self).__init__()
        self.pattern = re.compile('(\*?\w+|\*)', re.UNICODE)

    @staticmethod
    def mark():
        return '*'

    def get_words(self, line):
        line = simplify_spaces(line)
        parts = re.split(self.pattern, line)
        parts = filter(None, parts)
        #print 'parts =', parts
        return parts

    def generate(self, line, lang1, lang2, category):
        line = self.set_tag(line)
        ex = []
        parts = self.get_words(line)
        for i in xrange(0, len(parts)):
            if len(parts[i])>0 and parts[i][0]==self.mark():
                question = ''.join(parts[:i])
                question = question + Exercise.placeholder()
                question = question + ''.join(parts[i+1:])
                question = question.replace(self.mark(), '')
                answer = parts[i][1:]
                ex.append(Exercise('', question, answer, lang1, lang1, category, self.tag))
                
        return ex
