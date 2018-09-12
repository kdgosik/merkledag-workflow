from unittest import TestCase

import merkledag

class TestHashFile(TestCase):
    def test_is_string(self):
        s = merkledag.hash_file('test.txt')
