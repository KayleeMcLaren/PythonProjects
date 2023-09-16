# Life in Weeks Exercise
# A program using maths and f-Strings that tells you how many days, weeks, months you have left assuming you live until 90 years old

age = input("What is your current age? ")

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
