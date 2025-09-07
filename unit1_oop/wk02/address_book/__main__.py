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


entry_01 = Contact(
    first_name="Rick",
    last_name="Deckard",
    birthday="1979/01/08",
    email="bladerunner.rd@lapd.gov",
    street_address="Apt #9732",
    city="Los Angeles",
    state="CA",
    country="USA",
    zip_code="90009",
    phone="213-082-1119"
)

entry_02 = Contact(
    first_name="Cassandra",
    last_name="Anderson",
    birthday="1987/09/07",
    email="psi.anderson@mc1-justice.gov",
    street_address="Peach Trees Apt #0907",
    city="New York",
    state="NY",
    country="USA",
    zip_code="10001",
    phone="212-907-1212"
)

entry_03 = Contact(
    first_name="Max",
    last_name="Rockatansky",
    birthday="1979/04/12",
    email="mfp.max@mfp.gov.au",
    street_address="MFP Highway Patrol #44",
    city="Melbourne",
    state="Victoria",
    country="AUS",
    zip_code="03000",
    phone="613-412-1979"
)

entry_04 = Contact(
    first_name="Shaun",
    last_name="Riley",
    birthday="1978/09/24",
    email="shaun.riley@foree.co.uk",
    street_address="Flat #2B, 42 Nelson Road",
    city="London",
    state="N/A",
    country="ENG",
    zip_code="NW5 2QH",
    phone="020-924-2004"
)


# Functions

def menu_loop():
    active = True
    while active == True:
        selection = None
        print(
            ("\n" * 1) + "Select Option:" + ("\n" * 2) +
            f"1) Create User               (Enter [1])" + "\n"
            f"2) Create Contact            (Enter [2])" + "\n"
            f"3) Run Class Assignment      (Enter [3])" + "\n"
            f"4) Quit                      (Enter [4])" + "\n"
        )

        try:
            selection = int(input("Choice: "))
            if selection in (1, 2, 3, 4):
                print(f"Thank you for entering {selection}.\n")
            else:
                raise ValueError("Entry must be [1], [2], [3], or [4]")
        except ValueError as e:
            print(f"Invalid Entry: {e}")
        except Exception as e:
            print(f"Unknown error occurred: {e}")

        if selection == 1:
            print("This selection is not implemented yet."+"\n")
            time.sleep(2)
            if selection != None:
                selection = None
        elif selection == 2:
            try:
                print(f"Starting contact creation...")
                startup = (
                    ".\n"
                    ".\n"
                    ".\n"
                    ".\n"
                )
                for line in startup.splitlines():
                    print(line)
                    time.sleep(0.25)
                create_contact()
            except Exception as e:
                print(f"Encountered error: \n{e}")
        elif selection == 3:
            time.sleep(0.5)
            try:
                first = (
                    f"1. Create and print four contact entries:\n"
                    f"   -(Two-fer: Print 4 instantiations and)-\n"
                    f"   -(Magic Method Implementation of __str__)-\n"
                    f"   =========================================\n\n"
                    f"{entry_01}\n\n"
                    f"{entry_02}\n\n"
                    f"{entry_03}\n\n"
                    f"{entry_04}\n\n"
                )
                for line in first.splitlines():
                    print(line)
                    time.sleep(0.25)
            except Exception as e:
                print(f"An error occurred: {e}")
            time.sleep(0.5)
            try:
                second = (
                    f"\n2. Compare two entries to see if they are the same contact:\n"
                    f"   -(Magic Method Implementation of __eq__)-\n"
                    f"   ========================================================\n\n"
                    # Formatted to show intentional magic method usage
                    # Could also be print(entry_01 == entry_03)
                    # Magic method provides type validation
                    f"Is {entry_01.first_name} {entry_01.last_name} the same person as {entry_03.first_name} {entry_03.last_name}\n\n"
                    f"{Contact.__eq__(entry_01, entry_03)}"
                )
                for line in second.splitlines():
                    print(line)
                    time.sleep(0.25)
            except Exception as e:
                print(f"An error occurred: {e}")
            time.sleep(0.5)
            try:
                print(
                    f"\n3. Contact sorting algorithm:\n"
                    f"   -(Magic Method Implementation of __lt__)-\n"
                    f"   -(Magic method provides type validation)-\n"
                    f"   =========================================\n\n"
                )
                # Sort using AddressBook.__lt__ (using _sort_key)
                Contact._instances.sort()
                # Print results
                for entry in Contact._instances:
                    show = str(entry)
                    for line in show.splitlines():
                        print(line)
                        time.sleep(0.25)
                    print("\n" * 2)

            except Exception as e:
                print(f"An error occurred: {e}")

                # Create Dictionary for contact_data
        if selection == 4:
            print("\nThank you, goodbye.")
            time.sleep(2)
            exit()


def create_contact():
    # TODO: this just creates an instance, but does not save it to a file, or generate iterative variable names.
    # One or the other should be implemented so the contact can then be recalled later.

    while True:
        first = input_module.user_entry_first_name()
        last = input_module.user_entry_last_name()
        email = input_module.user_entry_email()
        phone = input_module.user_entry_phone()
        try:
            new_contact = Contact(
                first_name=first, last_name=last, email=email, phone=phone)
            break
        except ValueError as e:
            print(
                f"Invalid name: {e}\n"
                f"Please re-enter the name fields.\n\n"
            )

    optional_fields = [
        ("birthday", input_module.user_entry_birthday),
        ("street_address", input_module.user_entry_street_address),
        ("city", input_module.user_entry_city),
        ("state", input_module.user_entry_state),
        ("country", input_module.user_entry_country),
        ("zip_code", input_module.user_entry_zip_code)
    ]

    for attr, input_fn in optional_fields:
        while True:
            try:
                entry = input_fn()
                setattr(new_contact, attr, entry)
                break
            except ValueError as e:
                print(f"Invalid {attr}: Please try again.\n")
                return None
            except Exception as e:
                print(f"Unexpected error: {e}")
                return None

    print("\n\n" + ("=" * 50))
    print(
        f"Contact successfully created.\n"
        f"Contact data entered as follows:\n\n"
        f"{new_contact}"
    )
    print("="*50)

    return new_contact

    # TODO: Verify if user wants to add the contact to the addrbk_user**.json file, located in the user folder. Do some research to figure out how to do this properly. I know that .json is useful for structured data, but haven't looked into specifics yet. On the list, depending on time.

# --- Main Program Loop ---


def main():
    """Main application entry point"""
    # Startup process to give user sense of agency and control over program

    startup = (
        ("\n" * 3) +
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
        input("Please press enter to continue...")
        print("\n\n\n")
        go = True

    menu_loop()


if __name__ == "__main__":
    main()
