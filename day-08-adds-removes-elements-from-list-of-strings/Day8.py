# B E G I N N E R
def manage_participants(participants_list, to_remove_list, to_add_list):
  new_list = participants_list
  if len(to_remove_list)>0:
    new_list = [p for p in participants_list if p not in to_remove_list]
  if len(to_add_list)>0:
    for p in to_add_list:
      if p not in new_list:
        new_list.append(p)
  return sorted(new_list)


# A D V A N C E D
def manage_participants_advanced(participants_list, to_remove_list, to_add_list):
  new_list = participants_list
  if len(to_remove_list)>0:
    new_list = [p for p in participants_list if p not in to_remove_list]
  if len(to_add_list)>0:
    for p in to_add_list:
      if p not in new_list:
        new_list.append(p)
      else:
        new_list = list(map(lambda b: b.replace(p,p+"_1"), new_list))
        new_list.append(p+'_2')
  new_list.sort()
  return sorted(new_list)
