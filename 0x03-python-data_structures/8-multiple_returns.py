#!/usr/bin/python3
def multiple_returns(sentence):
      if len(sentence) == 0:
          return ("None")
      else:
          leng = len(sentence)
          first_char = sentence[0]
          return (leng, first_char)
