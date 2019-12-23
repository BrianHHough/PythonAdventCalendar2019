def split_participants(dictionary):
  beginners, intermediate, advanced = [], [], []
  for item in dictionary.items():
    if item[1] < 3:
      beginners.append(item[0])
    elif item[1] > 7:
      advanced.append(item)
    else: 
      intermediate.append(item[1])
  return beginners, intermediate, advanced
  
participants_skills = {'John':3, 'Mike':0, 'Anna':2, 'Jacob':3, 'Tomas':10, 'Peter':1, 'Gabby':7}
print(split_participants(participants_skills))
