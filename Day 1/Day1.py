# write a function text_message(name,n)
# argument turning name + n
# return message "Dear John, you have solved 5 tasks so far."

import testyourcode

def text_message(name,n):
  return "Dear %s, you have solved %s tasks so far"%(name, n)

print(text_message("John", 5))
  
testyourcode.check_funcion(text_message)
