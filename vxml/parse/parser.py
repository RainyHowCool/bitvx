from tkinter import Canvas, font
from .tokenizer import Tokenizer

class Control:
  def render(self, canvas: Canvas, x: int, y: int) -> tuple:
    pass

class Text(Control):
  text = None
  color = None

  def __init__(self, attributes: dict):
    self.text = attributes['text']
    self.color = attributes.get('color', 'black')

  def __str__(self):
    return f"Text({self.text}, {self.color})"
  
  def __repr__(self):
    return self.__str__()
  
  def render(self, canvas: Canvas, x: int, y: int):
    text_font = font.Font(family="Arial", size=12)
    canvas.create_text(x, y, text=self.text, fill=self.color, font=text_font)
    return (x + (12 * len(self.text)), y + 12)
  

class Button(Control):
  text = None
  color = None

  def __init__(self, attributes: dict):
    self.text = attributes['text']
    self.color = attributes.get('color', 'black')

  def __str__(self):
    return f"Button({self.text}, {self.color})"
  
  def __repr__(self):
    return self.__str__()
  
  def round_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    canvas.create_polygon(points, **kwargs, smooth=True)
  
  def render(self, canvas: Canvas, x: int, y: int):
    text_font = font.Font(family="Arial", size=12)
    self.round_rectangle(canvas, x, y, x + 100, y + 50, fill='snow', outline='white', width=2)
    canvas.create_text(x + 50, y + 25, text=self.text, fill=self.color, font=text_font)
    return (x + 100, y + 50)

class Parser:
  tokenizer = None
  def __init__(self, tokenizer):
    self.tokenizer = tokenizer;
  
  def get_attributes(self, pos: int, token: list):
    attributes = {}
    prev = []
    curr = []
    next = []

    while pos < len(token) - 1 and token[pos][1] != 'NEWLINE':
      curr = token[pos]
      if pos < len(token):
        next = token[pos + 1]
      else:
        next = None

      if curr[1] == 'COLON':
        attributes[prev[0]] = next[0]
      elif curr[1] == 'COMMA':
        pos += 2
        prev = next
        continue

      prev = curr
      pos += 1
    print(attributes)
    return (pos, attributes)

  def parse(self):
    ast_list = []
    # 三个指针，分别指向当前、前一个和后一个token
    prev = []
    curr = []
    next = []
    
    token = self.tokenizer.tokenize()
    ptr = 0
    while ptr < len(token) - 1:
      curr = token[ptr]
      if ptr < len(token):
        next = token[ptr + 1]
      else:
        next = None

      if curr[1] == 'ASSIGNMENT':
        controlType = prev[0];
        pos, attributes = self.get_attributes(ptr, token)
        match controlType:
          case 'Text':
            ast_list.append(Text(attributes))
          case 'Button':
            ast_list.append(Button(attributes))

      prev = curr
      ptr += 1
    return ast_list