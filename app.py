def greet_user(name):
    print(f"Hello, {name}! Welcome to Git Demo.")

def farewell_user(name):
    print(f"Goodbye, {name}! See you next time.")

if _name_ == "_main_":
    user_name = input("Enter your name: ")
    greet_user(user_name)
    farewell_user(user_name)