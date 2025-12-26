import function
contacts = function.load_contact()
print("Well come to Contact Books !!")
while True:
    print("1.Add Contact")
    print("2.Veiw Contact")
    print("3.Search Contact")
    print("4.Remove Contact")
    print("5.Exit Program")

    user_input = input("Enter your choice [1-5]: ")
    # Add contact
    if user_input == "1":
        function.add_contact(contacts)
        function.save_contact(contacts)
        print("New contact has add to contact book.")
    # Show contact
    elif user_input == "2":
        if not contacts:
            print("you don't have contact list.\n")
        else:
            print("----- Contact List -----")
            function.view_contact(contacts)
            print("------------------------\n")
    # Search Contact
    elif user_input == "3":
        matching_contact = function.search_contact(contacts)
        if not matching_contact:
            print("Contact not found.")
        else:
            print(f"----- Found {len(matching_contact)} contact Lists -----")
            function.view_contact(matching_contact)
            print("------------------------\n")
    # Remove Contact
    elif user_input == "4":
        if not contacts:
            print("you don't have contact list.")
        else:
            print("----- Remove contact List -----")
            function.view_contact(contacts)
            remove_item = input("Enter number of list you want to remove: ")
            try:
                remove_index = int(remove_item)
            except ValueError:
                print("Invalid input. Please enter a number.\n")
            contact = function.remove_contact(contacts, remove_index)
            print(f"Name {contact['name']} has been remove from contact book.")
            function.save_contact(contacts)
            print("------------------------\n")
    # Exit
    elif user_input == "5":
        print("Exiting the contact book.")
        function.save_contact(contacts)
        break
    else:
        print("Invalid choice. Please try again.\n")
