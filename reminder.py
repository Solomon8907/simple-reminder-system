# Simple Reminder System
# Name: Omosegbon Solomon Ayomide
# Matric No: 24/13797
# Department: Computer Science

reminders = []

def add_reminder():
    reminder = input("Enter your reminder: ")
    reminders.append(reminder)
    print("✅ Reminder added successfully!\n")

def view_reminders():
    if not reminders:
        print("📭 No reminders available.\n")
    else:
        print("\n📌 Your Reminders:")
        for index, reminder in enumerate(reminders, start=1):
            print(f"{index}. {reminder}")
        print()

def main():
    while True:
        print("=== Simple Reminder System ===")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_reminder()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Program execution starts here
main()
