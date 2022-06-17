VAGRANT_API_VERSION=2

Vagrant.configure(VAGRANT_API_VERSION) do |config|
  

  config.vm.box = "ubuntu/focal64"
  config.vm.define "vault"
  config.ssh.insert_key = false
  config.vm.network "private_network", ip: "192.168.56.12"

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 1
  end

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "vault_provisioning.yml"
  end
end