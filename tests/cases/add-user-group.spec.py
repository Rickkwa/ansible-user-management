import unittest
import testinfra


class Test(unittest.TestCase):

    def setUp(self):
        self.b = testinfra.get_backend("ansible://containers")

    def test_user_exists_and_uid(self):
        pass

    def test_group_exists_and_gid(self):
        pass

    def test_user_in_group(self):
        pass

    def test_user_not_in_group(self):
        pass

    def test_group_sudoers_file(self):
        pass


if __name__ == "__main__":
    unittest.main()
