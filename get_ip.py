import socket
def get_ip(self):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        return s.getsockname()[0]
    except:
        return ''
wifi = get_ip('wlan0')