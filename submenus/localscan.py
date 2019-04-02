from external import config
import nmap
import xmltodict


def execute():

	base = '.'.join(config.local_ip.split('.')[:-1]) + '.'

	nmap_scanner = nmap.PortScanner()

	nmap_scanner.scan(hosts=base + '0/24', arguments='-n -sP -PE -PA21,23,80,3389')

	xml_output = xmltodict.parse(nmap_scanner.get_nmap_last_output())

	for host in xml_output['nmaprun']['host']:
		print(host['address']['@addrtype'] + ': ' + host['address']['@addr'])
