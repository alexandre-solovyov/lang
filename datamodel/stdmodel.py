
from datamodel.model import Model


class StdModel(Model):

    def __init__(self):
        super(StdModel, self)

    def add(self, text, category):
        context = {}
        context[CATEGORY] = category
        context[DATE] =
        super(StdModel, self).add(text, context)
