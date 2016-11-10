#!usr/bin/env python3

import sys
import argparse
import requests
import json

host_ip = ""
host_port = '8080'
head = {"Content-Type": "text/plain"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--request", type = str,
                        required = True,
                        help = "Request type (GET, PUT, POST)")
    parser.add_argument("-i", "--item", type = str,
                        required = True,
                        help = "Item to be dealt with")
    parser.add_argument("-ip", "--ip_addr", type = str,
                        required = True,
                        help = "IP address of server Pi")
    parser.add_argument("-p", "--port", type = str,
                        required = True,
                        help = "Port to listen in on")
    parser.add_argument("-d", "--data", type = str,
                        required = False,
                        help = "ON or OFF")

    args = parser.parse_args()

    host_ip = args.ip_addr
    host_port = args.port
    key = args.item
    request = args.request

    data = None

    if args.data:
        data = args.data

    if request == 'GET':
        url = 'http://%s:%s/rest/items/%s/state'%(host_ip, host_port, key)

        try:
                req = requests.get(url)

                print(req.content.decode('UTF-8'))
                        
        except:
                print('Error ', sys.exc_info()[0])

    elif request == 'PUT':
        url = 'http://%s:%s/rest/items/%s/state'%(host_ip, host_port, key)
        req = requests.put(url, data = data, headers = head)

        if req.status_code != requests.codes.ok:
            req.raise_for_status()

    elif request == 'POST':
        url = 'http://%s:%s/rest/items/%s'%(host_ip, host_port, key)
        req = requests.post(url, data = data, headers = head)

        if req.status_code != requests.codes.ok:
            req.raise_for_status()
