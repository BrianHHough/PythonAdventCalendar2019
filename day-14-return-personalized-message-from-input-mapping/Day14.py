import testyourcode

def send_personalized_email(mapping, email_address):
  mapping = {'Magda' : 'travellingprogrammer@gmail.com', 'John': 'johny@gmail.com'}
  reverse_mapping = {j:i for i,j in mapping.items()}
  email_address = ['travellingprogrammer@gmail.com', 'johny@gmail.com']
  results =s []
  for email_address in reverse_mapping:
    return 'Dear %s, congrats on solving the task!' % (reverse_mapping[email_address])

print(send_personalized_email('Magda', 'travellingprogrammer@gmail.com'))

testyourcode.check_funcion(send_personalized_email)
