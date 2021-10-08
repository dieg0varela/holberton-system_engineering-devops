# Change the limit of file descriptor nginx can handle
exec {'Correct Setting':
    command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx",
}
exec { 'Restart Nginx':
    require => Exec['Correct Setting'],
    command => '/usr/bin/service nginx restart',
}
