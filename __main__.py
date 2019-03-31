import tkinter as tk
from enum import Enum
from socket import socket, AF_INET, SOCK_DGRAM

local_ip = None
target_ip = None
target_ip_type = None


class IpType(Enum):
	local = 'local'
	external = 'external'


def set_local_ip():
	global local_ip
	s = socket(AF_INET, SOCK_DGRAM)
	s.connect(('1.1.1.1', 80))
	local_ip = s.getsockname()[0]
	s.close()


def get_target_ip_validate():
	set_target_ip_from_interface()
	get_target_ip_frame.grid_forget()


def set_target_ip_from_interface():
	global target_ip
	global target_ip_type
	target_ip = get_target_ip_value.get()
	target_ip_type = ip_type_value.get()


def launch():
	global window
	global ip_type_value
	global get_target_ip_value
	global get_target_ip_frame

	window = tk.Tk()
	window.title('PenTool')
	window.geometry('500x400')
	window.resizable(0, 0)

	window.grid_rowconfigure(0, weight=1)
	window.grid_rowconfigure(1, weight=1)
	window.grid_rowconfigure(2, weight=1)
	window.grid_rowconfigure(3, weight=1)
	window.grid_rowconfigure(4, weight=1)
	window.grid_rowconfigure(5, weight=1)
	window.grid_columnconfigure(0, weight=1)
	window.grid_columnconfigure(1, weight=1)
	window.grid_columnconfigure(2, weight=1)

	get_target_ip_frame = tk.Frame(window, width=30, height=100, borderwidth=1)
	get_target_ip_frame.grid(row=2, column=1)

	get_target_ip_label = tk.Label(get_target_ip_frame, text='Ip cible ?', font=('Helvetica', 14))
	get_target_ip_label.pack()

	get_target_ip_value = tk.StringVar()
	get_target_ip_value.set(local_ip)
	get_target_ip_entry = tk.Entry(get_target_ip_frame, textvariable=get_target_ip_value, width=15)
	get_target_ip_entry.pack()

	ip_type_value = tk.StringVar()
	ip_type_value.set(IpType.local)
	ip_type_local_radiobutton = tk.Radiobutton(get_target_ip_frame, text='Locale', variable=ip_type_value, value=IpType.local)
	ip_type_external_radiobutton = tk.Radiobutton(get_target_ip_frame, text='Externe', variable=ip_type_value, value=IpType.external)
	ip_type_local_radiobutton.pack()
	ip_type_external_radiobutton.pack()

	get_target_ip_button = tk.Button(get_target_ip_frame, text='Valider', command=get_target_ip_validate)
	get_target_ip_button.pack()

	window.mainloop()

	print(target_ip_type)
	print(target_ip)


if __name__ == '__main__':
	set_local_ip()
	launch()
