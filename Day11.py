
def compute_average_price(list_of_tuples):
  test_list = [(469.25, 28), (32.44, 2), (35.34, 2)]
  results = []
  return round((sum([el[0] for el in test_list]) / sum(el[1] for el in test_list)), 2)

print(compute_average_price([(469.25, 28), (32.44, 2), (35.34, 2)]))
