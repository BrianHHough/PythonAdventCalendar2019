#  B E G I N N E R
def fun_with_sets(set1, set2):
  return len(set1.intersection(set2))

testyourcode.check_funcion(fun_with_sets)

#  A D V A N C E D
def fun_with_sets2(set1, set2):
  return len((set1.union(set2)).difference(set1.symmetric_difference(set2)))

