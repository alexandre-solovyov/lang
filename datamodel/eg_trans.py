
from exercise import Exercise
from tools import simplify_spaces
from eg_one import EG_One

class EG_Trans(object):
    def __init__(self):
        pass
      
    @staticmethod
    def mark():
        return '='
      
    def generate(self, line, lang1, lang2):
        ex = []
        line = simplify_spaces(line)
        parts = line.split(self.mark())
        if len(parts)==2:
            question = parts[0].strip()
            question = question.replace(EG_One.mark(), '')
            answer = parts[1].strip()
            answer = answer.replace(EG_One.mark(), '')
            ex.append(Exercise(question, answer, lang1, lang2))
            ex.append(Exercise(answer, question, lang2, lang1))
        return ex
