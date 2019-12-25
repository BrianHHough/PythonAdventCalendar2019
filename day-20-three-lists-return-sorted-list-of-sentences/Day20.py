import testyourcode

def generate_sentences(subjects, verbs, objects):
  subjects = ["I", "You"]
  verbs = ["love", "like"]
  objects = ["Python", "coding"]
  return sorted(["%s %s %s." % (subjects[a], verbs[b], objects[c]) for a in range(len(subjects)) for b in range(len(verbs)) for c in range(len(objects))])
  
testyourcode.check_funcion(generate_sentences)
