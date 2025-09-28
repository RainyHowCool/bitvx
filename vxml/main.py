from parse.tokenizer import Tokenizer
from parse.parser import Parser
from rendertest.gui import Application

tokenizer = Tokenizer()
with open("C:\\Users\\xiaokuai\\Desktop\\bitvx\\vxml\\main.vxml", "r") as file:
  content = file.read()
  tokenizer.bind(content)
  #print("Tokens: {}".format(tokenizer.tokenize()))
  parser = Parser(tokenizer)
  ast = parser.parse()
  print("AST: {}".format(ast))
  app = Application(500, 500)
  for control in ast:
    app.register(control)
  app.show()
  