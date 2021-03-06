node default {
  notice("The host ${hostname} has no node entry")
}

# FIXME: put this somewhere else
class apt_update {
  exec { "do_apt_update":
    command     => "/usr/bin/apt-get update",
    timeout     => 300,
  }
  package { 'apt-transport-https':
    ensure => installed
  }
}

node "hdo-bot-service" {
  # Run apt update before everything else
  stage { "init": before  => Stage["main"] }
  class { "apt_update":
    stage => init
  }

  include apt
  include timezone


  class { 'unattended_upgrades':
    origins => ['${distro_id}:${distro_codename}',
                '${distro_id}:${distro_codename}-security',
                '${distro_id}:${distro_codename}-updates',
                '${distro_id}:${distro_codename}-proposed']
  }

  include bot_service

  bot_service::app { 'bot_service':
    domain => 'snakk.holderdeord.no'
  }

  bot_service::app { 'bot_service_dev':
    domain          => 'snakk-dev.nkweb.no',
    gunicorn_port   => 8001,
    app_environment => 'development',
    app_user        => 'botappdev',
    git_branch      => 'develop'
  }
}