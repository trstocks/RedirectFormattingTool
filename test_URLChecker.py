import unittest
from URLChecker import URLChecker

class ProtocolTests(unittest.TestCase):
    """Tests for URLChecker validation"""
    def test_PASS_checkProtocol_return_true_for_http(self):
        """does http://google.com have http://"""
        testurl=URLChecker()
        self.assertTrue(testurl.checkProtocol("http://google.com/troy"))
    def test_FAIL_checkProtocol_return_true_for_http(self):
        """does htp://google.com have http:// - accounts for typos"""
        testurl=URLChecker()
        self.assertTrue(testurl.checkProtocol("htp://google.com/troy"),msg="There is a typo in the protocol")
    def test_PASS_checkProtocol_return_true_for_https(self):
        testurl=URLChecker()
        self.assertTrue(testurl.checkProtocol("https://google.com/troy"))
    def test_PASS_checkProtocol_return_true_for_ftp(self):
        testurl=URLChecker()
        self.assertTrue(testurl.checkProtocol("ftp://google.com/troy"))

    def test_PASS_checkProtocol_return_false(self):
        testurl=URLChecker()
        self.assertFalse(testurl.checkProtocol("google.com/troy"))
        self.assertFalse(testurl.checkProtocol("google.com/shortbread"))
class SubdomainTests(unittest.TestCase):
    """Check for Subdomain"""
    def test_PASS_checkSubdomain_returnStringDetectingSubdomain(self):
        testurl = URLChecker()
        self.assertEqual(testurl.checkSubdomain('pope.spacepirate.com/firebritches'),'pope.spacepirate.com/firebritches has a subdomain')
    def test_PASS_checkSubdomain_returnStringNotDetectingSubdomain(self):
        testurl = URLChecker()
        self.assertEqual(testurl.checkSubdomain('spacepirate.com/firebritches'),'There is no subdomain in spacepirate.com/firebritches')



if __name__ == '__main__':
    unittest.main()
