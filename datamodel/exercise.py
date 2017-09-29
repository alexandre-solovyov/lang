
class Exercise(object):
    def __init__(self, question, answer):
        self.question = question.strip()
        self.answer = answer.strip()

    def __repr__(self):
        return self.question + ' (' + self.answer + ')'
