printf "\n[INSTALLING ANSIBLE GALAXY ROLES]\n"
ansible-galaxy install -r requirements.yml
printf "\n[BEGINNING PROVISIONING]\n"
vagrant up