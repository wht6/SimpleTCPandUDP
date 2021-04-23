from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
# AF_INET指示了底层网络使用IPv4，第二个参数指示了套接字是SOCK_DGRAM类型的，这意味着它是一个UDP套接字而不是一个TCP套接字
message = str.encode(input('Input lowercase sentence:'))
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(bytes.decode(modifiedMessage))
clientSocket.close()
