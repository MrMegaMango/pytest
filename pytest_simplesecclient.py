# echo_client.py
#import socket

#host = socket.gethostname()    
#port = 12345                   # The same port as used by the server
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))
#s.sendall(b'Hello, world')
#data = s.recv(1024)
#s.close()
#print('Received', repr(data))
# Import socket module
import socket               

# Create a socket object
s = socket.socket()         

# Define the port on which you want to connect
port = 12345                

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
print (s.recv(1024))
# close the connection
s.close()       