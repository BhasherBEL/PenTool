import json
import os
import netifaces
from socket import socket, AF_INET, SOCK_DGRAM

config_path = 'configs/config.json'

default_ip = ''
distant_neutral_server = ''
gateway_ip = ''
local_ip = ''


def set_local_ip():
	global local_ip
	s = socket(AF_INET, SOCK_DGRAM)
	s.connect((gateway_ip, 80))
	local_ip = s.getsockname()[0]
	s.close()


def set_default_ip(value):
	global default_ip
	if value.lower() == 'router':
		default_ip = gateway_ip
	elif value.lower() == 'this':
		default_ip = local_ip
	else:
		default_ip = value


def load():
	global distant_neutral_server
	global gateway_ip

	gateway_ip = netifaces.gateways()['default'][2][0]
	set_local_ip()

	if os.path.exists(config_path) and os.path.isfile(config_path):
		try:
			with open(config_path, 'r') as file:
				config_data = json.load(file)
				set_default_ip(config_data['default_ip'])
				distant_neutral_server = config_data['distant_neutral_server']
		except (ValueError, json.JSONDecodeError) as e:
			print(e)
	else:
		raise FileNotFoundError('the {0} file does not exist.'.format(config_path))
