import os

def register_user():
    user_id = input("Enter User ID: ")
    auth_key = input("Enter Auth Key: ")
    private_key = input("Enter Private Key: ")

    with open(f'users/{user_id}.txt', 'w') as f:
        f.write(f"{auth_key}\n{private_key}\n{user_id}")
    print(f"User {user_id} registered.")

if __name__ == "__main__":
    os.makedirs("users", exist_ok=True)
    register_user()
    
    
    
    

