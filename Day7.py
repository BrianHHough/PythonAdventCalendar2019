
#  B E G I N N E R

def check_destination(city, avg_temp, avg_airbnb_price, time_offset):
  if all([avg_temp>15, avg_airbnb_price <= 1000, 0 <= time_offset <= 8]):
    return "%s is a good destination." % city
  else:
    return "%s is a bad destination." % city

print(check_destination("Lisboa", 18.5,   1050.90,  0))


#  A D V A N C E D
print('----------------------------')
from datetime import datetime, timedelta

def get_local_time(city, time_offset):
  return "It is %s local time in %s right now." % ((datetime.utcnow() + timedelta(hours=time_offset)).strftime("%X"), city)
  
print(get_local_time("Warsaw", 1))
