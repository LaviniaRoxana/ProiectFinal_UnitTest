import unittest
import test_linkuri
import test_login
import test_forgot_password
import test_geolocation


def suite():

    # inregistreaza toate testele intr-o suita
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_linkuri.TestLinkuri))
    test_suite.addTest(unittest.makeSuite(test_login.TestLogin))
    test_suite.addTest(unittest.makeSuite(test_forgot_password.TestForgotPassword))
    test_suite.addTest(unittest.makeSuite(test_geolocation.TestGeolocation))

    return test_suite


mySuit = suite()

runner = unittest.TextTestRunner()
runner.run(mySuit)
