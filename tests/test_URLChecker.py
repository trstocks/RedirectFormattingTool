import unittest
from package.URLChecker import URLChecker

class ProtocolTests(unittest.TestCase):
    """Tests for URLChecker validation"""
    def test_checkProtocol_return_true_for_http(self):
        """does http://google.com have http://"""
        testurl=URLChecker('http://google.com/troy')
        self.assertTrue(testurl.checkProtocol())
        self.assertTrue(testurl.checkProtocol(),msg="There is a typo in the protocol")
    def test_checkProtocol_return_true_for_https(self):
        testurl=URLChecker('https://google.com/troy')
        self.assertTrue(testurl.checkProtocol())
    def test_checkProtocol_return_true_for_ftp(self):
        testurl=URLChecker('ftp://google.com/troy')
        self.assertTrue(testurl.checkProtocol())

    def test_checkProtocol_return_false(self):
        testurl=URLChecker('google.com/troy')
        testurl2=URLChecker('google.com/shortbread')
        self.assertFalse(testurl.checkProtocol())
        self.assertFalse(testurl2.checkProtocol())

class SubdomainTests(unittest.TestCase):
    """Check for Subdomain"""
    def test_checkSubdomain_returnStringDetectingSubdomain(self):
        testurl = URLChecker('pope.spacepirate.com/firebritches')
        self.assertEqual(testurl.checkSubdomain(),'pope.spacepirate.com/firebritches has a subdomain')
    def test_checkSubdomain_returnStringNotDetectingSubdomain(self):
        testurl = URLChecker('spacepirate.com/firebritches')
        self.assertEqual(testurl.checkSubdomain(),'There is no subdomain in spacepirate.com/firebritches')
    def test_checkPath_returnPath(self):
        testurl = URLChecker('google.com/troy')
        self.assertEqual(testurl.checkPath(),'troy')


if __name__ == '__main__':
    unittest.main()
