import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("Name", [
    ("sonar"),
])
def test_service(Service, Name):
    assert Service(Name).is_enabled
    assert Service(Name).is_running
