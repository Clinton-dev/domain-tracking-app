import unittest
from main import check_domain_status


class TestDomainTracking(unittest.TestCase):
    def test_check_domain_status_up(self):
        # Test for a domain that is up and running
        domain_url = "http://barizicommunications.co.ke/"
        result = check_domain_status(domain_url)
        self.assertEqual(result, (domain_url, "Up and running"))

    def test_check_domain_status_down(self):
        # Test for a domain that is down with status code 404
        domain_url = "https://example-down.com"
        result = check_domain_status(domain_url)
        self.assertEqual(result, (domain_url, "Down with status code: 404"))

    def test_check_domain_status_error(self):
        # Test for a domain that raises a requests exception
        domain_url = "https://example-error.com"
        result = check_domain_status(domain_url)
        self.assertEqual(result[0], domain_url)
        self.assertTrue(result[1].startswith("Down with an error:"))


if __name__ == "__main__":
    unittest.main()
