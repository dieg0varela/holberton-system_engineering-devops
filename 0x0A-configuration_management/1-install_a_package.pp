# Install puppet-lint

package { 'puppet-lint':
    ensure          => 'present',
    provider        => 'gem',
    install_options => ['-v 2.1.1'],
}
