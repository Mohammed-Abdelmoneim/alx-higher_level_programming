#!/usr/bin/python3
def multiple_returns(sentence):
      leng = len(sentence)
      first_char = ""
      if len(sentence) > 0:
          first_char = sentence[0]
      else:
           first_char = "None"
      return (leng, first_char)    
