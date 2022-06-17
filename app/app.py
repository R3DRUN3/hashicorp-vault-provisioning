import os
import hvac 

SECRETS_PATH = 'test-secret'
vault = hvac.Client(
    url='http://192.168.56.12:8200',
    token=os.environ['VAULT_TOKEN']) 
print(f"IS CLITENT AUTHENTICATED ===> {vault.is_authenticated()}\n")
print("RETRIEVING SECRET\n")
read_response = vault.secrets.kv.v2.read_secret_version(mount_point='kv', path=SECRETS_PATH)
print(f"Value under path {SECRETS_PATH} : {read_response['data']['data']}\n")

print("WRITE A NEW K/V PAIR\n")
# Write a new k/v pair
create_response = vault.secrets.kv.v2.create_or_update_secret(
      mount_point='kv',
      path=SECRETS_PATH+'-new',
      secret=dict(value='my_secret_value'),
)
print('DONE')
