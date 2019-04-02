from external import config
from submenus import localscan, portscan


if __name__ == '__main__':
	config.load()
	stop = False
	command = ''
	while not stop:
		all_command = input('>> ').split(' ')

		command = all_command[0]
		args = all_command[1:]

		if command == 'stop':
			stop = True
		elif command == 'localscan':
			print('localscan done.')
			localscan.execute()
		elif command == 'portscan':
			portscan.execute(args)
			print('portscan done.')
		else:
			print('command not found')
