
import unittest

from test_model import TestModel
from test_generators import TestGenerators
from test_text_utils import TestTextUtils
from unicode_tools import init

try:
    init()
    unittest.main()
except Exception as error:
    print "Unexpected error:", format(error)
