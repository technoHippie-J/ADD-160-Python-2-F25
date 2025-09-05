"""
Address Book Application Entry Point
"""

# TODO: Instead of importing AddressBook as Contact
from address_book import AddressBook as Contact
import addrbk_user_input as input_module
import time

#       The below is a mix of code/pseudocode (kinda)
#
# TODO: Implement a user creation/login module:
#
#       install_type = {Check install.json -> line [TBD] -> install_type}
#       force_set_user_id = {Check user/{user_dir}/settings.json ->
#                               line [TBD] -> force_set_True/False}
#       applicable = False
#       if install_type == org or force_set_user_id = True:
#           applicable = True
#       Get first_name
#           str, strip validation
#       Get last_name
#           str, strip validation
#       Get user_id (optional; if applicable == True)
#           str, strip, len, isdigit(var_pos; or letters or position
#           formatting specific to org)
#       Set user_ = {
#           "last_name": {last_name}
#           "first_name": {first_name}
#           "user_id":{if applicable != False: user_id; else: return None}
#       }
#       Write user_ to {user/{user_dir}/settings.json}
#
#
#
# TODO: Implement a file name generator:
#
#       user_id = {Check user/{user_dir}/settings.json -> line [TBD] ->
#                   if user_id: return user_id; else: return None}
#       f_name = {Check user/{user_dir}/settings.json -> line [TBD] ->
#                   last_name}
#       l_name = {Check user/{user_dir}/settings.json -> line [TBD] ->
#                   first_name}
#
#   -the idea of {count} in the lines below is an alternative to the
#    {user_id} field above, and if the chosen implementation, the above
#    would include similar logic for generation:
#
#       count = (
#           if [directory:{fname}_{l_name}_{count}] in [directory]:
#               counter = {count}
#               counter += 1
#               return counter
#       )
#       file_name_template = str(f"({f_name}+{l_name})_{count}")
#

# --- Pre-Instantiated Object Examples ---
"""Instanced [Objects] of the AddressBook [Class]"""


entry_01 = Contact(first_name="Rick", last_name="Deckard", birthday="1979/01/08",
                   email="bladerunner.rd@lapd.gov", street_address="Apt #9732", city="Los Angeles", state="CA", country="USA", zip_code="90009", phone="213-082-1119")

entry_02 = Contact(first_name="Cassandra", last_name="Anderson", birthday="1987/09/07",
                   email="psi.anderson@mc1-justice.gov", street_address="Peach Trees Apt #0907", city="New York", state="NY", country="USA", zip_code="10001", phone="212-907-1212")

entry_03 = Contact(first_name="Max", last_name="Rockatansky", birthday="1979/04/12",
                   email="mfp.max@mfp.gov.au", street_address="MFP Highway Patrol #44", city="Melbourne", state="Victoria", country="AUS", zip_code="03000", phone="613-412-1979")

entry_04 = Contact(first_name="Shaun", last_name="Riley", birthday="1978/09/24",
                   email="shaun.riley@foree.co.uk", street_address="Flat #2B, 42 Nelson Road", city="London", state="N/A", country="ENG", zip_code="NW5 2QH", phone="020-924-2004")


# --- Main Program Loop ---
def main():
    """Main application entry point"""
    # Startup process to give user sense of agency and control over program

    startup = (
        "Starting Address Book Entry...\n"
        ".\n"
        ".\n"
        ".\n"
        ".\n"
        ".\n"
        ".\n"
        ".\n"
    )

    for line in startup.splitlines():
        print(line)
        time.sleep(0.25)

    go = False
    while go == False:
        input("Please press any key to continue...")
        print("\n\n\n")
        go = True

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
        # ** unpacks dictionary to populate class attributes
        new_contact = Contact(**contact_data)

        # Verify instantiation and display
        print("\n" + "="*50)
        print(
            f"Contact successfully created.\n"
            f"Contact data entered as follows:\n\n"
            f"{new_contact}"
        )
        print("\n" + "="*50)

    except ValueError as e:
        print(f"Error creating contact: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

    # TODO: Verify if user wants to add the contact to the addrbk_user**.json file, located in the user folder. Do some research to figure out how to do this properly. I know that .json is useful for structured data, but haven't looked into specifics yet. On the list, depending on time.


if __name__ == "__main__":
    main()
