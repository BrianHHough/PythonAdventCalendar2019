
def clean_participants_list(participants):
  participants.sort(reverse=True)
  if "Magda" in (participants):
    participants.remove("Magda")
  participants.insert(1, "Gabby")
  return(participants[-2])
  
challenge_participants = ['John', 'Mike', 'Anna', 'Jacob', 'Magda', 'Tomas', 'Peter']
print(clean_participants_list(challenge_participants))

