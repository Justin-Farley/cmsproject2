import os
import sys

contacts = {}

def display_menu():
    print("menu:")
    print("1. add a new contact")
    print("2. edit an existing contact")
    print("3. delete a contact")
    print("4. search for a contact")
    print("5. display all contacts")
    print("6. export contacts to a text file")
    print("7. import contacts from a text file")
    print("8. quit")

def add_contact():
    print("adding a new contact:")
    name = input("enter the name: ")
    phone = input("enter the phone number: ")
    email = input("enter the email address: ")
    additional_info = input("enter additional info (e.g., address, notes): ")
    contacts[email] = {"name": name, "phone": phone, "email": email, "addition_info": additional_info}
    print("contact added successfully")

def edit_contact():
    print("editing a contact:")
    search_email = input("Enter the email address of the contact to edit: ")
    if search_email in contacts:
        print("Contact found. Please provide updated information:")
        contacts[search_email]["name"] = input(f"Enter the new name ({contacts[search_email]['name']}): ") or contacts[search_email]["name"]
        contacts[search_email]["phone"] = input(f"Enter the new phone number ({contacts[search_email]['phone']}): ") or contacts[search_email]["phone"]
        contacts[search_email]["email"] = search_email  # email cannot be changed as it's used as the key
        contacts[search_email]["additional_info"] = input(f"Enter new additional information ({contacts[search_email]['additional_info']}): ") or contacts[search_email]["additional_info"]
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    print("Deleting a contact:")
    search_email = input("Enter the email address of the contact to delete: ")
    if search_email in contacts:
        del contacts[search_email]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    print("Searching for a contact:")
    search_email = input("Enter the email address of the contact: ")
    if search_email in contacts:
        print(contacts[search_email])
    else:
        print("Contact not found.")


def display_contacts():
    print("Displaying all contacts:")
    if not contacts:
        print("No contacts found.")
    else:
        for email, contact in contacts.items():
            print(contact)

def print_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Additional Information: {contact['additional_info']}")

def export_contacts():
    filename = input("\nEnter the filename to export (e.g., contacts.txt): ")
    with open(filename, 'w') as file:
        for email, contact in contacts.items():
            name = contact.get('name', '')
            phone = contact.get('phone', '')
            email = contact.get('email', '')
            additional_info = contact.get('additional_info', '')
            file.write(f"{name},{phone},{email},{additional_info}\n")
    print("Contacts exported successfully.")

def import_contacts():
    filename = input("\nEnter the filename to import (e.g., contacts.txt): ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    name, phone, email, additional_info = line.strip().split(',')
                    contacts[email] = {"name": name, "phone": phone, "email": email, "additional_info": additional_info}
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("File not found.")

def main():
    print("Welcome to the Contact Management System!")
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
main()



