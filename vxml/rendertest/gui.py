from tkinter import Canvas, Frame

class Application(Frame):
  controls = []
  offest = 8
  def __init__(self, width, height):
    self.width = width
    self.height = height
    Frame.__init__(self, None)
    self.pack()
    self.createCanvas()

  def createCanvas(self):
    self.canvas = Canvas(self, bg="white", width=500, height=500)
    self.canvas.pack()

  def register(self, control):
    self.controls.append(control)
  
  def draw(self):
    self.canvas.delete('all')
    x = self.offest
    y = self.offest
    for control in self.controls:
      positions = control.render(self.canvas, x, y)
      y = positions[1]
      x += self.offest
      y += self.offest
    self.after(100, self.draw)

  def show(self):
    self.master.title('BitVX Window')
    self.master.geometry(f'{self.width}x{self.height}')
    self.after(100, self.draw)
    self.mainloop()