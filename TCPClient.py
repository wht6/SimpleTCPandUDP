from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
# IPv4，套接字是SOCK_STREAM类型，表明它是一个TCP类型的套接字而不是一个UDP类型的套接字
clientSocket.connect((serverName, serverPort))
sentence = str.encode(input("Input lowercase sentence:"))
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print('From server:', bytes.decode(modifiedSentence))
clientSocket.close()
