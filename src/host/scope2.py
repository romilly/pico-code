from guizero import App, Drawing
from sender import Sender

s = Sender()

def plot(data, drawing):
	drawing.clear()
	for i in range(len(data)-1):
		drawing.line(i,data[i],i+1, data[i+1])
		
def convert(text):
	value = int(text)/65536.0
	return int(100-value*50)
		
def progress(drawing):
	global values
	values = values[1:]+[convert(s.receive())]
	drawing.clear()
	plot(values, drawing)
		
app = App()
drawing = Drawing(app)
drawing.repeat(5, progress, [drawing])
values = 100*[0]
app.display()


	
		
		
	
