from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = ('smtp.gmail.com', 465) #Fill in start #Fill in end


# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.connect(mailserver)

#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


#LOGGING IN
clientSocket.send('AUTH LOGIN \r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print ("After AUTH LOGIN:" + recv1)

username = "cs148test@gmail.com"
base64Str = username.encode()
base64Str = base64.b64encode(base64Str)
clientSocket.send(base64Str + '\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print ("After USERNAME INPUT:" + recv1)


password = "ilikechicken1234"
base64Str = password.encode()
base64Str = base64.b64encode(base64Str)
clientSocket.send(base64Str + '\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print ("After PASSWORD INPUT:" + recv1)



# Send MAIL FROM command and print server response.

# Fill in start
mailFrom = "MAIL FROM:<cs148test@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv1 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: " +recv1)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start

rcptTo = "RCPT TO:<cs148test@gmail.com>\r\n"
clientSocket.send(rcptTo.encode())
recv1 = clientSocket.recv(1024).decode()
print("After RCTP TO:" + recv1)

#Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send('DATA\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end


# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send('QUIT\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
clientSocket.close()

# Fill in end
