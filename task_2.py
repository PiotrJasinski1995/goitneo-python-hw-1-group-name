def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    # Check number of arguments
    if len(args) != 2:
        return 'Wrong number of arguments. Try again!'
    else:
        name, phone = args

        # Check if key exists
        if contacts.get(name, False):
            return 'Contact already exists! If you want to change contact, use "change" command.'
        else:
            contacts[name] = phone
            return 'Contact added.'
        
def change_contact(args, contacts):
    # Check number of arguments
    if len(args) != 2:
        return 'Wrong number of arguments. Try again!'
    else:
        name, phone = args

        # Check if key exists
        if contacts.get(name, False):
            contacts[name] = phone
            return 'Contact changed.'
        else:
            return 'Contact does not exists! If you want to add contact, use "add" command.'
        
def get_phone(args, contacts):
    # Check number of arguments
    if len(args) != 1:
        return 'Wrong number of arguments. Try again!'
    else:
        (name, ) = args

        # Check if key exists
        if contacts.get(name, False):
            return f'Phone number for {name}: {contacts[name]}'
        else:
            return 'Contact does not exists! If you want to add contact, use "add" command.'
        
def get_all(args, contacts):
    # Check number of arguments
    if len(args) != 0:
        return 'You should not put any arguments in "all" command!'
    if not contacts:
        return 'No contacts in phonebook!!!'
    else:
        contact_name = 'Contact'

        # Calculate max width of contact column
        max_key_len = max(len(key) for key in contacts)
        max_key_len = len(contact_name) if len(contact_name) > max_key_len else max_key_len
        max_key_len = max_key_len + 1 if not max_key_len % 2 else max_key_len

        # Calculate max width of phone number column
        phone_name = 'Phone'
        max_contact_len = max(len(contacts[key]) for key in contacts)
        max_contact_len = len(phone_name) if len(phone_name) > max_contact_len else max_contact_len
        max_contact_len = max_contact_len + 1 if not max_contact_len % 2 else max_contact_len

        # Prepare separator for rows
        space_width = 4
        separator = f'|{'-' * ((max_key_len + max_contact_len) + 2 * space_width + 1)}|\n'

        # Print phonebook
        # Print title
        contacts_string = f'\n{separator}'
        title_name = 'PHONEBOOK'
        pound_sign_string_len = int((len(separator) - len(title_name)) / 2)
        contacts_string += f'| {'#' * (pound_sign_string_len - 3)} {title_name} {'#' * (pound_sign_string_len - 3)} |\n'
        contacts_string += separator
        
        # Print column names
        contacts_string += '|{name:^{name_width}}|{phone:^{phone_width}}|\n'.format(name=contact_name, name_width=max_key_len + space_width, phone=phone_name, phone_width=max_contact_len + space_width)
        contacts_string += separator * 2

        # Print contacts
        for key in contacts:
            contacts_string += '|{name:^{name_width}}|{phone:^{phone_width}}|\n'.format(name=key, name_width=max_key_len + 4, phone=contacts[key], phone_width=max_contact_len + 4)
            contacts_string += separator

        return contacts_string

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()