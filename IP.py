# IP
import socket
hostname = socket.gethostname()   
ip_address = socket.gethostbyname(hostname)   
print("IP:", ip_address)
