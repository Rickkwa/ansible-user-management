import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


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


def test_sudoer_file_deleted(host):
    file = host.file("/etc/sudoers.d/rel_gid_1")
    assert not file.exists
