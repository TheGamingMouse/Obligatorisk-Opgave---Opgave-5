from socket import *
import json
IPv4 = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((IPv4, serverPort))

while True:
 modifiedSentence = clientSocket.recv(1024)
 print('From server: ', modifiedSentence.decode())
 userInput = input('Message from Client: ')
 sentence = userInput.lower()
 if sentence.split(' ')[0] == 'calculator':
  dictCalc = {
   'func' : sentence.split(' ')[0],
   'calc' : sentence.split(' ')[1],
   'num1' : sentence.split(' ')[2],
   'num2' : sentence.split(' ')[3]
  }
  dictSent = json.dumps(dictCalc)
  #print('Dumped dictCalc')
 elif sentence.split(' ')[0] == 'random':
  dictRand = {
   'func' : sentence.split(' ')[0],
   'num1' : sentence.split(' ')[1],
   'num2' : sentence.split(' ')[2]
  }
  dictSent = json.dumps(dictRand)
  #print('Dumped dictRand')
 clientSocket.send(dictSent.encode())
 #print('Sent dictSent')
 modifiedSentence = clientSocket.recv(1024)
 print('From Server: ', modifiedSentence.decode())