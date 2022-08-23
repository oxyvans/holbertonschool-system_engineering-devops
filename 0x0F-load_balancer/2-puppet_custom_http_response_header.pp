#puppilete

exec { 'update':
  command => 'sudo apt-get update',
}

package { 'nginx':
    ensure   => installed,
    require => exec['update'],
}

file_line { 'Header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
