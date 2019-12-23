def find_missing_digit(pseudo_number):
  test_list = ['1900800x0', '9000000x0', '1234x4321']
  results = []
  for pseudo_number in test_list:
    digits_sum = sum([int(i) for i in pseudo_number if i!='x'])
    for i in range(10):
      if (digits_sum+i)%10==0:
        return i