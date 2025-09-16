"""
This module demonstrates the use of abstract classes and inheritance to model different types of customers
and their discount behaviors in a business context.
Classes:
    Customer (ABC): Abstract base class for customers, requiring discount and details methods.
    Retail (Customer): Represents a retail customer, with loyalty rewards logic.
    Enterprise (Customer): Represents an enterprise customer, with discount type management.
Functions:
    discount_message(msg, width): Formats a message with decorative lines for display.
    slow_tblok(tblok): Prints each line of a string with a delay for improved CLI UX.
    main(): Entry point for interactive demo and menu selection.
Demo Objects:
    retail_01, retail_02: Instances of Retail customers.
    ent_01, ent_02, ent_03: Instances of Enterprise customers.
Usage:
    Run the module to interactively demo customer discount and details logic.

*** This docstring was auto generated using "Right Click -> Generate Code -> Generate Docs"
"""

from abc import ABC, abstractmethod
import time

# ------ Line Delay Knob ------

PRINT_DELAY = 0.25

# ------ Return Messages ------ (had this idea late, would otherwise put return messages here)


def discount_message(msg, width):
    """
    Active Status None Return Message
    - Assign "=" times width to [line]
    - Return formatted message string with char
      decorations equal to length of msg str with name
    """
    line = ("=" * width)
    return f"\n{line}\n{msg}\n{line}"


# ------ Slow Text Helper ------


def slow_tblok(tblok):
    for line in tblok.splitlines():
        time.sleep(PRINT_DELAY)
        print(line)


# ------ Abstract Class ------


class Customer(ABC):
    """
    Abstract Customer Class:
    self.name - Customer Name
    self.cust_type - Customer Type
    self.active - Active Customer T/F (default = True)
    """

    def __init__(self, name, cust_type, active=True):
        self.name = name
        self.cust_type = cust_type
        self.active = active

    @abstractmethod
    def discount(self):
        """Discount Abstract Method (same purpose as add-ins in assignment instructions)"""
        pass

    @abstractmethod
    def details(self):
        """Details Abstract Method"""
        pass

# ------ Concrete Classes ------

# ------ Retail Customer ------


class Retail(Customer):
    """
    Retail Customer Sub-Class:
    self.name - Customer Name
    self.cust_type - Customer Type
    self.active - Active Customer T/F (default = True)
    self.loyalty - Loyalty Rewards Member T/F (default = False)
    """

    def __init__(self, name, cust_type, active=True, loyalty=False):
        super().__init__(name, cust_type, active)
        self.loyalty = loyalty

    def discount(self):
        """
        Discount Method
        - Check if active or inactive customer
        - If active -> User input -> Get program entry Y/N
            - If [Y]es, check if already a program member
            - If [Y]es but (not self.loyalty), set loyalty to True
            - If yes to both, alert user and make no change
            - If no to both, alert user and make no change
        - If inactive -> Alert user -> User input -> remove from program Y/N
            - If amend = [y], set loyalty to False and return message
            - If amend = [n], return no changes made

        UX CONTROL LOOP
        ---------------
        These "while not cont:" blocks are intentional placeholders for a richer
        add/edit customer flow. Each path currently returns immediately,
        but the loop gives a future slot for:
        - input validation / re-prompts,
        - policy/tier branching (e.g., tenure-based loyalty),
        - multi-field decisions before mutating state.

        In a GUI, this becomes event-driven callbacks. Here, it keeps the CLI
        interaction and business-state transitions in one place.
        """
        if self.active:
            cont = False
            while not cont:
                tblok = (
                    f"\nAdd {self.name} to loyalty rewards program? Enter [Y]es or [N]\n\n"
                )
                slow_tblok(tblok)
                # (tblok = "") is a visual cue; due to frequent reuse, indicates to anyone
                # that it's always cleared before reuse, even if redundant
                tblok = ""
                amend = input("Enter: ").lower()

                if amend == "y" and not self.loyalty:
                    self.loyalty = True
                    cont = True
                    return (
                        f"\n{self.name} added to loyalty rewards program.\n\n"
                        f"-{self.name}'s Details:\n"
                        f"{'=' * 30}"
                        f"{self.details()}"
                    )

                elif amend == "y" and self.loyalty:
                    cont = True
                    return (
                        f"\n{self.name} already a loyalty rewards member.\n"
                        "No changes made to customer."
                    )

                else:
                    return f"\n{self.name} was not added to the program."

        elif not self.active and self.loyalty:
            cont = False

            while not cont:
                tblok = (
                    f"\n{self.name} is no longer active.\n"
                    "Would you like to remove them from the loyalty rewards program? Enter [Y]es or [N]o\n"
                )
                slow_tblok(tblok)
                tblok = ""

                amend = input("Enter: ").lower()

                if amend == "y":
                    self.loyalty = False
                    cont = True
                    return (
                        f"\n{self.name} removed from loyalty rewards program.\n\n"
                        f"-{self.name}'s Details:\n"
                        f"{'=' * 30}"
                        f"{self.details()}"
                    )

                elif amend == "n":
                    cont = True
                    return f"\nNo changes made to {self.name}."

        else:
            return f"\n{self.name} is inactive and not enrolled. No changes were made."

    def details(self):
        """
        Details Method
        - Return (Name:name, Customer Type:cust_type, Active Customer:active, Loyalty Rewards Member:loyalty) attributes
        """
        return (
            f"\nName:                     {self.name}\n"
            f"Customer Type:            {self.cust_type}\n"
            f"Active Customer?:         {self.active}\n"
            f"Loyalty Rewards Member?:  {self.loyalty}\n"
        )


# ------ Enterprise Customer ------


class Enterprise(Customer):
    """
    Enterprise Customer Sub-Class:
    self.name - Customer Name
    self.cust_type - Customer Type (Wholesale/Retail/Spec Work/etc...)
    self.active - Active Customer T/F (default = True)
    self.discount_active - Active Discount T/F (default = False)
    self.discount_type - Type of Discount (default = "N/A")
    """

    def __init__(self, name, cust_type, active=True, discount_active=False, discount_type="N/A"):
        super().__init__(name, cust_type, active)
        self.discount_active = discount_active
        self.discount_type = discount_type

    def discount(self):
        """
        Discount Method
        - Check if customer is active
            - Empty Check: If attribute is empty, return formatted discount message function
                -(had the idea late in writing this of separating out return messages
                  into a module since it's reasonable to me that those elements have a
                  higher likelihood of being updated more frequently, and should be
                  separate from the Class structure itself)
            - If active is True, set active True
            - If active is False, set active False and type None, return status update
        """
        if self.active is None:
            msg = f"{self.name}'s active status is currently empty."
            width = max(36, (len(msg)))
            return discount_message(msg, width)
        elif self.active:
            self.discount_active = True
            # DEMO: When activating, assign PH type to show invariant discount_active has type.
            self.discount_type = "Test_Placeholder"
            return (
                f"\n{self.name}'s active discount status set to {self.discount_active}\n\n"
                f"-{self.name}'s Details:\n"
                f"{'=' * 30}"
                f"{self.details()}"
            )
        elif not self.active:
            self.discount_active = False
            self.discount_type = None
            return (
                f"\n{self.name}'s active discount status set to:     -{self.discount_active}-\n"
                f" and the Discount Type field set to:                      -{self.discount_type}-\n\n"
                f"-{self.name}'s Details:\n"
                f"{'=' * 30}"
                f"{self.details()}"
            )

    def details(self):
        """
        Details Method
        - Return (Name:name, Customer Type:cust_type, Active Customer:active,
                   Discount Type:discount_type) attributes
        """
        details_me = (
            f"\nName:              {self.name}\n"
            f"Customer Type:     {self.cust_type}\n"
            f"Active Customer?:  {self.active}\n"
            f"Discount Active?:  {self.discount_active}\n"
            f"Discount Type:     {self.discount_type}\n"
        )
        return details_me

# ------ Demo Instantiations ------

# ------ Retail ------


retail_01 = Retail(
    name="Janus, Anthony",
    cust_type="Residential",
    active=True,
    loyalty=False
)

retail_02 = Retail(
    name="Sanders, John",
    cust_type="Contractor",
    active=False,
    loyalty=False
)

# ------ Enterprise ------

ent_01 = Enterprise(
    name="Janus Applied Systems",
    cust_type="Spec Work",
    active=True,
    discount_active=False,
    discount_type="N/A"
)

ent_02 = Enterprise(
    name="Health Med Hospitals",
    cust_type="Ongoing - Medical Facility Network",
    active=False,
    discount_active=True,
    discount_type="Medical/MilitaryAdmin"
)

ent_03 = Enterprise(
    name="Acme Research Labs",
    cust_type="R&D Contract",
    active=None,
    discount_active=False,
    discount_type="N/A"
)


# ------ Main Program Logic ------


def main():
    line = "=" * 70
    tblok = (
        f"\n\n{line}\n\n"
        f"{'-' * 68}\n"
        f" ***Validation try & except blocks not used in this assignment.***\n"
        f"***Intentional decision to focus on other concepts w/o time sink.***\n"
        f"{'-' * 68}\n"
        f"\nPlease make a selection:\n"
        f"{'=' * 24}\n\n"
        f"1) Interactive Demo (assignment reqs)\n"
        f"2) Customer Menu (not yet implemented)\n\n"
    )
    slow_tblok(tblok)
    tblok = ""

    choice = int(input("Enter: "))

    steps = (
        (retail_01, retail_01.details,
         "Show Retail active customer's current\n           attributes before any loyalty changes."),
        (retail_01, retail_01.discount,
         "Prompt to enroll active non-member in\n           loyalty; update state and display details."),
        (retail_02, retail_02.details,
         "Show Retail inactive non-member's\n           attributes prior to discount logic\n           execution."),
        (retail_02, retail_02.discount,
         "Handle inactive, not-enrolled customer;\n           perform no changes and report status."),
        (ent_01, ent_01.details,
         "Show Enterprise active customer's\n           attributes before automatic\n           discount activation check."),
        (ent_01, ent_01.discount,
         "Activate enterprise discount for active\n           account; confirm by printing updated details."),
        (ent_02, ent_02.details,
         "Show Enterprise inactive customer's\n           attributes with a currently defined\n           discount type."),
        (ent_02, ent_02.discount,
         "Deactivate discount for inactive enterprise;\n           clear discount type and print summary."),
        (ent_03, ent_03.details,
         "Show Enterprise customer whose active\n           status is unknown, prior to policy check."),
        (ent_03, ent_03.discount,
         "Detect missing active status; emit banner\n           message via helper and continue.")
    )

    if choice == 1:
        tblok = (
            f"\nPlay Demo\n"
        )
        slow_tblok(tblok)
        tblok = ""

        count = 1
        for obj, method, string in steps:
            obj_name = obj.__class__.__name__
            method_name = method.__name__

            tblok = (
                f"{'=' * 70}\n"
                f"--- [ Test ({count}) ]-[ {obj_name} ]-[ {method_name} ] ---\n"
                f"{'=' * 50}\n\n"
                f"Test Goal: {string}"
            )
            slow_tblok(tblok)
            tblok = ""

            do = method()
            if do is not None and isinstance(do, str):
                slow_tblok(do)

            tblok = (
                f"\n{'-\n' * 2}\n"
            )
            slow_tblok(tblok)
            tblok = ""

            count += 1

    elif choice == 2:
        tblok = (
            f"{'=' * 24}\n\n"
            "I'm sorry, that option has not been implemented yet.\n\n"
            f"{'-\n' * 2}\n"
        )
        slow_tblok(tblok)
        tblok = ""

    print(
        f"{'=' * 70}\n"
        f"--Test Complete--\n\n"
    )


if __name__ == "__main__":
    main()
