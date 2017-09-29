
class Exercise(object):
    def __init__(self, question, answer, lang1, lang2):
        self.question = question.strip()
        self.answer = answer.strip()
        self.lang1 = lang1
        self.lang2 = lang2

    def __repr__(self):
        return "%s (%s) [%s, %s]" % ( self.question, self.answer, self.lang1, self.lang2 )

    def __unicode__(self):
        return self.__repr__()

    @staticmethod
    def placeholder():
        return '...'
