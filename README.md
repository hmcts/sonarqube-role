devops.sonarqube
=========

Install Sonarqube

Requirements
------------

This role was built for RedHat systems like RHEL 7, Centos 7.

Role Variables
--------------

Dependencies
------------

Sonarqube needs Java 

ansible-galaxy install -p roles devops.java

Example Playbook
----------------

Example of how to use this role:

    - hosts: soonarqube
      roles:
         - { role: devops.sonarqube }

License
-------

BSD,MIT

Author Information
------------------
HMCTS Reform
