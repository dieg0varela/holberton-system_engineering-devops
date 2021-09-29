# Correct setting fo WordPress
file_line {'Correct Setting':
    path  => '/var/www/html/wp-settings.php',
    line  => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
    match =>  '/class-wp-locale.phpp',
}
exec { 'Restart Apache2':
    require => File_line['Correct Setting'],
    command => '/usr/bin/service apache2 restart',
}
