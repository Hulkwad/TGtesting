import socket
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#-------------------------------------------------------------

nick = "Botwad"
homechan = "#Testwad"
network = irc.freenode.net
irc.connect((network, 6777))

#------------------------------------------------------------------

print irc.recv (4096)
irc.send ( 'NICK Botwad'\r\n)
irc.send ( 'USER Botwad Botwad Botwad :Botwad botten \r\n')
irc.send ( 'JOIN #Testwad' \r\n)
irc.send ('PRIVMSG #Testwad :Jeg elsker internett!\r\n')

#------------------------------------------------------------------



while True:
    data = irc.recv (4096)
    print ("FUCK YEAH!!!"):
