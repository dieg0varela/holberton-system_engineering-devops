# Create a holberton file in /tmp with specific permissions

package { 'nginx':
    ensure          => 'present',
    provider        => 'apt',
    install_options => ['-y'],
}

file { '/var/www/html/index.html':
    ensure  => 'present',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'Holberton School',
}

file { '/etc/nginx/sites-available/default':
  ensure => 'present',
}->
file_line {'Adding redirect':
    path  => '/etc/nginx/sites-available/default',
    after => 'server_name _;',
    line  =>  '        rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
