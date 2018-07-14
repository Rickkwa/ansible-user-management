# Adding new tests

## New Remote Environment

If you want to test on a new container containing whatever distro/environment, create a file in `environments/<name>.Dockerfile`.

* The image should have python installed.
* The image should run ssh port 22.
* Base image should *not* use the `latest` tag.
* You can set the user and password as you wish, and use ansible's `ansible_user` and `ansible_ssh_pass` variable.

Then in `docker-compose.yml`, add this environment as a new container using a new port. Then simply add the environment into the ansible inventory file, specifying the environment name as the node name, and set the ansible variables `ansible_host=127.0.0.1`, `ansible_port=`, `ansible_user=`, `ansible_ssh_pass=`, `ansible_python_interpreter=` as needed.

## New Test Case

Test cases consists of 2 components.

1. Ansible playbook to prepare and execute the role.
2. Pytest file to verify the state of the container after running the role.

### Ansible playbook test

Create a new test case file in `cases/<test-name>.yml`. The test case should follow the following principles:

* Filename should be meaningful to the test, using dashes (-) to delimit words.
* The playbook should have some comments at the top to describe the test.
* Use `pre_tasks` to do any setup for the test, and use `tasks` to actually execute the role.
* The test should not rely on variables defined in the role. Instead, the test should override the variables.

### Verification using Pytest

Create a new test case spec file in `cases/<test-name>_spec.py`. The `<test-name>` should match the one for the corresponding ansible playbook file so that the CI can associate the two. Make use of the `pytest` testing framework with the `testinfra` plugin to write your verification.

After creating the test case files under `tests/cases/`, the travis ci should automatically pick up the test case and run it against all environments.
