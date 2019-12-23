from collections import Counter

def check_domains(list_of_emails):
  return Counter([d.split('@')[1] for d in list_of_emails])

emails = ['magda@gmail.com', 'travelingprogrammer@yahoo.com','polishgirl@outlook.com', 'travelingprogrammer@gmail.com']
print(check_domains(emails))
