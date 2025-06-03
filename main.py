from lib.db.connection import init_db
from lib.scripts.run_scripts import (
    create_user,
    make_payment,
    start_wifi_session,
    get_active_session_for_user,
    get_user_by_username,
    delete_user,
    update_user_session,
    stop_session,
)

def print_menu():
    print("\n=== WiFi Management CLI ===")
    print("1. Create User")
    print("2. Make Payment")
    print("3. start wifi session")
    print("4. View Active Sessions")
    print("5. View User")
    print("6. Delete User")
    print("7. Update User Session Duration")
    print("8. Stop Session")
    print("9. Exit")

def main():
    init_db()
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            user = create_user(username, password)
            if user:
                print(f"User created: {user.username} (ID: {user.id})")

        elif choice == "2":
            user_id = input("Enter user ID: ").strip()
            amount = input("Enter payment amount: ").strip()
            try:
                amount = float(amount)
                payment = make_payment(int(user_id), amount)
            except ValueError:
                print("Invalid amount or user ID.")
        
        elif choice == "3":  
            user_id = input("Enter user ID: ").strip()
            duration = input("Enter session duration in minutes: ").strip()
            try:
                session = start_wifi_session(int(user_id), int(duration))
                print(f"Started session ID {session.id} for user ID {user_id} lasting {duration} minutes.")
            except ValueError:
                print("Invalid user ID or duration.")

        elif choice == "4":
            user_id = input("Enter user ID: ").strip()
            try:
                sessions = get_active_session_for_user(int(user_id))
                if sessions:
                    print(f"Active sessions for user {user_id}:")
                    for s in sessions:
                        print(f"- Session ID {s.id}, Duration {s.duration_minutes} min, Status {s.status}")
                else:
                    print("No active sessions found.")
            except ValueError:
                print("Invalid user ID.")

        elif choice == "5":
            print("\n View user")
            print("1. View specific user by username")
            print("2. view all users")
            sub_choice = input("choose option: ").strip()

            if sub_choice == "1":
                username = input("Enter username to view: ").strip()
                user = get_user_by_username(username)

                if user:
                    print(f"User ID: {user.id}, Username: {user.username}")
                else:
                    print("User not found.")

            elif sub_choice == "2":
                from lib.scripts.run_scripts import get_all_users
                users = get_all_users
                if users:
                    print("All registered users:")
                    for user in users:
                        print(f"- ID: {user.id}, Username: {user.username}")

                else:
                    print(" No users found.")

            else:
                print("Invalid sub-option.")

        elif choice == "6":
            user_id = input("Enter user ID to delete: ").strip()
            try:
                success = delete_user(int(user_id))
                if success:
                    print("User deleted.")
                else:
                    print("User not found or could not be deleted.")
            except ValueError:
                print("Invalid user ID.")

        elif choice == "7":
            session_id = input("Enter session ID to update: ").strip()
            duration = input("Enter new duration (minutes): ").strip()
            try:
                updated = update_user_session(int(session_id), int(duration))
                if updated:
                    print("Session updated.")
                else:
                    print("Session not found or could not be updated.")
            except ValueError:
                print("Invalid input.")

        elif choice == "8":
            session_id = input("Enter session ID to stop: ").strip()
            try:
                stopped = stop_session(int(session_id))
                if stopped:
                    print("Session stopped.")
                else:
                    print("Session not found or could not be stopped.")
            except ValueError:
                print("Invalid session ID.")

        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
