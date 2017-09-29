
from exercise import Exercise
from tools import simplify_spaces
import re

MARK = '*'
PLACEHOLDER = '...'

def concat(text1, text2):
    return text1 + text2

class EG_One(object):
    def __init__(self):
        self.pattern = re.compile('(\*?\w+|\*)')
      
    def get_words(self, line):
        line = simplify_spaces(line)
        parts = re.split(self.pattern, line)
        parts = filter(None, parts)
        #print 'parts =', parts
        return parts

    def generate(self, line):
        ex = []
        parts = self.get_words(line)
        for i in xrange(0, len(parts)):
            if len(parts[i])>0 and parts[i][0]==MARK:
                question = ''.join(parts[:i])
                question = question + PLACEHOLDER
                question = question + ''.join(parts[i+1:])
                question = question.replace(MARK, '')
                answer = parts[i][1:]
                ex.append(Exercise(question, answer))
                
        return ex
