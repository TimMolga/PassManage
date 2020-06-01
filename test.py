import unittest
import test_password_generator
import test_password_retrieval

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_password_generator))
suite.addTests(loader.loadTestsFromModule(test_password_retrieval))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)