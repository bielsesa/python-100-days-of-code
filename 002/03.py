# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Time calculations
#   Years left
years_left = 90 - int(age)
#   12 months in a year
months = years_left * 12
#   52 weeks in a year
weeks = years_left * 52
#   365 days in a year
days = years_left * 365

# Final output
print(f"You have {days} days, {weeks} weeks, and {months} months left.")