def ask_name():
    while True:
        name = input("Enter player name: ").strip()
        if name:
            return name[:30]
        print("Name cannot be empty.")

def menu():
    print("\n=== ROCK PAPER SCISSORS ===")
    print("1. Play round")
    print("2. View scoreboard")
    print("3. Reset scoreboard")
    print("4. Exit")
    return input("Enter option: ").strip()
