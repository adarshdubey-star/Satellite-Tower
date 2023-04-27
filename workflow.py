import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fqdn = 'https://dhcp-X-A.redhat.com' # AAP url
response = requests.get(f'{fqdn}/api/v2/hosts',verify=False,auth=HTTPBasicAuth('username', 'password'))
result = json.dumps(response.json(),indent=2)
print(result)



