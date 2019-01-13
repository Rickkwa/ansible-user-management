import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


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


def test_user1_in_group(host):
    user = host.user("foo")
    assert "customgroup" in user.groups


def test_user2_not_in_group(host):
    user = host.user("bar")
    assert "customgroup" not in user.groups


def test_group_sudoers_file(host):
    file = host.file("/etc/sudoers.d/rel_gid_1")
    assert file.exists and file.is_file
    assert file.mode == 0o440


@pytest.mark.parametrize("user", [
    "foo",
    "bar"
])
def test_authorized_keys(host, user):
    file = host.file("/home/{0}/.ssh/authorized_keys".format(user))
    assert file.exists and file.is_file
    assert file.size > 0
