age = input("Are you a cigarette addict older than 75 years old?. Enter Yes or No:").title()
chronic = input("Do you have a severe chronic disease? Enter Yes or No:").title()
immune = input("Is your immune system too weak? Enter Yes or No:").title()

if age == "Yes" and chronic == "Yes" and immune == "Yes":
print("You are in risky group")
elif age == "Yes" and chronic == "Yes" and immune == "No":
print("You are in risky group")
elif age == "No" and chronic == "Yes" and immune == "Yes":
print("You are in risky group")
elif age == "Yes" and chronic == "No" and immune == "Yes":
print("You are in risky group")
else :
print("You are not in risky group")
