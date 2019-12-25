import testyourcode

# B E G I N N E R
def check_insta_handle(name):
  if all(['_' not in name, '-' not in name, len(name)<=20,
          not name.startswith('.'), not name.endswith('.')]):
    return 'Good'
  else:
    return 'Bad'

  
testyourcode.check_funcion(check_insta_handle)
  
  
# A D V A N C E D

import re
def check_insta_handle2(name):
  if all(['_' not in name, '-' not in name, len(name)<=20,
          not name.startswith('.'), not name.endswith('.'), 
          (name.lower()==name or name.upper()==name), 
          len(re.findall('[@!#$%^&*?~:]', name))==0, 
          not bool(re.search('\d', name))]):
    return 'Good'
  else:
    return 'Bad'
  
# for advanced:
#testyourcode.check_funcion2(check_insta_handle2)
