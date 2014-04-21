import socket
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect(("irc.freenode.net", 6667))

print (irc.recv(4096))
irc.send(b'NICK Botwad\r\n')
irc.send(b'USER wad wad wad : wad\r\n')
irc.send(b'JOIN #testwad\r\n')

#irc.send(b'PRIVMSG #wad : TEST\r\n')
#irc.send(b':wad PRIVMSG PewZ :NIGGA\r\n')
#irc.send(b'QUIT : I QUIT!\r\n')

while True:
    data = irc.recv(4096)
    print (data)
    #if data.find(b"PRIVMSG jawad :ping"):
    #    irc.send(b"PRIVMSG PewZ :pong\r\n")
    #if data.find(b'slaps wad') != -1:
    #   irc.send(b'''PRIVMSG #wad :Please don't slap me!\r\n''')
