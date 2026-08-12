

while True:
    # Prompt the user to enter a score
    score_input = input("Enter game score")
    
if score.strip().lower() == "stop":
        print("Game session ended.")
else:
    score = int(score_input)  # Convert the input to an integer
    if score > 100:
        print("WOW! That's a NEW high score!")
    else:
        print("Keep trying! You can do better!")