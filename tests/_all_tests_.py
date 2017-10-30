
import unittest

from test_model import TestModel
from test_generators import TestGenerators
from test_unicode_tools import TestUnicodeTools
from test_grammar import TestGrammar

from unicode_tools import init

try:
    init()
    unittest.main()
except Exception as error:
    print "Unexpected error:", format(error)
