import testyourcode

# O P T I O N  1 
def count_letters(text, letter):
  return text.lower().count(letter.lower())
  
# O P T I O N  2
import re
def count_letters2(text, letter):
  return len(re.findall(letter.lower(), text.lower()))

# O P T I O N  3
def count_letters3(text, letter):
  return sum(map(lambda x : 1 if letter.lower() in x else 0, text.lower())) 

testyourcode.check_funcion(count_letters)
