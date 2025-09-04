"""
Address Book Application Entry Point
"""

from address_book import AddressBook as Contact
import addrbk_user_input as input_module


def main():
    """Main application entry point"""
    print("Starting Address Book Application...")
    # Application logic

    # Create a dictionary from user input
    contact_data = {
        "first_name": input_module.user_entry_first_name(),
        "last_name": input_module.user_entry_last_name(),
        "birthday": input_module.user_entry_birthday(),
        "email": input_module.user_entry_email(),
        "street_address": input_module.user_entry_street_address(),
        "city": input_module.user_entry_city(),
        "state": input_module.user_entry_state(),
        "country": input_module.user_entry_country(),
        "zip_code": input_module.user_entry_zip_code(),
        "phone": input_module.user_entry_phone()
    }

    # Create instance from user data
    try:
        new_contact = Contact(**contact_data)

        # Verify instantiation and display
        print("\n" + "="*50)
        print("Contact successfully created.")
        print("="*50)
        print(new_contact)

    except ValueError as e:
        print(f"Error creating contact: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


if __name__ == "__main__":
    main()
