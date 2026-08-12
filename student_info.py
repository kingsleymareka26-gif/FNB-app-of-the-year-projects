# student info formatter
# collect personal personal information and display it in a formatted profile

#--- Collect input ---
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = int(input("Enter your favourite number: "))

#--- String manipulation ---
full_name = f"{first_name} {surname}"
full_name_upper = full_name.upper()
full_name_title = full_name.title()

#--- Arithmetic ---
age_in_months = age * 12
favourite_number_rounded = round(favourite_number ** 2)

#--- Output ---
print(f"\nWelcome, {full_name}!")
print(f"Name (UPPERCASE): {full_name_upper}")
print(f"Name (Title Case): {full_name_title}")
print(f"Age in Months: {age_in_months}")
print(f"Favourite Number ( Rounded to 2 Decimal Places): {favourite_number_rounded}")

print("\n--- Data Types ---")
print(f"First Name: {first_name} (Type: {type(first_name)})")
print(f"Surname: {surname} (Type: {type(surname)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Favourite Number: {favourite_number} (Type: {type(favourite_number)})")