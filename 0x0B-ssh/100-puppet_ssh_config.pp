# Create a holberton file in /tmp with specific permissions
file_line {'Password Auth conf':
    path  => '/etc/ssh/ssh_config',
    line  => '    PasswordAuthentication no',
    match =>  'PasswordAuthentication yes',
}
file_line {'Add holberton keys':
    path => '/etc/ssh/ssh_config',
    line => '    IdentityFile ~/.ssh/holberton',
}
