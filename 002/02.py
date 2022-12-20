# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Weight doesnt necessarily need decimal places bc it's already pretty accurate as an int
bmi = int(int(weight) / float(height) ** 2)
print("Your BMI is: {0}".format(bmi))