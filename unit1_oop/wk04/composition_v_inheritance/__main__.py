import sys

try:
    from network.smart_home import SmartHome
    from network.devices.base_classes import *
    from network.devices.connection import slow_tblok
except ImportError:
    try:
        from smart_home import SmartHome
        from base_classes import *
        from connection import slow_tblok
    except ImportError as e:
        print("ERROR: Could not import required modules.")
        print("Make sure all .py files are present:\n")
        print("  - __main__.py")
        print("  - smart_home.py")
        print("  - base_classes.py")
        print("  - connection.py")
        print("  - demo_data.py")
        print(f"\nImport error: {e}")
        sys.exit(1)


def main_menu():
    """Display main menu and get user choice"""
    slow = (
        f"\n" + ("=" * 40) + "\n"
        f"Smart Home System - Main Menu\n"
        + ("=" * 40) + "\n"
        f"1. Add Device\n"
        f"2. View All Devices\n"
        f"3. Control Device\n"
        f"4. Remove Device\n"
        f"5. Turn All Devices Off\n"
        f"6. Turn All Devices On\n"
        f"7. Exit\n"
        + ("=" * 40) + ("\n" * 2)
    )
    slow_tblok(slow)
    slow = ""
    return input("Selection: ")


def add_device_menu(home):
    """
    Menu for adding a new device

    NOTE: In production, this would:
    1. Scan network for available devices
    2. Detect brand/model from device responses
    3. Load brand-specific configuration from JSON
    4. Establish actual hardware connection

    For this assignment demonstration, we simulate this with demo data.
    """
    slow = (
        f"\n" + ("=" * 40) + "\n"
        f"ADD DEVICE\n"
        + ("=" * 40) + "\n"
        f"1. RGB Light\n"
        f"2. Tunable White Light\n"
        f"3. Basic Light\n"
        f"4. Thermostat\n"
        f"5. Switch\n"
        f"6. Back to Main Menu\n"
        + ("=" * 40) + ("\n" * 2)
    )
    slow_tblok(slow)
    slow = ""

    choice = input("Select device type: ").strip()

    if choice == "1":
        device = RGBLight(model="New RGB", status="active", pwr=False)
        device.get_info()  # Your connection system kicks in here
        home.add_device(device)
        print(f"\nRGB Light added successfully!")

    elif choice == "2":
        device = TunableWhiteLight(
            model="New Tunable", status="active", pwr=False)
        device.get_info()
        home.add_device(device)
        print(f"\nTunable White Light added successfully!")

    elif choice == "3":
        device = BasicLight(model="New Basic", status="active", pwr=False)
        device.get_info()
        home.add_device(device)
        print(f"\nBasic Light added successfully!")

    elif choice == "4":
        device = Thermostat(model="New Thermostat", status="active", pwr=False)
        device.get_info()
        home.add_device(device)
        print(f"\nThermostat added successfully!")

    elif choice == "5":
        device = Switch(model="New Switch", status="active", pwr=False)
        device.get_info()
        home.add_device(device)
        print(f"\nSwitch added successfully!")


def control_device_menu(home):
    """Menu for controlling a specific device"""
    if not home.devices:
        print("\nThere are no devices on the network.")
        return

    slow_tblok(home.list_devices())

    try:
        index = int(input("\nSelect device number (0 to cancel): ")) - 1
        if index < 0:
            return

        device = home.get_device(index)
        if not device:
            print("Invalid device number")
            return

        slow = (
            f"\n" + ("=" * 40) + "\n"
            f"CONTROLLING: {device.__class__.__name__} - {device.model}\n"
            + ("=" * 40) + "\n"
            f"1. Turn On\n"
            f"2. Turn Off\n"
        )
        slow_tblok(slow)
        slow = ""
        if isinstance(device, RGBLight):
            slow = (
                f"3. Set RGB Color\n"
                f"4. Set Scene Mode\n"
            )
            slow_tblok(slow)
            slow = ""
        if isinstance(device, TunableWhiteLight):
            slow = (
                f"3. Set Color Temperature\n"
            )
            slow_tblok(slow)
            slow = ""
        if isinstance(device, Thermostat):
            slow = (
                f"3. Set Temperature\n"
            )
            slow_tblok(slow)
            slow = ""

        slow = (
            f"0. Back\n"
            + ("=" * 40) + ("\n" * 2)
        )
        slow_tblok(slow)
        slow = ""

        action = input("Selection: ").strip()

        if action == "1":
            device.pwr = True
            print(f"{device.model} Turned ON")
        elif action == "2":
            device.pwr = False
            print(f"{device.model} turned OFF")
        elif action == "3":
            if isinstance(device, RGBLight):
                r = int(input("Red (0-255): "))
                g = int(input("Green (0-255): "))
                b = int(input("Blue (0-255): "))
                print(device.set_color(r, g, b))
            elif isinstance(device, TunableWhiteLight):
                temp = int(input("Color Temperature (2700-6500K): "))
                print(device.set_color_temp(temp))
            elif isinstance(device, Thermostat):
                device.tmp = int(input("Set temperature (°F): "))
                print(f"Temperature set to {device.tmp}°F")
        elif action == "4" and isinstance(device, RGBLight):
            scene = input("Scene (Normal/Party/Relax/Focus/Sleep): ")
            print(device.set_scene(scene))

    except (ValueError, IndexError):
        print("Invalid input")


def main():
    """Main program loop"""
    home = SmartHome("My Smart Home")

    slow = (
        f"\n" + ("=" * 40) + "\n"
        f"Welcome to your Smart Home System!"
        f"\n" + ("=" * 40)
        + ("\n" * 2)
    )
    slow_tblok(slow)
    slow = ""

    while True:
        choice = main_menu()

        if choice == "1":
            add_device_menu(home)
        elif choice == "2":
            slow_tblok(home.list_devices())
            input("\nPress Enter to continue...")
        elif choice == "3":
            control_device_menu(home)
        elif choice == "4":
            slow_tblok(home.list_devices())
            try:
                index = int(
                    input("\nDevice number to remove (0 to cancel): ")) - 1
                if index >= 0:
                    print(home.remove_device(index))
            except (ValueError, IndexError):
                print("Invalid input.\n\n")
        elif choice == "5":
            print(home.turn_all_off())
        elif choice == "6":
            print(home.turn_all_on())
        elif choice == "7":
            print("\nGoodbye...")
            break
        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()
