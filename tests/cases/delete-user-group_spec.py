import pytest


@pytest.mark.parametrize("user", [
    ("foo"),
    ("bar"),
])
def test_user_not_exist(host, user):
    user = host.user(user)
    assert not user.exists


def test_group_not_exist(host):
    group = host.group("customgroup")
    assert not group.exists
