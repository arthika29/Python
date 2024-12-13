import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

# Search for a contact
def search_contact():
    search_name = input("Enter name to search: ")
    contacts = load_contacts()
    found = [c for c in contacts if search_name.lower() in c['name'].lower()]

    if not found:
        print("No contacts found.")
    else:
        print("\nSearch Results:")
        for contact in found:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

# Delete a contact
def delete_contact():
    name_to_delete = input("Enter name of the contact to delete: ")
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c['name'].lower() != name_to_delete.lower()]

    if len(contacts) == len(updated_contacts):
        print("Contact not found.")
    else:
        save_contacts(updated_contacts)
        print("Contact deleted successfully!")

# Update a contact
def update_contact():
    name_to_update = input("Enter name of the contact to update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name_to_update.lower():
            print("Leave field blank to keep current value.")
            contact['name'] = input(f"New name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"New phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"New email ({contact['email']}): ") or contact['email']
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Main menu
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
