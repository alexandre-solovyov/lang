
class Exercise(object):
    def __init__(self, question, answer):
        self.question = question.strip()
        self.answer = answer.strip()

    def __repr__(self):
        return self.question + ' (' + self.answer + ')'

    def __unicode__(self):
        return self.__repr__()

    @staticmethod
    def placeholder():
        return '...'
