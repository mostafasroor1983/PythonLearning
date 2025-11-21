#Tenary 
grade = 90
score = "A+" if grade >= 90 else "A" if grade >= 80 else "B" if grade >= 70 else "C" if grade >= 60 else "F"
print(f"Your score is: {score}")
print("#"*50)