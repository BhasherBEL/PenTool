import nmap


def execute(args):

	nmap_scanner = nmap.PortScanner()
	nmap_scanner.scan(' '.join(args), arguments='-p 22-443 -sV')

	for host in nmap_scanner.all_hosts():
		print('----------------------------------------------------')
		print('Host : %s (%s)' % (host, nmap_scanner[host].hostname()))
		print('State : %s' % nmap_scanner[host].state())
		for proto in nmap_scanner[host].all_protocols():
			print('----------')
			print('Protocol : %s' % proto)

			l_port = list(nmap_scanner[host][proto].keys())
			l_port.sort()
			for port in l_port:
				info = nmap_scanner[host][proto][port]

				service = info['name']

				if service == '':
					service = 'unknown'

				spacing = ' '*(15-len(service))

				extra = []
				if info['product'] != '':
					extra.append('product: {0}'.format(info['product']))
				if info['version'] != '':
					extra.append('version: {0}'.format(info['version']))
				if info['extrainfo'] != '':
					extra.append('extra: {0}'.format(info['extrainfo']))
				if info['cpe'] != '':
					extra.append('cpe: {0}'.format(info['cpe']))
				if len(extra) == 0:
					extra.append('None')
				print('port: {0}\t state: {1}\t service: {2}{3} extra-info: ({4})'.format(port, info['state'], service, spacing, ', '.join(extra)))

