import re

class Tokenizer:
  pattern_list = []
  compiled_pattern_list = []
  matches_buffer = []
  input = None
  executed = False

  def __init__(self):
    self.pattern_list = [
      (r'\d+', 'INTEGER'),
      (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
      (r'"([^"\\]|\\.)*"', 'STRING'),
      (r'=', 'ASSIGNMENT'),
      (r':', 'COLON'),
      (r'[{}]', 'PARENTHESIS'),
      (r'[,]', 'COMMA'),
      (r'[\n;]', 'NEWLINE')
    ]
    self.compile_pattern_list()

  def set_pattern_list(self, pattern_list: list):
    self.pattern_list = pattern_list

  def compile_pattern_list(self):
    # 一般不需要使用此函数
    self.compiled_pattern_list = [
      (re.compile(pattern), type)
      for pattern, type in self.pattern_list
    ]

  def bind(self, input: str) -> None:
    self.input = input
    self.executed = False

  def tokenize(self) -> list:
    if self.input is None:
        raise ValueError("请先绑定输入字符串")
    if self.executed:
        return self.matches_buffer
    
    pos = 0
    matches = []
    input = self.input
    input_length = len(self.input)
    
    while pos < input_length:
        # 跳过空白字符
        if self.input[pos].isspace():
            pos += 1
            continue
            
        matched = False
        # 在当前位置尝试所有模式
        for pattern, token_type in self.compiled_pattern_list:
            match = pattern.match(input, pos)
            if match:
                # 找到匹配，添加到结果
                token_value = match.group(0)
                token_values = token_value
                if token_type == 'STRING':
                  token_values = token_value[1:-1]  # 去掉引号
                matches.append((token_values, token_type))
                pos += len(token_value)
                matched = True
                break
        
        # 如果没有模式匹配，说明有无法识别的字符
        if not matched:
            raise ValueError(f"无法识别的字符: '{input[pos]}' 在位置 {pos}")
        
    self.executed = True
    return matches