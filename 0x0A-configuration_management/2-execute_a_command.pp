# Exec kill command

exec { 'pkill':
    command => '/usr/bin/pkill -15 killmenow',
}
