import os
import tempfile
import unittest

from rpchecker.__main__ import _read_urls_from_file
from rpchecker.checker import site_is_online


class CheckerTests(unittest.TestCase):
    def test_site_is_online_returns_boolean_for_a_url(self):
        result = site_is_online("example.com", timeout=1)
        self.assertIsInstance(result, bool)

    def test_read_urls_from_file_returns_urls_from_file(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as handle:
            handle.write("example.com\n")
            temp_path = handle.name

        try:
            self.assertEqual(_read_urls_from_file(temp_path), ["example.com"])
        finally:
            os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()
