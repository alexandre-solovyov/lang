
from exercise import Exercise
from tools import simplify_spaces
from eg_one import EG_One
from eg_base import EG_Base

class EG_Trans(EG_Base):
    def __init__(self):
        super(EG_Trans, self).__init__()
      
    @staticmethod
    def mark():
        return '='
      
    def generate(self, line, lang1, lang2, category):
        line = self.set_tag(line)
        ex = []
        line = simplify_spaces(line)
        parts = line.split(self.mark())
        if len(parts)==2:
            question = parts[0].strip()
            question = question.replace(EG_One.mark(), '')
            answer = parts[1].strip()
            answer = answer.replace(EG_One.mark(), '')
            ex.append(Exercise(question, answer, lang1, lang2, category, self.tag))
            ex.append(Exercise(answer, question, lang2, lang1, category, self.tag))
        return ex
