# Create a holberton file in /tmp with specific permissions

file { '/tmp/holberton':
    ensure  => 'present',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
