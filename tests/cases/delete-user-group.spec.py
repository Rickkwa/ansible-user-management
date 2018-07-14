import unittest
import testinfra


class Test(unittest.TestCase):

    def setUp(self):
        self.b = testinfra.get_backend("ansible://containers")

    def test_user_not_exist(self):
        user1 = self.host.user("foo")
        user2 = self.host.user("bar")
        assert not user1.exists
        assert not user2.exists

    def test_group_not_exist(self):
        group = self.host.group("customgroup")
        assert not group.exists


if __name__ == "__main__":
    unittest.main()
