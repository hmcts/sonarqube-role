import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("Name", [
    ("sonar"),
])
def test_package(Package, Name):
    assert Package(Name).is_installed
