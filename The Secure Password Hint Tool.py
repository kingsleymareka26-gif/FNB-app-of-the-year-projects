# ---Create a script that helps users generate a secure password hint based on their input. The script should prompt the user for their first name, last name, and a memorable word or phrase. It should then create a password hint that combines the first letter of their first name, the last letter of their last name, and the memorable word or phrase, all in lowercase. Finally, it should display the generated password hint to the user.

# --- Collect Input ---
password = input("Enter a memorable word or phrase: ").strip()

# --- Clean up accidental spaces ---
password = password.strip()

# --- Grab first and last letter ---
first_letter = password[0]
last_letter = password[-1]

# --- Print the hint in uppercase ---
print(f"Your password hint is:It starts with {first_letter.lower()} and ends with{last_letter.upper()}.")

