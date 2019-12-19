import random

def check_attempts(list_of_emails, your_email):
  counter = 1
  while random.choice(list_of_emails) != your_email:
    counter += 1
  return counter

emails = ['magda@sth.ai', 'travellingprogrammer@gmail.com', 'digitalnomad@magda.me']
print(check_attempts(emails, 'travellingprogrammer@gmail.com'))