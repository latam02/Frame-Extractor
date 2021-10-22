Vagrant.configure("2") do |config|
  config.vm.box ="ubuntu/bionic64"
  config.vm.boot_timeout = 1200
  config.vm.provider "virtualbox" do |vb|
    vb.memory ="2048"
  end 

  # Configure provisioners on the machine
  config.vm.provision :docker
  config.vm.provision :docker_compose

  config.vm.define "server-1" do |server1| 
    server1.vm.network "private_network", ip: '192.168.33.67'
    server1.vm.hostname = "server-1"
  end
end