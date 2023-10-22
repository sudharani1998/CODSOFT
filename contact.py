class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, contact_idx, updated_contact):
        if 0 <= contact_idx < len(self.contacts):
            self.contacts[contact_idx] = updated_contact

    def delete_contact(self, contact_idx):
        if 0 <= contact_idx < len(self.contacts):
            del self.contacts[contact_idx]

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                print("\nSearch results:")
                for idx, result in enumerate(results, start=1):
                    print(f"{idx}. Name: {result.name}, Phone: {result.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            contact_idx = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= contact_idx < len(contact_manager.contacts):
                updated_name = input("Enter updated Name: ")
                updated_phone_number = input("Enter updated Phone Number: ")
                updated_email = input("Enter updated Email: ")
                updated_address = input("Enter updated Address: ")
                updated_contact = Contact(updated_name, updated_phone_number, updated_email, updated_address)
                contact_manager.update_contact(contact_idx, updated_contact)
                print("Contact updated successfully.")
            else:
                print("Invalid index.")

        elif choice == "5":
            contact_idx = int(input("Enter the index of the contact to delete: ")) - 1
            contact_manager.delete_contact(contact_idx)
            print("Contact deleted successfully.")

        elif choice == "6":
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
