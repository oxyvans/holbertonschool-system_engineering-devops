# task 2

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
