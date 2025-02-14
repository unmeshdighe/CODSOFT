# Dictionary to store contacts
contacts = {}

def add_contact():
    print("\n--- Add a New Contact ---")
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email: ").strip()
    address = input("Enter the contact's address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    search_term = input("\nEnter the name or phone number to search: ").strip().lower()
    found = False

    for name, details in contacts.items():
        if search_term in name.lower() or search_term in details["phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True

    if not found:
        print("No matching contacts found.")

def update_contact():
    name = input("\nEnter the name of the contact to update: ").strip()
    if name in contacts:
        print(f"\nUpdating contact: {name}")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()
        address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()

        contacts[name]["phone"] = phone if phone else contacts[name]["phone"]
        contacts[name]["email"] = email if email else contacts[name]["email"]
        contacts[name]["address"] = address if address else contacts[name]["address"]
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("\nEnter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()