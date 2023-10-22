#!/usr/bin/env python3
import argparse
import requests
import sys

parser = argparse.ArgumentParser(description='Update OVH Dynamic IP')
parser.add_argument('--ovhdynid', 
                    help='OVH Id tied to domain', required=True)
parser.add_argument('--ovhdynpass',
                    help='OVH Password tied to domain', required=True)
parser.add_argument('--domain', 
                    help='OVH DynDomain', required=True)

def get_ip():
    try:
        ip_response  = requests.get('https://ident.me')
        ip_response.raise_for_status()
        ip = ip_response.text
        print('IP: '+ip)
        return ip
    except:
        print('Error getting IP')
        sys.exit(1)

def update_domain(ip, id, password, domain):
    try:
        ovh_url = 'https://%s:%s@www.ovh.com/nic/update?system=dyndns&hostname=%s&myip=%s' %  (id, password, domain, ip)
        print(ovh_url)
        update_domain_response = requests.get(ovh_url)
        update_domain_response.raise_for_status()
        print(update_domain_response.text)
    except:
        print('Error updating domain')
        sys.exit(1)

try:
    args       = parser.parse_args()
    ovhdynid   = args.ovhdynid
    ovhdynpass = args.ovhdynpass
    domain     = args.domain   

    ip=get_ip()
    update_domain(ip=ip, id=ovhdynid, password=ovhdynpass, domain=domain)

except:
    exception = sys.exc_info()
    print(exception)
    parser.print_help()
    sys.exit(1)
