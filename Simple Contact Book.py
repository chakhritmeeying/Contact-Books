import json

# # Load contact file


def load_contacts():
    try:
        with open("contact.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# # Save Ccontact to .txt file


def save_contacts(contacts):
    with open("contact.txt", "w") as file:
        json.dump(contacts, file)


# Function add new contact
def add_contact(contacts):
    contact_name = input("Enter contact neme : ")
    contact_phone = input("Ente contact phone number : ")
    contacts.append({"name": contact_name, "phone": contact_phone})

# Function show contact list


def show_contacts(contacts):
    print("----- Contact List -----")
    for idx, info in enumerate(contacts, start=1):
        print(f"{idx}. Name : {info['name']} | Phone : {info['phone']}")
    print("------------------------\n")

# Function remove contact


def remove_contact(contacts, remove_index):
    if 1 <= remove_index <= len(contacts):
        return contacts.pop(remove_index - 1)

# Function search contact


def search_contact(contacts):
    print("Search a Contact")
    search_keyword = input("Enter the keyword you want to search : ")
    matching = []
    for idx, info in enumerate(contacts, start=1):
        if search_keyword.lower() in str(info['name']).lower() or search_keyword in info['phone']:
            matching.append({"name": info['name'], "phone": info['phone']})
    return matching


# Main Program
contacts = load_contacts()
print("Welcome to Contack book!!")
while True:
    print("1. Add a contact")
    print("2. View contact")
    print("3. Remove a contact")
    print("4. Search contact")
    print("5. Exit")

    user_input = input("Enter you choice [1-5] : ")
    # choice 1 Add contact
    if user_input == "1":
        add_contact(contacts)
        save_contacts(contacts)
    # choice 2 view contact
    elif user_input == "2":
        if not contacts:
            print("You don't have contact list.")
            continue
        else:
            show_contacts(contacts)
    # choice 3 remove contact
    elif user_input == "3":
        if not contacts:
            print("You don't have contact list.")
        else:
            show_contacts(contacts)
            remove_choice = input(
                "Enter the number of list you want to remove : ")
            try:
                remove_index = int(remove_choice)
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue
            contact = remove_contact(contacts, remove_index)
            print(
                f"Name {contact['name']} has been remove form you contact book.")
            save_contacts(contacts)
    # choice 4 search contact
    elif user_input == "4":
        matching_contacts = search_contact(contacts)
        if not matching_contacts:
            print("No matching contact found.")
            continue
        else:
            print("----- Matching List -----")
            for idx, info in enumerate(matching_contacts, start=1):
                print(
                    f"{idx}. Name : {info['name']} | Phone : {info['phone']}")
            print("------------------------\n")
    # choice 5 close program
    elif user_input == "5":
        # save_contacts(contacts)
        print("Exiting the contact book.")
        break
    else:
        print("Invalid choice. Please try again.\n")
