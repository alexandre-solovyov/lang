
import unittest

from test_model import TestModel
from test_generators import TestGenerators

try:
    unittest.main()
except Exception as error:
    print "Unexpected error:", format(error)
