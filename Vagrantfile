# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.



Vagrant.configure(2) do |config|
  config.vm.define :geonode1 do |geonode1|
    geonode1.vm.box = "puppetlabs/ubuntu-14.04-64-puppet"

    geonode1.vm.network "forwarded_port", guest: 80, host: 18888
    geonode1.vm.network "forwarded_port", guest: 8000, host: 18000
    geonode1.vm.network "forwarded_port", guest: 8080, host: 18080
    geonode1.vm.network "forwarded_port", guest: 5432, host: 15432
    geonode1.vm.network "private_network", ip: "192.168.33.101"

    geonode1.vm.synced_folder "geonode", "/install"


    geonode1.vm.provision "shell", path: "automation.sh", privileged: false, :args => "geonode1.vag"

    geonode1.vm.provider "virtualbox" do |vb|
      vb.memory = "3192"
      vb.cpus = 2
    end
  end

  config.vm.define :geonode2 do |geonode2|
    geonode2.vm.box = "puppetlabs/ubuntu-14.04-64-puppet"

    geonode2.vm.network "forwarded_port", guest: 80, host: 28888
    geonode2.vm.network "forwarded_port", guest: 8000, host: 28000
    geonode2.vm.network "forwarded_port", guest: 8080, host: 28080
    geonode2.vm.network "forwarded_port", guest: 5432, host: 25432
    geonode2.vm.network "private_network", ip: "192.168.33.102"

    geonode2.vm.synced_folder "geonode", "/install"


    geonode2.vm.provision "shell", path: "automation.sh", privileged: false, :args => "geonode2.vag"

    geonode2.vm.provider "virtualbox" do |vb|
      vb.memory = "3192"
      vb.cpus = 2
    end
  end

  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  #config.vm.box = "puppetlabs/ubuntu-14.04-64-puppet"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  #config.vm.network "forwarded_port", guest: 80, host: 18888
  #config.vm.network "forwarded_port", guest: 8000, host: 18000
  #config.vm.network "forwarded_port", guest: 8080, host: 18080
  #config.vm.network "forwarded_port", guest: 5432, host: 15432

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  #config.vm.network "private_network", ip: "192.168.33.101"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  #config.vm.synced_folder "geonode", "/install"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  #config.vm.provision "shell", path: "automation.sh", privileged: false
end
