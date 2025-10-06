import json
import time

try:
    from . import demo_data
except ImportError:
    import demo_data

REMOTE_CONFIG_PATH = f'/etc/config.json'
PRINT_DELAY = 0.15

# ------ Path Builder ------


def get_local_config_dir(device):
    """Build the local config directory path based on device type."""
    return f'./{device}/'

# ------ Slow Text Helper ------


def slow_tblok(slow):
    for line in slow.splitlines():
        time.sleep(PRINT_DELAY)
        print(line)

# ------ Attribute Grabbers ------


def model_chk(config_data):
    for attr, val in config_data.items():
        if attr == "Model":
            return val
    return None


def brand_chk(config_data):
    for attr, val in config_data.items():
        if attr == "Brand":
            return val
    return None


def dimmer_chk(config_data):
    for attr, val in config_data.items():
        if attr == "Dimmer":
            return val
    return None


# ------ Connection Type Detector ------


def detect_net_type():
    """Ask if connecting to remote or local device."""
    slow = (
        f"Are you connecting to a [R]emote or [L]ocal device? (or [D]emo)\n\n"
    )
    slow_tblok(slow)
    slow = ""
    connection_type = input("[R], [L], or [D]: ").lower()
    print("\n" * 2)
    if connection_type == "r":
        return "remote"
    elif connection_type == "l":
        return "local"
    elif connection_type == "d":
        return "demo"
    else:
        print("Invalid input, defaulting to demo mode...")
        return "demo"


# ------ Device Info Helper ------

def get_info_json(device_type, network_type):
    device = device_type
    connection = network_type
    local_config_dir = get_local_config_dir(device)
    detected = False
    config_data = None
    brand = None

    while not detected:
        if connection == "remote":
            try:
                with open(REMOTE_CONFIG_PATH, 'r') as config_file:
                    config_data = json.load(config_file)
                    brand = brand_chk(config_data)
                    detected = True
                    return config_data, brand
            except FileNotFoundError:
                print("Error: 'config.json' not found.")
                print("Falling back to demo mode...")
                connection = "demo"
                continue

        elif connection == "local":
            try:
                default_local_path = f'{local_config_dir}default_config.json'

                with open(default_local_path, 'r') as config_file:
                    config_data = json.load(config_file)
                    brand = brand_chk(config_data)

                actual_local_path = f'{local_config_dir}{brand}.json'

                with open(actual_local_path, 'r') as brand_file:
                    brand_config = json.load(brand_file)
                    detected = True
                    return brand_config, brand

            except FileNotFoundError as e:
                print(f"Error: Config file not found - {e}")
                print("Falling back to demo mode...")
                connection = "demo"
                continue

        elif connection == "demo":
            print(f"Using demo mode for {device_type}...")
            config_data, brand = demo_data.get_demo_config(device_type)
            print(f"Loaded {brand} {config_data.get('Model', 'Unknown')}")
            detected = True
            return config_data, brand

        else:
            slow = (
                f"Invalid choice, Please enter 'R' or 'L'\n"
            )
            slow_tblok(slow)
            slow = ""
            user_input = input("[R] or [L]: ").lower()
            if user_input == "r":
                connection = "remote"
            elif user_input == "l":
                connection = "local"
            elif user_input == "d":
                connection = "demo"

    return None, None
