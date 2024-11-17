contacts = {}
while True:
    print("\n Contact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact Numbers")
    print("7. Exit")

    choice = input("Enter your choice(1-7):")

    if choice == '1':
        name = input("Enter the contact name :")
        if name in contacts :
            print(f"Contact Name '{name}' is already in contact list")
        else:
            mobile = input("Enter the Phone Number📞:")
            Email = input("Enter Email I'd :")
            address = input(f"Enter the Address of '{name}' :")
            contacts[name] = {'Phone Number': mobile , 'Email' : Email , 'Address' : address}
            print(f"Contact Details of {name} added successfully😊!")

    elif choice == '2':
        name = input("enter the contact name to view :")
        if name in contacts:
            contact = contacts[name]
            print(f"Name : {name} ,\nPhone Number : {mobile}, \nAddress : {address} ")
        else:
            print("Contact not found in list😞!")

    elif choice == '3':
        name = input("enter the name for updating :")
        if name in contacts:
            mobile = input("Enter the Updated Phone Number📞:")
            Email = input("Enter Updated Email I'd :")
            address = input(f"Enter the Updated Address of '{name}' : ")
            contacts[name] = {'Phone Number': mobile , 'Email' : Email , 'Address' : address}
        else:
            print("Contact not found in list😞!")

    elif choice == '4':
        name = input("enter the name for deleting :")
        if name in contacts :
            del contacts[name] 
            print(f"contact name {name} has been deleted successfully👍!")  
        else:
            print("Contact not found in list😞!") 

    elif choice == '5':
        search_name = input("enter the contact name to be searched :")
        found = False
        for name, contact in contacts.item():
            if search_name.lower() in name.lower():
                print(f" found ----- Name:{name}, Email:{Email}, Mobile Number:{mobile}")
                found = True
            if not found:
                print("no contact found with that name") 

    elif choice == '6':
        print(f"Total contacts in your list is {len(contacts)}")

    elif choice == '7':
        print("Exiting the program")

    else:
        print("Invalid Input")                   






