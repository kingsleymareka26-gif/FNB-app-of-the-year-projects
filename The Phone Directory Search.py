#Dictionary acting as a mini phone directory
# keys are friend names and values are their phone numbers
# Numbers are kept as strings so a leading "0" is not lost
contacts = {
    "Mbali": "0776549850",
    "Lepedi": "0776549851",
    "Kingsley": "0776549852"
}
#Ask the user which contact they want to call
name = input("Enter the name of the friend you want to call: ")

# Check if the entered name exists as a key in the contacts dictionary
if name in contacts:
   # Name found - look up its corresponding phone number
   print(f"Found!{name}'s phone number is {contacts[name]}.")
else:
    # Name doesn't match any key - nothing to look up
    print("Contact not found.")