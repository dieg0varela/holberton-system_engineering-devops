# Create a holberton file in /tmp with specific permissions

package { 'nginx':
    ensure => present,
}

file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Holberton School',
}

file_line {'Adding_redirect':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    after  => 'server_name _;',
    line   =>  '        rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => File_line['Adding_redirect'],
}
