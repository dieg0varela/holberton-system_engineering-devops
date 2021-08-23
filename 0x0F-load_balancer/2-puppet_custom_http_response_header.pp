# Create a holberton file in /tmp with specific permissions

package { 'nginx':
    ensure => present,
}

file_line {'Adding_Header':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    after  => 'location / {',
    line   =>  '               add_header X-Served-By ${HOSTNAME};\n;',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => File_line['Adding_Header'],
}
