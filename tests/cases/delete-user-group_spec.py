import pytest


def test_user_not_exist(host):
    user1 = host.user("foo")
    user2 = host.user("bar")
    assert not user1.exists
    assert not user2.exists

def test_group_not_exist(host):
    group = host.group("customgroup")
    assert not group.exists
