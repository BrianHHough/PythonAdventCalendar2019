# B E G I N N E R S

def fun_with_words(word):
  return word+word[::-1]
  
# A D V A N C E D
import re
def fun_with_words2(word):
  new_word=fun_with_words(word)
  for vowel in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    new_word = new_word.replace(vowel, '')
  return new_word


