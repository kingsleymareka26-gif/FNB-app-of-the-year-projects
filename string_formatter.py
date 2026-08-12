# --- Username and Message Formatter ---
# Takes a user's first and last name, and bio, then applies
# string transformations to produce a formatted profile output.

# --- Collect Input ---
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio about yourself: ")

# --- Create username: first initial + last name, all lowercase ---
username = f"{first_name[0].lower()}{last_name.lower()}"

# --- Full name in Title Case ---
full_name = f"{first_name} {last_name}".title()

# --- Clean the bio ---
clean_bio = bio.strip()
length_of_bio = len(clean_bio)
replaced_bio = clean_bio.replace("I am", "I'm")

# --- Output ---
print(f"\nUsername: {username}")
print(f"Full Name: {full_name}")
print(f"Bio: {replaced_bio}")
print(f"Length of Bio: {length_of_bio} characters")