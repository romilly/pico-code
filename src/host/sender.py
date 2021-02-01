import serial


class Sender:
    TERMINATOR = '\r'.encode('UTF8')

    def __init__(self):
        self.serial = serial.Serial('/dev/ttyACM0', 9600, timeout=10)

    def send(self, text: str):
        line = '%s\r\f' % text
        self.serial.write(line.encode('utf-8'))
        return self.read_line() # the line will be echoed

    def receive(self) -> str:
        line = self.serial.read_until(self.TERMINATOR)
        return line.decode('UTF8').strip()

    def close(self):
        self.serial.close()

