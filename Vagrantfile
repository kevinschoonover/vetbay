# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "bento/ubuntu-16.04"


  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder ".", "/vagrant"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"
  config.vm.network "private_network", type: "dhcp"

  config.vm.provider "libvirt" do |lv, override|
      override.vm.box = "generic/ubuntu1604"
      # override.vm.synced_folder ".", "/vagrant", type: '9p', disabled: false, accessmode: "mapped", mount: true
  end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  $updates = <<-UPDATE
    apt-get update
    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    apt-get install build-essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info postgresql nodejs -y
    pip3 install --upgrade pip
    cd /vagrant/saleor/
    npm install
    npm run build-assets
    npm run build-emails
  UPDATE

  $db = <<-DB
    sudo -u postgres psql -c "create database saleor"
    sudo -u postgres psql -c "create user saleor with password 'saleor'"
    sudo -u postgres psql -c "ALTER USER saleor WITH SUPERUSER"
    sudo -u postgres psql -c "grant all privileges on database saleor to saleor"
    sudo -u postgres psql -c "alter user saleor createdb"
  DB

  $migrate = <<-MIGRATE
    cd /vagrant/saleor/
    pip3 install -r requirements.txt
    python3 manage.py makemigrations --noinput
    python3 manage.py collectstatic --noinput
    python3 manage.py migrate
  MIGRATE

  $setup = <<-SETUP
    SECRET_KEY='test' tmux new-session -d -s django 'cd /vagrant/saleor && python3 manage.py runserver 0.0.0.0:8000'
    tmux detach -s django
  SETUP

  config.vm.provision :shell, inline: $updates
  config.vm.provision :shell, inline: $db
  config.vm.provision :shell, inline: $migrate
  config.vm.provision :shell, inline: $setup
end
