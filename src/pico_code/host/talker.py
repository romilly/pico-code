import serial


class Talker:
    TERMINATOR = '\r'.encode('UTF8')

    def __init__(self, timeout=-1):
        """
        Initialise Talker instance


        :param timeout:
        """
        self.serial = serial.Serial('/dev/ttyACM0', 115200, timeout=timeout)

    def send(self, text: str):
        line = '%s\r\f' % text
        self.serial.write(line.encode('utf-8'))
        return self.receive() == text # the line should be echoed, so the result should match

    def receive(self) -> str:
        line = self.serial.read_until(self.TERMINATOR)
        return line.decode('UTF8').strip()

    def close(self):
        self.serial.close()

