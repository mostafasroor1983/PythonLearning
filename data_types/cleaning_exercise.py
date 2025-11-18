text = "968-Maria, (Data@Engineer);; 29y  "

# Cleaning the string
second_part = text.strip().split('-')[1] 
third_part = second_part.strip().split('(')[1]
fourth_part = third_part.strip().split(');;')[1].strip()
print(f"name: {second_part[0:5]} | role : {third_part.replace("@"," ")[0:13]}| age:{fourth_part[0:2]} ") # Remove leading/trailing whitespace and split by '-'