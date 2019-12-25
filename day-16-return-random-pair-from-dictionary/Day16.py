import testyourcode

import random
dictionary = [('Johny', 2), ('Magda', 10), ('Paul', 7)]

def pick_random_pair(dictionary):
  return random.choice(dictionary.items())
  
testyourcode.check_funcion(pick_random_pair)

# for advanced:
#testyourcode.check_funcion2(pick_random_value_n_times) 
