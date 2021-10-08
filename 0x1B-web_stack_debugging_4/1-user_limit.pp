# Increase the limit of file descriptors per user
exec {'Correct Hard':
    command => "/bin/sed -i 's/5/1000/g' /etc/security/limits.conf",
}
exec { 'Correct Soft':
    require => Exec['Correct Hard'],
    command => "/bin/sed -i 's/4/1000/g' /etc/security/limits.conf",
}
