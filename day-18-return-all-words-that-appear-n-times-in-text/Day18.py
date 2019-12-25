import testyourcode

# F I N A L

from collections import Counter

def get_top_words(plain_text, n):
  return sorted([i[0] for i in Counter(plain_text.split()).items() if i[1]>=n])
  
text = "this challenge is like piece of cake for you if you like coding"
print(get_top_words(text, 2))
  
testyourcode.check_funcion(get_top_words)
