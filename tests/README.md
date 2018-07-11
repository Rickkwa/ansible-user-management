# Adding new tests

## New Remote Environment

If you want to test on a new container containing whatever distro/environment, create a file in `environments/<name>.Dockerfile`. Then in `docker-compose.yml`, add this environment as a new container using a new port. Then simply add the environment into the ansible inventory file, specifying the environment name as the node name, and set the ansible magic variables `ansible_host=127.0.0.1`, `ansible_port=`, `ansible_user=`, `ansible_ssh_pass=`, `ansible_python_interpreter=` as needed.

## New Test Case

Create a new test case file in `cases/<test-name>.yml`. Test cases should follow the following principles:

* Filename should be meaningful, and use dashes (-) to delimit words.
* First line of the test case file should contain a description of the test (as comments).
* The test should not rely on variables defined in the role. Instead, the test should override the variables.
* The test case should be split into 3 parts (with comments in the file indicating each part)
    * **Setup** stage which prepares your variables, and/or environment
    * **Run** stage which imports and runs the role
    * **Verification** stage which checks the changes were made correctly

After creating the test case file under `cases/`, the travis ci should automatically pick up the test case and run it against all environments.
