from pico_code.host.talker import Talker
import turtle

talker = Talker()
turtle = turtle.Turtle()


def convert(text):
    return (int(text)-200)//300


while True:
    text = talker.receive()
    x,y = [convert(text) for text in  text.split()]
    turtle.setx(x)
    turtle.sety(y)
