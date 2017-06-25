from unittest import TestCase

import proverb

class TestSaying(TestCase):
    def test_is_string(self):
        s = proverb.saying()
        self.assertTrue(isinstance(s, str))
