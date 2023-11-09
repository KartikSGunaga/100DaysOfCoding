student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

def get_grade(score):
  if(score > 90):
    return "Outstanding"
  elif(score > 80):
    return "Exceeds Expectations"
  elif(score > 70):
    return "Acceptable"
  else:
    return "Fail"

for names in student_scores:
  student_grades[names] = get_grade(student_scores[names])

print(student_grades)