import json


def load_contact():
    try:
        with open("contacts.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contact(contacts):
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)


def add_contact(contacts):
    contact_name = input("Enter contacat name: ")
    contact_phone = input("Enter contact phone: ")
    contacts.append({"name": contact_name, "phone": contact_phone})


def view_contact(contacts):
    for idx, info in enumerate(contacts, start=1):
        line = " | ".join(f"{key} : {values}" for key, values in info.items())
        print(f"{idx}. {line}")


def search_contact(contacts):
    print("----- Search List -----")
    search_keyword = input("Enter the keyword you want to search : ")
    matching = []
    for idx, info in enumerate(contacts, start=1):
        if any(search_keyword.lower() in str(values).lower() for values in info.values()):
            matching.append(info)
    return matching


def remove_contact(contacts, remove_index):
    if 1 <= remove_index <= len(contacts):
        return contacts.pop(remove_index-1)


# test function
if __name__ == "__main__":
    c = load_contact()

    # matching_contact = search_contact(c)
    # if not matching_contact:
    #     print("Contact not found.")
    # else:
    #     print(f"----- Found {len(matching_contact)} list. -----")
    #     view_contact(matching_contact)
    #     print("------------------------\n")

    print("----- Remove contact List -----")
    view_contact(c)
    remove_item = input("Enter number of list you want to remove: ")
    try:
        remove_index = int(remove_item)
    except ValueError:
        print("Error")
    contact = remove_contact(c, remove_index)
    print(f"Name {contact['name']} has been remove from contact book.")

    print("------------------------\n")
    view_contact(c)
