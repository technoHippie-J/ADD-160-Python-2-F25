"""
-Objective-

Create a Python function that simulates a conference sign-up process, accepting any number of participants and their contact details. The function should print a summary of the participants and their contact details.


-Assignment Instructions-

1. Create a Python function named conference_signup that accepts any number of participant names using *args and their contact details (email and phone) using **kwargs.

2. Inside the function, print a summary of the participants and their contact details in a clear and organized format.

3. Ensure that your function handles cases where no participants or no contact details are provided gracefully.

4. Test your function with sample data to ensure it works correctly.


-Expected Output-

When you run the sample code, the output should look like this:

Conference Participants and Their Contact Details:
--------------------------------------------------
Name: Alice
Email: alice@example.com
Phone: 123-456-7890
--------------------------------------------------
Name: Bob
Email: bob@example.com
Phone: 987-654-3210
--------------------------------------------------
Name: Charlie
Email: charlie@example.com
Phone: N/A
--------------------------------------------------

-Submission Instructions-

Submit your completed assignment by uploading the Python script to your course directory on GitHub, hand in the link to your repository.

"""


"""List of Attendees (directory for contacts{})"""
names = ["Alice", "Bob", "Charlie"]
"""Contacts directory to be unpacked"""
contacts = {
    "Alice": {"email": "alice@example.com", "phone": "123-456-7890"},
    "Bob": {"email": "bob@example.com", "phone": "987-654-3210"},
    "Charlie": {"email": "charlie@example.com", "phone": ""}
}

"""
Main Logic
    - if names isn't empty:
    - get name[i] in names
    - get email for name
    - get phone for name
    - print out in desired format
    - loop back, repeat through each i in list
"""


def conference_signup(*names, **contacts):
    print(
        f"\n\nConference Participants and Their Contact Details:\n"
        f"--------------------------------------------------"
    )
    if names:
        for person in names:
            record = contacts.get(person, {})
            email = record.get("email") or "N/A"
            phone = record.get("phone") or "N/A"
            print(
                f"Name:  {person}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"--------------------------------------------------"
            )
    else:
        print("No participants found.")
    print("\n")


def main():
    conference_signup(*names, **contacts)


if __name__ == "__main__":
    main()
