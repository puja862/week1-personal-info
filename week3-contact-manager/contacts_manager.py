# Contact Management System
# Week 3 Project – Functions & Dictionaries
# Author: Vemula Puja

import json
import re
import os
from datetime import datetime

DATA_FILE = "contacts_data.json"

def validate_phone(phone):
    digits = re.sub(r"\D", "", phone)
    return 10 <= len(digits) <= 15, digits

def validate_email(email):
    if email == "":
        return True
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Name: ").strip()
    if not name or name in contacts:
        print("Invalid or duplicate name")
        return
    phone = input("Phone: ")
    valid, phone = validate_phone(phone)
    if not valid:
        print("Invalid phone")
        return
    email = input("Email: ")
    if not validate_email(email):
        print("Invalid email")
        return
    contacts[name] = {
        "phone": phone,
        "email": email,
        "created_at": datetime.now().isoformat()
    }
    print("Contact added")

def main():
    contacts = load_contacts()
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            print(json.dumps(contacts, indent=4))
        elif choice == "3":
            save_contacts(contacts)
            print("Goodbye")
            break

if __name__ == "__main__":
    main()
