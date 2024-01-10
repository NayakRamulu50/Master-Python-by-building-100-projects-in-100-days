# Welcome message
print("Welcome to the tip calculator!")

# Input the total bill amount
total_bill = float(input("What was the total bill? $"))

# Input the tip percentage
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Input the number of people to split the bill
num_people = int(input("How many people to split the bill? "))

# Calculate the tip and total amount
tip_amount = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip_amount

# Calculate each person's share
each_person_share = total_amount / num_people

# Format the result to 2 decimal places
each_person_share_formatted = "{:.2f}".format(each_person_share)

# Display the result
print(f"Each person should pay: ${each_person_share_formatted}")
