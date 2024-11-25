import random

# Data storage
users = {}
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": 0},
    {"question": "Which is the smallest prime number?", "options": ["0", "1", "2", "3"], "answer": 2},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": 1},
    {"question": "What is the boiling point of water?", "options": ["90°C", "100°C", "110°C", "120°C"], "answer": 1},
    {"question": "Who wrote 'Macbeth'?", "options": ["Shakespeare", "Keats", "Wordsworth", "Byron"], "answer": 0},
    {"question": "Which planet is closest to the sun?", "options": ["Venus", "Earth", "Mercury", "Mars"], "answer": 2},
    {"question": "What is the square root of 16?", "options": ["2", "3", "4", "5"], "answer": 2},
    {"question": "Which gas is essential for human respiration?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": 1},
    {"question": "What color is the sky on a clear day?", "options": ["Red", "Blue", "Green", "Yellow"], "answer": 1},
    {"question": "Which is the largest ocean?", "options": ["Indian", "Pacific", "Atlantic", "Arctic"], "answer": 1},
    {"question": "Who discovered gravity?", "options": ["Newton", "Einstein", "Tesla", "Galileo"], "answer": 0},
    {"question": "What is the atomic number of Hydrogen?", "options": ["1", "2", "3", "4"], "answer": 0},
    {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": 0},
    {"question": "Which is the longest river?", "options": ["Amazon", "Nile", "Ganga", "Yangtze"], "answer": 1},
    {"question": "What is the national animal of India?", "options": ["Tiger", "Lion", "Elephant", "Leopard"], "answer": 0},
    {"question": "Which is the fastest land animal?", "options": ["Cheetah", "Lion", "Horse", "Deer"], "answer": 0},
    {"question": "What is the primary source of energy on Earth?", "options": ["Wind", "Water", "Sun", "Coal"], "answer": 2},
    {"question": "Which is the coldest continent?", "options": ["Asia", "Africa", "Antarctica", "Europe"], "answer": 2},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Shark", "Giraffe"], "answer": 1},
    {"question": "Which is the smallest state in India by area?", "options": ["Goa", "Sikkim", "Delhi", "Tripura"], "answer": 0},
]

# Authentication functions
def register_user():
    username = input("Enter a username: ").strip()
    if username in users:
        print("Username already exists. Try logging in.")
        return False
    password = input("Enter a password: ").strip()
    users[username] = {"password": password, "score": 0}
    print("Registration successful!")
    return True

def login_user():
    username = input("Enter your username: ").strip()
    if username not in users:
        print("User not found. Please register.")
        return None
    password = input("Enter your password: ").strip()
    if users[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Incorrect password.")
        return None

# Game functions
def play_game(username):
    score = 0
    shuffled_questions = random.sample(questions, 10)
    for i, question_data in enumerate(shuffled_questions):
        print(f"\nQuestion {i+1}: {question_data['question']}")
        for idx, option in enumerate(question_data["options"]):
            print(f"{idx}. {option}")
        try:
            answer = int(input("Enter the option number (0-3): ").strip())
            if answer == question_data["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
        except ValueError:
            print("Invalid input. Skipping question.")
    print(f"\nYou scored {score} out of 10!")
    users[username]["score"] += score
    print(f"Total score: {users[username]['score']}")

# Main menu
def main_menu():
    current_user = None
    while True:
        print("\n--- Quiz Application ---")
        if current_user:
            print(f"Welcome, {current_user}! Choose an option:")
            print("1. Play Quiz")
            print("2. Logout")
        else:
            print("1. Login")
            print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            if current_user:
                play_game(current_user)
            else:
                current_user = login_user()
        elif choice == "2":
            if current_user:
                current_user = None
                print("Logged out successfully.")
            else:
                if register_user():
                    print("You can now log in.")
        elif choice == "3":
            print("Thank you for using the Quiz Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main_menu()
