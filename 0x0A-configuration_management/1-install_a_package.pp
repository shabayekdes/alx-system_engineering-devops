# 1-install_a_package.pp

class { 'python':
  version => 'system',
}

package { 'python3-pip':
  ensure => installed,
}

package { 'build-essential':
  ensure => installed,
}

package { 'libssl-dev':
  ensure => installed,
}

package { 'libffi-dev':
  ensure => installed,
}

package { 'python3-dev':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install --user flask==2.1.0',
  path    => ['/bin', '/usr/bin'],
  unless  => '/usr/bin/flask --version | grep "Flask 2.1.0"',
  require => Package['python3-pip'],
}
