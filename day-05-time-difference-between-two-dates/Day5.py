import testyourcode
import datetime

# B E G I N N E R
def take_difference(datetime1, datetime2):
  return int((datetime2-datetime1).total_seconds())

testyourcode.check_funcion(take_difference)


# A D V A N C E D

def take_difference2(datetime1, datetime2, unit='second'):
    outp_true=int((datetime2-datetime1).total_seconds())
    if unit=='minute':
      outp_true=int(outp_true/60)
    elif unit=='hour':
      outp_true=int(outp_true/3600)
    return outp_true

# For advanced: uncomment the following line
#testyourcode.check_funcion2(take_difference2)
