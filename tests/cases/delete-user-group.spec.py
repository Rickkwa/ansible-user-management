import unittest
import testinfra


class Test(unittest.TestCase):

    def setUp(self):
        self.b = testinfra.get_backend("ansible://containers")
        # Create user and group to be removed

    def test_user_not_exist(self):
        pass

    def test_group_not_exist(self):
        pass


if __name__ == "__main__":
    unittest.main()
