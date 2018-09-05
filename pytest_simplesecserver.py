# first of all import the socket library
import socket               

# next create a socket object
s = socket.socket()         
print ("Socket successfully created")
port = 12344             


# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)     
print ("socket is listening")            

# a forever loop until we interrupt it or 
# an error occurs
while True:
   # Establish connection with client.
   c, addr = s.accept()     
   print ('Got connection from', addr)

   # send a thank you message to the client. 
   c.send('Thank you for connecting')
   # Close the connection with the client
   c.close()    
def encrypt(string, shift):
  shift=2
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
 
def decrypt(string, shift):
  shift=2
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
  
  return cipher
text = input("enter plaintext: ")
#s = int(input("enter shift number: "))
print("original string: ", text)
print("after encryption: ", encrypt(text, 2))
text = input("enter ciphertext: ")
print("your input: ", text)
print("after decryption: ", decrypt(text, 2))

# Close the connection with the client
#c.close()  