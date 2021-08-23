# Create a holberton file in /tmp with specific permissions

package { 'nginx':
    ensure => present,
}

file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Holberton School',
}

file { '/var/www/html/404.html':
    ensure  => present,
    content => "Ceci n'est pas une page",
}

file_line {'Adding_redirect':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    after  => 'server_name _;',
    line   =>  '        rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file_line {'Adding_404':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    after  => 'location / {',
    line   =>  '        error_page 404 /404.html;\n;',
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
  subscribe  => File_line['Adding_redirect','Adding_404', 'Adding_Header'],
}
