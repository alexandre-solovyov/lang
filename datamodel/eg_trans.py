
from exercise import Exercise
from tools import simplify_spaces
from eg_one import EG_One
from eg_base import EG_Base


class EG_Trans(EG_Base):

    def __init__(self):
        super(EG_Trans, self).__init__()

    @staticmethod
    def marks():
        return ['~', '!=', '=']

    def generate(self, line, lang1, lang2, category):
        line = self.set_tag(line)
        ex = []
        line = simplify_spaces(line)

        for mark in self.marks():
            parts = line.split(mark)
            if len(parts) == 2:
                question = parts[0].strip()
                question = question.replace(EG_One.mark(), '')
                answer = parts[1].strip()
                answer = answer.replace(EG_One.mark(), '')

                etype = mark
                if mark == '=':
                    etype = ''
                else:
                    lang2 = lang1

                ex.append(
                    Exercise(etype, question, answer, lang1, lang2,
                             category, self.tag))
                ex.append(
                    Exercise(etype, answer, question, lang2, lang1,
                             category, self.tag))

                break
        return ex
