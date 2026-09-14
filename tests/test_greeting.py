import unittest

from greeting import greet


class GreetingTests(unittest.TestCase):
    def test_name(self):
        self.assertEqual(greet("Git"), "Hello, Git!")

    def test_empty_name(self):
        self.assertEqual(greet("  "), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
