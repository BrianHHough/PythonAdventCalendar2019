# B E G I N N E R

def text_message(name,n):
  return 'Dear {}, you have solved {} tasks so far.'.format(name,n)

print(text_message('John', 5))

# A D V A N C E D

import datetime

def text_message_advanced(name, n, last_access_timestamp):
  percentage = n/24*100
  return("""Dear {}, your participation rate was {}% \ and your last access was on {} at {}""".format(name, str(round(percentage, 1)), 
  last_access_timestamp.strftime("%d-%m-%Y"), 
  last_access_timestamp.strftime("%I:%M:%S %p")))

result = text_message_advanced("John", float(5), datetime.datetime(2019,12,6,8,56,1))

print(result)
