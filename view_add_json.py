import json

def load_scores():
    try:
        with open("scores.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_scores(score_list):
    with open("scores.json", "w") as file:
        json.dump(score_list, file, indent=4)

def add_score(name, score):
    scores = load_scores()
    scores.append({"name" : name, "score" : score})
    save_scores(scores)
    print("Scores saved!")

print("+---------- MENU ----------+")
print(" 1. View Scores")
print(" 2. Add Score")
print(" 3. Exit")

while True: 

    user_input = input("Choose an option : ")
    if user_input == '1':
        print(load_scores())

    elif user_input == '2':
        name = input("Enter a name : ")
        score = input("Enter score : ")
        add_score(name, score)

    elif user_input == '3':
        break

    else:
        print("Invalid Input. Enter a valid number.")
        
