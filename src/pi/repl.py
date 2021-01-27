from sender import Sender

sender = Sender()
sender.send_line('2 + 2')
print(sender.read_line())
sender.close()
