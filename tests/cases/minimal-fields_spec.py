import pytest


@pytest.mark.parametrize("user,uid", [
    ("foo", 10001),
    ("bar", 10002),
])
def test_user_exists_and_uid(host, user, uid):
    user = host.user(user)
    assert user.exists
    assert user.uid == uid


def test_group_exists_and_gid(host):
    group = host.group("customgroup")
    assert group.exists
    assert group.gid == 10001


@pytest.mark.parametrize("user", [
    ("foo"),
    ("bar"),
])
def test_users_not_in_group(host, user):
    user = host.user(user)
    assert "customgroup" not in user.groups


def test_group_sudoers_file_not_exists(host):
    file = host.file("/etc/sudoers.d/rel_gid_1")
    assert not file.exists
