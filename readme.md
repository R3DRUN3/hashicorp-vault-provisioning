# HASHICORP VAULT PROVISIONING
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



Spin up Hashicorp Vault with vagrant and Ansible 🔐🔐🔐

<img width="300" alt="Vault Logo" src="https://github.com/hashicorp/vault/blob/f22d202cde2018f9455dec755118a9b84586e082/Vault_PrimaryLogo_Black.png">

## Abstract
[HashiCorp Vault](https://www.vaultproject.io/) is a secrets management tool specifically designed to control access to sensitive credentials in a low-trust environment. 
<br>
It can be used to store sensitive values and, at the same time, dynamically generate access for specific services/applications on lease.

This repo contains scripts to provision your own on-prem Vault test instance via Vagrant and Ansible

## Requirements
`vagrant` `ansible`

## Instructions
Clone this repo and start provisioning:

```console
git clone https://github.com/R3DRUN3/hashicorp-vault-provisioning.git \
&& cd hashicorp-vault-provisioning && sh provisioning.sh
```

Once provisioning is complete retrieve the token from the Ansible output, open your browser to the url `http://192.168.56.12:8200/ui`
and login to the Web UI:
![alt_text](https://github.com/R3DRUN3/hashicorp-vault-provisioning/blob/main/images/vault-login.png)

Once you have logged in, go to `http://192.168.56.12:8200/ui/vault/secrets/kv/show/test-secret`
and verify that the test secret is present:

![alt_text](https://github.com/R3DRUN3/hashicorp-vault-provisioning/blob/main/images/test-secret.png)

Now that your Vault is ready you can freely experiment with this fantastic tool, to test commands via CLI:

Login to the vault host:

```console
vagrant ssh vault
```
authenticate with the vault CLI:

```console
vault login token=INSERT_TOKEN_HERE
```
Retrieve test secret from CLI:
```console
vault kv get kv/test-secret
```

Add a new secret from CLI:
```console
vault kv put kv/new-secret secret-value=IamASecret!
```

This repo also contain a simple python script to demonstrate programmatic  integration with Vault.

export token as an env var:
```console
export VAULT_TOKEN="INSERT_TOKEN_HERE"
```
Move into app folder and install requirements:
```console
cd app && pip3 install -r requirements.txt
```
launch app:
```console
python3 app.py

IS CLITENT AUTHENTICATED ===> True

RETRIEVING SECRET

Value under path test-secret : {'value': 'my_secret_value'}

WRITE A NEW K/V PAIR

DONE
```
