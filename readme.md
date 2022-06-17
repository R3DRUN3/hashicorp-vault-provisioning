# HASHICORP VAULT PROVISIONING

## Abstract
HashiCorp Vault is a secrets management tool specifically designed to control access to sensitive credentials in a low-trust environment. 
<br>
It can be used to store sensitive values and at the same time dynamically generate access for specific services/applications on lease.

This repo contains scripts to start your own on-prem vault test instance via Vagrant and Ansible

Once you have logged in, go to `http://192.168.56.12:8200/ui/vault/secrets/kv/show/test-secret`
and verify that your test secret is present:


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

This repo also contain a simple python script to demonstrate programmatical integration with Vault.

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
```