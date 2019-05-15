import socket

def get_ip(name):
    return socket.gethostbyname(name)

name = "google.co.in"
print("google.co.in/" + get_ip(name))