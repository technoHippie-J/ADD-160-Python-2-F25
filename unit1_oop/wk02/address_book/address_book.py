"""
Lesson: Creating a Custom Address Book Class in Python

Objective: By the end of this lesson, students will be able to write a custom class for an address book that includes getter and setter methods for various attributes, utilizes at least three magic methods, and includes docstrings for documentation.

Directions
1. Create the Address Book Class
    - Create a class named AddressBook with the following attributes:

-first_name
-last_name
-birthday
-email
-street_address
-city
-state
-zip
-phone

    - Include getter and setter methods for each attribute.

2. Implement Magic Methods
    - Implement at least three magic methods. Some possibilities include:

__str__ - to nicely print the information about each person.
__repr__ - to provide an official string representation of the object.
__eq__ - to compare two AddressBook objects for equality.

3. Write Docstrings
    - Include docstrings for your class and its methods to provide documentation. Use the following template:

'''
Class to represent an address book entry.

Attributes:
   include attribute details here

Methods:
   include method details here
'''

4. Create Instances and Print Information
    - Create at least four instances of the AddressBook class, each representing a different person. Implement a method to nicely print all the information about each person.

Estimated Time for Completion
Estimated time: 2 hours

Sample Output
The output of your program should look similar to this:

First Name: John
Last Name: Doe
Birthday: 01/01/1990
Email: john.doe@example.com
Street Address: 123 Main St
City: Anytown
State: NY
Zip: 12345
Phone: 555-555-5555

First Name: Jane
Last Name: Smith
Birthday: 02/02/1985
Email: jane.smith@example.com
Street Address: 456 Elm St
City: Othertown
State: CA
Zip: 67890
Phone: 555-555-1234

First Name: Emily
Last Name: Johnson
Birthday: 03/03/1975
Email: emily.johnson@example.com
Street Address: 789 Oak St
City: Sometown
State: TX
Zip: 11111
Phone: 555-555-6789

First Name: Michael
Last Name: Brown
Birthday: 04/04/1965
Email: michael.brown@example.com
Street Address: 101 Pine St
City: Anycity
State: FL
Zip: 22222
Phone: 555-555-2468

---------------------------------------------------------------------------------

Notes during the process:

1. .casefold()

Found this while looking into magic methods to use as a string method that's similar to .lower(), but is "stronger" and "more aggressive", and is designed to work with Unicode instead of ASCII, which is what .lower() focuses on primarily.

2. @property / @<property>.setter / @<property.deleter

I had forgotten how to implement setters and getters, and during research, I discovered deleters, which were not covered in the previous class. Through looking into deleters, I found the property decorator. This seemed like the best approach for an address book because presumably it would serve as a module in a larger, user-facing application, and the use of the property decorator would give more internal control to protect from user error and malicious attacks.

This also changed the way I view class attributes, as the attribute itself can call a method that protects the attribute using the logic written in the method.

3. I obviously learned a lot more than this, but at a certain point, dev became a bit chaotic and I forgot to continue adding here

4. My docstrings are not consistent across implementations. This assignment took me forever (my own fault, went too deep), so my goal was just to ensure docstrings were placed where I could find it appropriate for them to be, but did not make their formatting consistent

"""


# --- Classes ---
"""[Classes] for the address_book.py program"""


class AddressBook:
    """AddressBook [Class] for address book entries"""
    _instances = []

    def __init__(self, first_name, last_name, birthday=None, email=None, street_address=None, city=None, state=None, country=None, zip_code=None, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.street_address = street_address
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code
        self.phone = phone
        AddressBook._instances.append(self)

    # --- Methods ---
    """[Methods] for the AddressBook [Class]"""

    def _sort_key(self):
        """Sorting key helper method"""
        return (
            (self.last_name or "").casefold(),
            (self.first_name or "").casefold(),
            (self.birthday or ""),
            (self.email or "").casefold(),
            (self.phone or "")
        )

    def __eq__(self, other):
        """[Method] comparing the _sort_key of two entries to determine if they are the same contact"""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._sort_key() == other._sort_key()

    def __lt__(self, other):
        """[Method] comparing the _sort_key of two entries to determine if self is less than other"""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._sort_key() < other._sort_key()

    def __str__(self):
        """[Method] that outputs a formatted string, displaying the instance's [Attributes] in a clean, structured way."""
        return (
            f"First Name:        {self.first_name}\n"
            f"Last Name:         {self.last_name}\n"
            f"Birthday:          {self.birthday}\n"
            f"Email:             {self.email}\n"
            f"Street Address:    {self.street_address}\n"
            f"City:              {self.city}\n"
            f"State:             {self.state}\n"
            f"Country:           {self.country}\n"
            f"Zip Code:          {self.zip_code}\n"
            f"Phone Number:      {self.phone}\n"
        )

    # ***** The following section was moved to separate file.
    # ***** Kept and commented out for historical context.
    # ***** This would be removed if this was a production deliverable.

    # # Methods for user input

    # """The methods used for entering user input. Input constraints implemented where applicable"""

    # def user_entry_first_name(self):
    #     complete = False
    #     while not complete:
    #         print("Please enter the contact's first name: \n")
    #         new_first_name = input("Enter: ").strip()
    #         try:
    #             self.first_name = new_first_name
    #             complete = True
    #             print(f"First name set to: {self.first_name}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_last_name(self):
    #     complete = False
    #     while not complete:
    #         print("Please enter the contact's last name: \n")
    #         new_last_name = input("Enter: ").strip()
    #         try:
    #             self.last_name = new_last_name
    #             complete = True
    #             print(f"Last name set to: {self.last_name}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_birthday(self):
    #     complete = False
    #     while not complete:
    #         print(
    #             "Please enter the contact's birthday in the following format:\n\n"
    #             "YYYY/MM/DD\n\n"
    #         )
    #         new_birthday = input("Enter: ").strip()
    #         try:
    #             self.birthday = new_birthday
    #             complete = True
    #             print(f"Birthday set to: {self.birthday}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_email(self):
    #     complete = False
    #     while not complete:
    #         print("Please enter the contact's email: \n")
    #         new_email = input("Enter: ").strip()
    #         try:
    #             self.email = new_email
    #             complete = True
    #             print(f"Email set to: {self.email}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_street_address(self):
    #     complete = False
    #     while not complete:
    #         print("Please enter the contact's street address: \n")
    #         new_street_address = input("Enter: ").strip()
    #         try:
    #             self.street_address = new_street_address
    #             complete = True
    #             print(f"Street address set to: {self.street_address}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_city(self):
    #     complete = False
    #     while not complete:
    #         print("Please enter the contact's city: \n")
    #         new_city = input("Enter: ").strip()
    #         try:
    #             self.city = new_city
    #             complete = True
    #             print(f"City set to: {self.city}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_state(self):
    #     complete = False
    #     while not complete:
    #         print("Please enter the contact's state: \n")
    #         new_state = input("Enter: ").strip()
    #         try:
    #             self.state = new_state
    #             complete = True
    #             print(f"State set to: {self.state}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_country(self):
    #     complete = False
    #     while not complete:
    #         print("Please enter the contact's three-letter country code: \n")
    #         new_country = input("Enter: ").strip()
    #         try:
    #             self.country = new_country
    #             complete = True
    #             print(f"Country set to: {self.country}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_zip_code(self):
    #     complete = False
    #     while not complete:
    #         print("Please enter the contact's zip code: \n")
    #         new_zip_code = input("Enter: ").strip()
    #         try:
    #             self.zip_code = new_zip_code
    #             complete = True
    #             print(f"Zip code set to: {self.zip_code}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

    # def user_entry_phone(self):
    #     complete = False
    #     while not complete:
    #         print(
    #             "Please enter the contact's phone number in the following format, including dashes:\n\n"
    #             "xxx-xxx-xxxx\n\n"
    #         )
    #         new_phone = input("Enter: ").strip()
    #         try:
    #             self.phone = new_phone
    #             complete = True
    #             print(f"Phone number set to: {self.phone}")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #             print("Please try again.\n")

# --- Getters ---
    """[Getters] for the AddressBook [Class]"""

    @property
    def first_name(self):
        """[Getter] for the first_name [Attribute]"""
        return self._first_name

    @property
    def last_name(self):
        """[Getter] for the last_name [Attribute]"""
        return self._last_name

    @property
    def birthday(self):
        """[Getter] for the birthday [Attribute]"""
        return self._birthday

    @property
    def email(self):
        """[Getter] for the email [Attribute]"""
        return self._email

    @property
    def street_address(self):
        """[Getter] for the street_address [Attribute]"""
        return self._street_address

    @property
    def city(self):
        """[Getter] for the city [Attribute]"""
        return self._city

    @property
    def state(self):
        """[Getter] for the state [Attribute]"""
        return self._state

    @property
    def country(self):
        """[Getter] for the country [Attribute]"""
        return self._country

    @property
    def zip_code(self):
        """[Getter] for the zip_code [Attribute]"""
        return self._zip_code

    @property
    def phone(self):
        """[Getter] for the phone [Attribute]"""
        return self._phone

    # --- Setters ---
    """[Setters] for the AddressBook [Class]"""

    @first_name.setter
    def first_name(self, new_first_name):
        """[Setter] for the first_name [Attribute] with validation."""
        # Check if new_first_name is None or an empty string
        if new_first_name is None or new_first_name == "":
            raise ValueError("First name cannot be empty.")

        # Check if input is a string
        if not isinstance(new_first_name, str):
            raise ValueError("First name must be a string.")

        # Strip the validated string of whitespace
        new_first_name = new_first_name.strip()

        # Verify whitespace stripping
        if new_first_name == "":
            raise ValueError("First name cannot be only whitespace.")

        # Assign new value
        self._first_name = new_first_name

    @last_name.setter
    def last_name(self, new_last_name):
        """[Setter] for the first_name [Attribute] with validation."""
        # Check if last_name is None or an empty string
        if new_last_name is None or new_last_name == "":
            raise ValueError("Last name cannot be empty.")

        # Check if input is a string
        if not isinstance(new_last_name, str):
            raise ValueError("Last name must be a string.")

        # Strip the validated string of whitespace
        new_last_name = new_last_name.strip()

        # Verify whitespace stripping
        if new_last_name == "":
            raise ValueError("Last name cannot be only whitespace.")

        # Assign new value
        self._last_name = new_last_name

    @birthday.setter
    # FIXME (FIXED) - validation does not trigger until the end of instantiation.
    # I was able to enter forbidden characters, but did not receive an error until going through each user input.
    # The error output is: "Error creating contact: Birthday must be in YYYY/MM/DD format (10 characters)."
    # This indicates that validation did raise exceptions at the birthday field (first with char reqs), but continued the process.
    # The process has been tested to work properly with correct inputs.
    def birthday(self, new_birthday):
        """
        [Setter] for the birthday [Attribute] with validation. Creates year, month, and day lists to check their positions in the string.
        Checks:
            - Is new_birthday a string?
            - Is the length exactly 10 characters? ((YYYY = 4) + (MM = 2) + (DD = 2) + ('/' * 2))
            - Are positions 4 and 7 slashes?
            - Are the year, month, and day positions digits?
            - Are the month and day positions valid ranges?
        If all of the above are true, new_birthday is assigned to self._birthday
        """
        # Check if blank or None, then return
        if new_birthday is None or new_birthday == "":
            self._birthday = None
            return

        # Check if input is a string
        if not isinstance(new_birthday, str):
            raise ValueError("Birthday must be a string.")

        # Strip the validated string of whitespace
        new_birthday = new_birthday.strip()

        # Verify whitespace stripping
        if new_birthday == "":
            raise ValueError("Birthday cannot be only whitespace")

        # Check if new_birthday is entered, then if length is exactly 10 characters
        if len(new_birthday) != 10:
            raise ValueError(
                "Birthday must be in YYYY/MM/DD format (10 characters).")

        # Check if new_birthday is entered, then if positions 4 and 7 are slashes
        if new_birthday[4] != "/" or new_birthday[7] != "/":
            raise ValueError(
                "Birthday must use '/' as separators. (YYYY/MM/DD)")

        # Check if new_birthday is entered, then if year, month, day position are all digits
        year = new_birthday[0:4]    # Positions 0,1,2,3
        month = new_birthday[5:7]   # Positions 5,6
        day = new_birthday[8:10]    # Positions 8,9

        if not year.isdigit():
            raise ValueError("Year must be 4 digits.")
        if not month.isdigit():
            raise ValueError("Month must be 2 digits.")
        if not day.isdigit():
            raise ValueError("Day must be 2 digits.")

        # Check if new_birthday is entered, then if month and day are valid ranges
        month_num = int(month)
        day_num = int(day)
        if month_num < 1 or month_num > 12:
            raise ValueError("Month must be between 01 and 12.")
        if day_num < 1 or day_num > 31:
            raise ValueError("Day must be between 01 and 31.")
        if month == "02":
            year_num = int(year)
            # Leap Year calculation
            if (year_num % 4 == 0 and year_num % 100 != 0) or (year_num % 400 == 0):
                days = 29     # Leap Year
            else:
                days = 28     # Regular Year
            if day_num > days:
                raise ValueError(f"February only has {days} in {year}.")

        if month in ("04", "06", "09", "11") and day_num > 30:
            raise ValueError(f"{month} only has 30 days.")

        self._birthday = new_birthday

    @email.setter
    def email(self, new_email):
        """
        [Setter] for the email [Attribute] with validation.
        Checks if entry is both a string and greater than 0 in length, then assigns new_email to self._email.
        """
        # Check if blank or None, then return
        if new_email is None or new_email == "":
            self._email = None
            return

        # Check if input is a string
        if not isinstance(new_email, str):
            raise ValueError("Email must be a string.")

        # Strip the validated string of whitespace
        new_email = new_email.strip()

        # Verify whitespace stripping
        if new_email == "":
            raise ValueError("Email cannot be only whitespace.")

        self._email = new_email

    @street_address.setter
    def street_address(self, new_street_address):
        """[Setter] for the street_address [Attribute] with validation."""
        # Check if blank or None, then return
        if new_street_address is None or new_street_address == "":
            self._street_address = None
            return

        # Check if input is a string and not empty
        if not isinstance(new_street_address, str):
            raise ValueError("Street Address must be a string.")

        # Strip the validated string of whitespace
        new_street_address = new_street_address.strip()

        # Verify whitespace stripping
        if new_street_address == "":
            raise ValueError("Street Address cannot be only whitespace.")

        self._street_address = new_street_address

    @city.setter
    def city(self, new_city):
        """[Setter] for the city [Attribute] with validation."""
        # Check if blank or None, then return
        if new_city is None or new_city == "":
            self._city = None
            return

        # Check if input is a string
        if not isinstance(new_city, str):
            raise ValueError("City must be a string.")

        # Strip the validated string of whitespace
        new_city = new_city.strip()

        # Verify whitespace stripping
        if new_city == "":
            raise ValueError("City cannot be only whitespace.")

        self._city = new_city

    @state.setter
    def state(self, new_state):
        """[Setter] for the state [Attribute] with validation."""
        # Check if blank or None, then return
        if new_state is None or new_state == "":
            self._state = None
            return

        # Check if input is a string, then assign
        if not isinstance(new_state, str):
            raise ValueError("State must be a string.")

        # Strip the validated string of whitespace
        new_state = new_state.strip()

        # Verify whitespace stripping
        if new_state == "":
            raise ValueError("State cannot be only whitespace.")

        self._state = new_state

    @country.setter
    def country(self, new_country):
        """[Setter] for the country [Attribute] with validation."""
        # Check if blank or None, then return
        if new_country is None or new_country == "":
            self._country = None
            return

        # Check if input is a string
        if not isinstance(new_country, str):
            raise ValueError("Country must be a string.")

        # Strip the validated string of whitespace
        new_country = new_country.strip()

        # Verify whitespace stripping
        if new_country == "":
            raise ValueError("Country cannot be only whitespace.")

        self._country = new_country

    @zip_code.setter
    def zip_code(self, new_zip_code):
        """[Setter] for the zip_code [Attribute] with validation."""
        # Check if blank or None, then return
        if new_zip_code is None or new_zip_code == "":
            self._zip_code = None
            return

        # Check if new_zip_code is a string
        if not isinstance(new_zip_code, str):
            raise ValueError("Zip code must be a string.")

        # Strip the validated string of whitespace
        new_zip_code = new_zip_code.strip()

        # Verify whitespace stripping
        if new_zip_code == "":
            raise ValueError("Zip Code cannot be only whitespace.")

        # Check if country is not empty, and country is USA,
        # then if length is exactly 5 characters, then if all characters are digits
        # Personal Reminder Note: the use of "_country" is a string literal:
        #    - getattr(obj, name, default) takes the attribute name as a string
        country = getattr(self, "_country", None)
        if (country or "").upper() == "USA":
            if len(new_zip_code) != 5:
                raise ValueError(
                    "US zip codes must be exactly 5 digits in length.")
            if not new_zip_code.isdigit():
                raise ValueError("US zip codes must only include numbers.")

        self._zip_code = new_zip_code

    @phone.setter
    def phone(self, new_phone):
        """[Setter] for the phone [Attribute] with validation."""
        # Check if blank or None, then return
        if not self.email and (new_phone is None or new_phone == ""):
            '''
                FIXME (MAYBE FIXED in __main__.py -> create_contact() logic): 
                This currently breaks if the user does not enter a phone number after not 
                entering an email, as no while loop to return to input has been implemented
                This can be fixed by setting a flag in the input function, then writing a
                While loop, recursively calling itself until the user has entered a phone number. 
                Another implementation could be providing an option to enter a value of 'None'
                NOT AN ISSUE in currently implementation, but if ever called outside of native
                logic, it could raise.
            '''
            raise ValueError(
                f"Phone and email cannot both be empty.\n"
                f"Please enter a phone number.\n"
            )
        elif self.email and (new_phone is None or new_phone == ""):
            self._phone = None
            return

        # Check if input is a string
        if not isinstance(new_phone, str):
            raise ValueError("Phone Number must be a string.")

        # Strip the validated string of whitespace
        new_phone = new_phone.strip()

        # Verify whitespace stripping
        if new_phone == "":
            raise ValueError("Phone Number must not be only whitespace.")

        # Check if length is exactly 12 characters
        if len(new_phone) != 12:
            '''
                FIXME: Currently forces USA format. Fix it to use the country field to determine phone number format, then adjust field constraints to accommodate.
            '''
            raise ValueError(
                "Phone Number must be in XXX-XXX-XXXX format. (12 characters)")

        # Check if positions 3 and 7 are dashes
        if new_phone[3] != "-" or new_phone[7] != "-":
            raise ValueError(
                "Phone Number must use '-' as separators. (XXX-XXX-XXXX)")

        # Check if area, first, and last position are all digits
        phone_area = new_phone[0:3]    # Positions 0,1,2,
        phone_middle = new_phone[4:7]   # Positions 4,5,6
        phone_last = new_phone[8:12]    # Positions 8,9,10,11

        if not phone_area.isdigit():
            raise ValueError("The area code must be 3 digits.")
        if not phone_middle.isdigit():
            raise ValueError("The middle block of numbers must be 3 digits.")
        if not phone_last.isdigit():
            raise ValueError("The last block of numbers must be 4 digits.")

        self._phone = new_phone

    # --- Deleters ---
    """[Deleters] for the AddressBook [Class]"""

    @first_name.deleter
    def first_name(self):
        """[Deleter] for the first_name [Attribute]"""
        # Required field; do not allow deletion
        raise AttributeError(
            "First Name is required. Please delete the contact instead.")

    @last_name.deleter
    def last_name(self):
        """[Deleter] for the last_name [Attribute]"""
        # Required field; do not allow deletion
        raise AttributeError(
            "Last Name is required. Please delete the contact instead.")

    @birthday.deleter
    def birthday(self):
        """[Deleter] for the birthday [Attribute]"""
        self._birthday = None

    @email.deleter
    def email(self):
        """[Deleter] for the email [Attribute]"""
        # Either phone or email are required; do not allow deletion if email is 'None'
        if not self._phone:
            raise ValueError(
                "Cannot delete 'Email'... 'Phone Number' is missing.")
        else:
            self._email = None

    @street_address.deleter
    def street_address(self):
        """[Deleter] for the street_address [Attribute]"""
        self._street_address = None

    @city.deleter
    def city(self):
        """[Deleter] for the city [Attribute]"""
        self._city = None

    @state.deleter
    def state(self):
        """[Deleter] for the state [Attribute]"""
        self._state = None

    @country.deleter
    def country(self):
        """[Deleter] for the country [Attribute]"""
        self._country = None

    @zip_code.deleter
    def zip_code(self):
        """[Deleter] for the zip_code [Attribute]"""
        self._zip_code = None

    @phone.deleter
    def phone(self):
        """[Deleter] for the phone [Attribute]"""
        # Either phone or email are required; do not allow deletion if email is 'None'
        if not self._email:
            raise ValueError(
                "Cannot delete phone number. 'Email' is missing.")
        else:
            self._phone = None


# # --- Instantiated Objects ---
# ***moved to __main__.py***
# """Instanced [Objects] of the AddressBook [Class]"""


# entry_01 = AddressBook(first_name="Rick", last_name="Deckard", birthday="1979/01/08",
#                        email="bladerunner.rd@lapd.gov", street_address="Apt #9732", city="Los Angeles", state="CA", country="USA", zip_code="90009", phone="213-082-1119")

# entry_02 = AddressBook(first_name="Cassandra", last_name="Anderson", birthday="1987/09/07",
#                        email="psi.anderson@mc1-justice.gov", street_address="Peach Trees Apt #0907", city="New York", state="NY", country="USA", zip_code="10001", phone="212-907-1212")

# entry_03 = AddressBook(first_name="Max", last_name="Rockatansky", birthday="1979/04/12",
#                        email="mfp.max@mfp.gov.au", street_address="MFP Highway Patrol #44", city="Melbourne", state="Victoria", country="AUS", zip_code="03000", phone="613-412-1979")

# entry_04 = AddressBook(first_name="Shaun", last_name="Riley", birthday="1978/09/24",
#                        email="shaun.riley@foree.co.uk", street_address="Flat #2B, 42 Nelson Road", city="London", state="N/A", country="ENG", zip_code="NW5 2QH", phone="020-924-2004")


"""

To-Do's:

- Phone/Email dependency problem, potential fixes:
    - validation helper method
        def _validate_contact_info(self, email, phone):
            '''Helper to ensure at least one contact method exists'''
            if not email and not phone:
                raise ValueError("at least one contact method [email or phone] is required.")
    - two-phase initialization
        def __init__(self, first_name, last_name, **kwargs):
            # Store temp values
            temp_email = kwargs.get('email')
            temp_phone = kwargs.get('phone')

            # Validate contact requirement
            if not temp_email and not temp_phone:
                raise ValueError("At least one contact method required.")

            self.first_name = first_name # etc...
- More magic methods (__repr__)
- Docstring inconsistency cleanup and elaboration (later)

----------------------------------------------------------------

Later Goals:

- separate UI logic from data model (DONE)
    (user input methods pulled and placed in separate module; present now for completeness)
- tkinter integration
- international subclasses to handle phone/address/state-structure variance 
    (example: zip code only validates 5-digit codes or passes in not USA, 
    not 9-digit or international)
- integration into larger library of constructs
- additional modularity to enable repurposing for other use cases
- API-design language enhancement

"""
