#  B E G I N N E R
def get_avg_difficulty(list_of_lists):
  all_scores = []
  for subl in list_of_lists:
    all_scores = all_scores + subl
  return sum(all_scores)/len(all_scores)
  
l = [[1,0,8,4], [2, 5, 6, 2], [8,8,1,7], [1,9,4,5]] 
print(get_avg_difficulty(l))


#  A D V A N C E D
def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
        
def get_median_difficulty(list_of_lists):
  all_scores = []
  for subl in list_of_lists:
    all_scores = all_scores + subl
  return median(all_scores)