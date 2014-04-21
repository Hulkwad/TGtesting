import socket
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((irc.freenode.net, 6667))

irc.recv (4096)
irc.send ('NICK Botwad \r\n')
irc.send ('USER Botwad Botwad Botwad :Botwad \r\n')
irc.send ('JOIN #Testwad')
irc.send ('PRIVMSG #Testwad :Jawad er så jævla best!! <33')

