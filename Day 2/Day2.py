# write a function fun_with_words(word)
# input = word; returns new word that's a combination of given word and its reverse

import testyourcode

def fun_with_words(word):
  return word + word[::-1]

reverse_word = fun_with_words("TrAvElInGpRoGrAmMeR")

print(reverse_word)

testyourcode.check_funcion(fun_with_words)
