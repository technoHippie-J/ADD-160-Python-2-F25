"""
Demo configuration data - mirrors the JSON files for easy testing
Used when JSON files are not available
"""

LIGHT_CONFIGS = {
    'philips': {
        "Brand": "Philips",
        "Model": "Hue A19",
        "Category": "Lights",
        "Dimmer": True,
        "ColorTemp": 3000,
        "RGB": True,
        "MaxBrightness": 100,
        "PowerConsumption": "10W"
    },
    'ge': {
        "Brand": "GE",
        "Model": "C-Life LED",
        "Category": "Lights",
        "Dimmer": True,
        "ColorTemp": 2700,
        "RGB": False,
        "MaxBrightness": 100,
        "PowerConsumption": "9W"
    },
    'samsung': {
        "Brand": "Samsung",
        "Model": "SmartThings Bulb",
        "Category": "Lights",
        "Dimmer": True,
        "ColorTemp": 3500,
        "RGB": True,
        "MaxBrightness": 100,
        "PowerConsumption": "9.5W"
    },
    'govee': {
        "Brand": "Govee",
        "Model": "Smart LED Strip",
        "Category": "Lights",
        "Dimmer": True,
        "ColorTemp": 3000,
        "RGB": True,
        "MaxBrightness": 100,
        "PowerConsumption": "12W"
    }
}

THERMOSTAT_CONFIGS = {
    'nest': {
        "Brand": "Nest",
        "Model": "Learning Thermostat",
        "Category": "Thermostats",
        "Temperature": 72,
        "Humidity": 45,
        "TempUnit": "Fahrenheit",
        "Mode": "Auto"
    },
    'ecobee': {
        "Brand": "Ecobee",
        "Model": "SmartThermostat",
        "Category": "Thermostats",
        "Temperature": 70,
        "Humidity": 50,
        "TempUnit": "Fahrenheit",
        "Mode": "Heat"
    },
    'honeywell': {
        "Brand": "Honeywell",
        "Model": "Home T9",
        "Category": "Thermostats",
        "Temperature": 68,
        "Humidity": 48,
        "TempUnit": "Fahrenheit",
        "Mode": "Cool"
    }
}

SWITCH_CONFIGS = {
    'tplink': {
        "Brand": "TP-Link",
        "Model": "Kasa Smart Switch",
        "Category": "Switches",
        "Type": "Toggle",
        "MaxLoad": "15A",
        "Voltage": "120V"
    },
    'wemo': {
        "Brand": "Wemo",
        "Model": "Smart Plug",
        "Category": "Switches",
        "Type": "Outlet",
        "MaxLoad": "15A",
        "Voltage": "120V"
    },
    'ge': {
        "Brand": "GE",
        "Model": "Enbrighten Switch",
        "Category": "Switches",
        "Type": "Toggle",
        "MaxLoad": "15A",
        "Voltage": "120V"
    }
}

UNKNOWN_CONFIGS = {
    'generic_light': {
        "Brand": "Generic",
        "Model": "Basic Light",
        "Category": "Lights",
        "Dimmer": False,
        "RGB": False
    },
    'generic_thermostat': {
        "Brand": "Generic",
        "Model": "Basic Thermostat",
        "Category": "Thermostats",
        "Temperature": 72,
        "Humidity": 50
    },
    'generic_switch': {
        "Brand": "Generic",
        "Model": "Basic Switch",
        "Category": "Switches",
        "Type": "Toggle"
    }
}


def get_demo_config(device_type, brand=None):
    """
    Get demo configuration data for a device type

    Args:
        device_type: 'lights', 'thermostats', 'switches', or 'unknown'
        brand: Optional specific brand, otherwise returns first available

    Returns:
        tuple: (config_data dict, brand string)
    """
    config_map = {
        'lights': LIGHT_CONFIGS,
        'thermostats': THERMOSTAT_CONFIGS,
        'switches': SWITCH_CONFIGS,
        'unknown': UNKNOWN_CONFIGS
    }

    if device_type not in config_map:
        return {"Brand": "Unknown", "Model": "Unknown Device"}, "Unknown"

    configs = config_map[device_type]

    if brand and brand.lower() in configs:
        selected = configs[brand.lower()]
        return selected, selected['Brand']

    # Return first available brand
    first_brand = list(configs.keys())[0]
    selected = configs[first_brand]
    return selected, selected['Brand']
