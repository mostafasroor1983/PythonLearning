age = input("Enter your age:")

try:
    age = int(age)
    income = 20000
    risk = income / age
    print(f"You are {age} years old.")
except ValueError as e:
    print(f"Invalid input! Please enter a numeric value for age: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


