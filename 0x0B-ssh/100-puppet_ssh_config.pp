#!/usr/bin/env bash
#Making changes to our configuration file.

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    #SSH client configuration
    host
        HostName 100.25.111.181
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
   "
}
