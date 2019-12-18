
def choose_destination(list_of_tuples):
  return sorted([t[0] for t in list_of_tuples if t[1]])
  
  
print(choose_destination([('Warsaw', False), ('Barcelona', True), ('Alicante', True)]))
