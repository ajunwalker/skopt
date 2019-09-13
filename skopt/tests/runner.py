import unittest

import model_searcher

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(model_searcher))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
