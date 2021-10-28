#!/usr/bin/env python3

import sys
import os
import requests

ovhid     = 'your_nic_given_by_ovh'
pass      = 'your_ovh_password'
dyndomain = 'your_domain_to_update'

#get your public ip address
ipReq  = requests.get('https://ident.me')
ip = ipReq.text

#update ovh 
req = 'https://'+ovhid+':'+pass+'@www.ovh.com/nic/update?system=dyndns&hostname='+dyndomain+'&myip='
os.system('wget -q "' +req+ip +'" -O /dev/null')
