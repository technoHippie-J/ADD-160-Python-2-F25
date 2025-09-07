# Methods for user input
"""The methods used for entering user input. Input constraints implemented where applicable"""


def user_entry_first_name():
    complete = False
    while not complete:
        print("*- Please enter the contact's first name: \n")
        new_first_name = input("Enter: ").strip()
        first_name = new_first_name
        complete = True
        print(f"First name set to: {first_name}\n")
        return first_name


def user_entry_last_name():
    complete = False
    while not complete:
        print("*- Please enter the contact's last name: \n")
        new_last_name = input("Enter: ").strip()
        last_name = new_last_name
        complete = True
        print(f"Last name set to: {last_name}\n")
        return last_name


def user_entry_birthday():
    complete = False
    while not complete:
        print(
            "*- Please enter the contact's birthday in the following format:\n\n"
            "          YYYY/MM/DD\n"
        )
        new_birthday = input("Enter: ").strip()
        birthday = new_birthday
        complete = True
        print(f"Birthday set to: {birthday}\n")
        return birthday


def user_entry_email():
    complete = False
    while not complete:
        print("*- Please enter the contact's email: \n")
        new_email = input("Enter: ").strip()
        email = new_email
        complete = True
        print(f"Email set to: {email}\n")
        return email


def user_entry_street_address():
    complete = False
    while not complete:
        print("*- Please enter the contact's street address: \n")
        new_street_address = input("Enter: ").strip()
        street_address = new_street_address
        complete = True
        print(f"Street address set to: {street_address}\n")
        return street_address


def user_entry_city():
    complete = False
    while not complete:
        print("*- Please enter the contact's city: \n")
        new_city = input("Enter: ").strip()
        city = new_city
        complete = True
        print(f"City set to: {city}\n")
        return city


def user_entry_state():
    complete = False
    while not complete:
        print("*- Please enter the contact's state: \n")
        new_state = input("Enter: ").strip()
        state = new_state
        complete = True
        print(f"State set to: {state}\n")
        return state


def user_entry_country():
    complete = False
    while not complete:
        print("*- Please enter the contact's three-letter country code: \n")
        new_country = input("Enter: ").strip()
        country = new_country
        complete = True
        print(f"Country set to: {country}\n")
        return country


def user_entry_zip_code():
    complete = False
    while not complete:
        print("*- Please enter the contact's zip code: \n")
        new_zip_code = input("Enter: ").strip()
        zip_code = new_zip_code
        complete = True
        print(f"Zip code set to: {zip_code}\n")
        return zip_code


def user_entry_phone():
    complete = False
    while not complete:
        print(
            "*- Please enter the contact's phone number in the following format, including dashes:\n\n"
            "          xxx-xxx-xxxx\n"
        )
        new_phone = input("Enter: ").strip()
        phone = new_phone
        complete = True
        print(f"Phone number set to: {phone}\n")
        return phone
