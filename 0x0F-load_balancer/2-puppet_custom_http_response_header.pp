#puppilete

exec { 'update':
  command => 'sudo apt-get update',
  path    => ['/usr/bin', '/bin'],
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

exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File_line['Header'],
}`
