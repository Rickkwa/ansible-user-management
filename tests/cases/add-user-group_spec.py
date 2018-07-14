import pytest


def test_user_exists_and_uid(host):
    user1 = host.user("foo")
    user2 = host.user("bar")
    assert user1.exists
    assert user2.exists
    assert user1.uid == 10001
    assert user2.uid == 10002

def test_group_exists_and_gid(host):
    group = host.group("customgroup")
    assert group.exists
    assert group.gid == 10001

def test_user1_in_group(host):
    user = host.user("foo")
    assert "customgroup" in user.groups

def test_user2_not_in_group(host):
    user = host.user("bar")
    assert "customgroup" not in user.groups

def test_group_sudoers_file(host):
    file = host.file("/etc/sudoers.d/rel_gid_10001")
    assert file.exists and file.is_file
    assert file.mode == 0o440