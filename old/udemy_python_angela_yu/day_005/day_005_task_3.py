student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# print(max(student_scores))

max_number = student_scores[0]
# print(type(max_number))
# print(type(student_scores))

for highest_score in student_scores:
  if highest_score > max_number:
    max_number = highest_score
  
print(max_number)




