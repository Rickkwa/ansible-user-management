Ansible User Management Role
====

[![Build Status](https://travis-ci.com/Rickkwa/ansible-user-mgmt.svg?branch=master)](https://travis-ci.com/Rickkwa/ansible-user-mgmt)

Manages user accounts, groups, and sudoers using a centralized user/group inventory.

The role takes on a centralized and flat approach as it contains all user and group information in one place, as opposed to overriding the user/group inventory on a per host/group basis. When you have to use host_vars/group_vars to give users different access to different systems, there can be some uncertainty if a host belongs to multiple host groups with conflicting user/group inventories. When that happens, it's basically up to Ansible to choose which group has priority. But with the flat and centralized approach that this role uses, you can define exactly which host groups you expect the user/group to be in, and which host groups they should not be in.

Requirements
----

* Ansible 2.5+.

User and Group Inventory Variables
----

## User

The user inventory is a list containing the details of each user. This list is stored in `vars/users.yml`, and each item of the list is a dict that has the following fields:

|Field|Required|Type|Default|Description|
|---|---|---|---|---|
|name|yes|string|undefined|User's login name.|
|rel_uid|yes|int|undefined|Relative UID in this inventory list. The group's UID would be `rel_uid + um_uid_base`.|
|present|no|list[str]|`['all']`|List of ansible defined host groups containing the hosts that the user should be on.|
|absent|no|list[str]|`[]`|List of host groups containing the hosts that the user should not be on. This setting takes precedence over `present`.|
|passwd|yes|string|undefined|Hashed password for account. See this [ansible doc](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-crypted-passwords-for-the-user-module) on how you should generate the hashed password.|
|authorized_keys|no|string/list[str]|omit|A single pubkey or list of pubkeys to include in the user's authorized_keys file.|
|groups|no|list[str]|omit|A list of groups that the user should belong in.|

## Group

The gorup inventory is a list containing the details of each gorup. This list is stored in `vars/groups.yml`, and each item of the list is a dict that has the following fields:

|Field|Required|Type|Default|Description|
|---|---|---|---|---|
|name|yes|string|undefined|Group name.|
|rel_gid|yes|int|undefined|Relative GID in this inventory list. The group's GID would be `rel_gid + um_gid_base`.|
|present|no|list[str]|`['all']`|List of ansible defined host groups containing the hosts that the group should be on.|
|absent|no|list[str]|`[]`|List of host groups containing the hosts that the group should not be on. This setting takes precedence over `present`.|
|sudoer|no|string|omit|File content for the sudoer file associated with this group.|
