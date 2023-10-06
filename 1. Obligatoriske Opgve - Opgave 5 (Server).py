from socket import *
import threading
import random
import json
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def handleClient(connectionSocket, addr):
 connectionSocket.send('To use the "Calculator" function, format your input like so: "Calculator method num1 num2" The method can be "add, subtract, multiply, or divide". To use the "Random" function, format your input like so: "Random num1 num2" A random number between the two you sent, will then be generated.'.encode())
 dictJson = json.loads(connectionSocket.recv(1024).decode().lower())
 #print('Data recieved')
 
 if dictJson['func'] == 'random':
  print('Client function: Random')
  numRand = random.randrange(int(dictJson['num1']),int(dictJson['num2']))
  num = str(f'Your random number between {dictJson["num1"]} and {dictJson["num2"]} is: {numRand}.')
  print(f'Client random number is: {numRand}')

  connectionSocket.send(num.encode())
  handleClose(connectionSocket, addr)
 
 elif dictJson['func'] == 'calculator':
  print('Client function: Calculator')
  txtCalc = f' '
  
  if dictJson['calc'] == 'add':
   txtCalc = f'The addition of {dictJson["num1"]} + {dictJson["num2"]} = {int(dictJson["num1"]) + int(dictJson["num2"])}'
   print(txtCalc)
  
  elif dictJson['calc'] == 'subtract':
   txtCalc = f'The subtraction of {dictJson["num1"]} - {dictJson["num2"]} = {int(dictJson["num1"]) - int(dictJson["num2"])}'
   print(txtCalc)
  
  elif dictJson['calc'] == 'multiply':
   txtCalc = f'The multiplication of {dictJson["num1"]} * {dictJson["num2"]} = {int(dictJson["num1"]) * int(dictJson["num2"])}'
   print(txtCalc)
  
  elif dictJson['calc'] == 'divide':
   txtCalc = f'The divition of {dictJson["num1"]} / {dictJson["num2"]} = {int(dictJson["num1"]) / int(dictJson["num2"])}'
   print(txtCalc)
  
  connectionSocket.send(txtCalc.encode())
  handleClose(connectionSocket, addr)
 

def handleClose(connectionSocket, addr):
 connectionSocket.send('Connection ended'.encode())
 connectionSocket.close()
 print('Connection closed for client: ', addr)


print('The server is ready to receive')
while True:
 connectionSocket, addr = serverSocket.accept()
 print('Connection from client, address:',addr)
 threading.Thread(target=handleClient,args=(connectionSocket,addr)).start()
