import os # for clearing the console after each operation
import csv # contacts are saved as a .csv file [csv: Comma Separated Values]
import re # using regular expressions for validating details

class ContactBook:
    def __init__(self, filename="contacts.csv"):
        # the contact book will be a dictionary of dictionaries, where the keys will be contact names
        self.contacts = {}
        # here a name will be mapped to a dictionary of {phone_num, email, address} named 'details'
        self.filename = filename
        self.load_contacts() # loads any previously save contacts from the .csv file

    def add_contact(self, name, phone_number, email, address):
        if name not in self.contacts:
            new_contact = {
                'phone_number': phone_number,
                'email': email,
                'address': address
            }
            self.contacts[name] = new_contact # mapping the details with the name
            self.save_contacts() # saving in the .csv file for maintaining progress
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists. Please use a different name or edit the current contact.")

    def display_contacts(self):
        # Prints a list of all contacts with only their phone numbers.
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for name, details in self.contacts.items():
                print(f"{name}: {details['phone_number']}")

    def search_contact(self, query):
        found_contacts = [] # as there can be several contacts containing same query phrase, they will be contained within a list
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query == details['phone_number']:
                found_contacts.append(name)

        if found_contacts:
            print(f"\nContacts matching '{query}':")
            for contact_name in found_contacts:
                self.print_contact_details(contact_name, self.contacts[contact_name])
        else:
            print(f"No contacts found matching '{query}'.")

    def edit_contact(self, name, new_phone_number, new_email, new_address):
        # I'm confused if I should add an option to edit the name of the contact too. Maybe will add this feature in the future.
        self.contacts[name]['phone_number'] = new_phone_number
        self.contacts[name]['email'] = new_email
        self.contacts[name]['address'] = new_address
        self.save_contacts()
        print(f"Contact '{name}' edited successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found. Deletion failed.")

    def save_contacts(self):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for name, details in self.contacts.items():
                    writer.writerow([name, details['phone_number'], details['email'], details['address']])
            print(f'Contacts saved to {self.filename}')
        except Exception as e:
            print(f"Error saving contacts: {e}")

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for values in reader:
                    if len(values) == 4:
                        name, phone_number, email, address = values
                        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
                    else:
                        print(f"Skipping invalid line: {values}")
            print(f'Contacts loaded from {self.filename}')
        except FileNotFoundError:
            print('No previously saved contacts found. Starting from an empty contact book.')
        except Exception as e:
            print(f"Error loading contacts: {e}")

    def print_contact_details(self, name, details):
        print(f"\nContact Details for '{name}':")
        print(f"Phone: {details['phone_number']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")

    # validation of all the inputs
    
    ALLOWED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 .-'
    def validate_contact_name(self, name):
        if not bool(name): # returns false if the name is empty
            return False
        for char in name:
            if char not in self.ALLOWED_CHARS:
                return False
        if len(name) < 3: # I don't think valid names can be shorter than 3 letters
            return False
        return True


    def validate_phone_number(self, phone_number):
        return phone_number.isdigit()

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def validate_address(self, address):
        return bool(address)

def main():
    contact_book = ContactBook()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print("\n~~:Contact Book Management System:~~ \n")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        print()

        if choice == '1':
            name = input("Enter the contact name: ")
            if contact_book.validate_contact_name(name):
                phone_number = input("Enter the phone number: ")
                if contact_book.validate_phone_number(phone_number):
                    email = input("Enter the email: ")
                    if contact_book.validate_email(email):
                        address = input("Enter the address: ")
                        if contact_book.validate_address(address):
                            contact_book.add_contact(name, phone_number, email, address)
                        else:
                            print("Invalid address. Please enter a valid address.")
                    else:
                        print("Invalid email address. Please enter a valid email.")
                else:
                    print("Invalid phone number. Please enter a valid phone number.")
            else:
                print("Invalid contact name. Please enter a valid name.")
            # I know this looks awful but it's the best validation interface I could come up with

        elif choice == '2':
            contact_book.display_contacts()

        elif choice == '3':
            name = input("Enter the contact name or phone number to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            name = input("\nEnter the contact name to edit: ")
            if name in contact_book.contacts:
                new_phone_number = input("Enter the phone number: ")
                if contact_book.validate_phone_number(new_phone_number):
                    new_email = input("Enter the email: ")
                    if contact_book.validate_email(new_email):
                        new_address = input("Enter the address: ")
                        if contact_book.validate_address(new_address):
                            contact_book.edit_contact(name, new_phone_number, new_email, new_address)
                        else:
                            print("Invalid address. Please enter a valid address.")
                    else:
                        print("Invalid email address. Please enter a valid email.")
                else:
                    print("Invalid phone number. Please enter a valid phone number.")
            else:
                print(f"Contact '{name}' not found. Editing failed.")

        elif choice == '5':
            name = input("Enter the contact name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book Management System. Goodbye!\n")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

        input("\nPress Enter to continue...")  
        # pausing the console to allow the user to see output, otherwise the output will be automatically cleared before the user sees it.


if __name__ == "__main__":
    main()
