try:
    from network.devices.base_classes import *
except ImportError:
    from base_classes import *

"""
SmartHome class
"""


class SmartHome:
    def __init__(self, name="My Smart Home"):
        self.name = name
        self.devices = []

    def add_device(self, device):
        """Add a device to the smart home"""
        self.devices.append(device)
        return f"{device.__class__.__name__} '{device.model}' added to {self.name}"

    def remove_device(self, index):
        """Remove a device by index"""
        if 0 <= index < len(self.devices):
            removed = self.devices.pop(index)
            return f"Removed {removed.__class__.__name__} '{removed.model}'"
        return "Invalid device index"

    def list_devices(self):
        """Display all devices with their status"""
        if not self.devices:
            return "No devices in smart home"

        output = f"\n{self.name} Devices:\n" + "=" * 40 + "\n"
        for i, device in enumerate(self.devices):
            status = "On" if device.pwr else "Off"
            output += f"{i+1}. {device.__class__.__name__} - {device.model}\n"
            output += f"    Brand: {device.brand} | Status: {status}\n"

            if isinstance(device, RGBLight):
                output += f"    RGB Color: {device.rgb_color} | Scene: {device.scene_mode}\n"
            elif isinstance(device, TunableWhiteLight):
                output += f"    Color Temp: {device.color_temp}K\n"
            elif isinstance(device, BasicLight):
                output += f"    Status: {device.status}\n"
            elif isinstance(device, Thermostat):
                output += f"    Temperature: {device.tmp}°F | Humidity: {device.hmd}%\n"
            elif isinstance(device, Switch):
                output += f"    Status: {device.state}\n"

        return output

    def get_device(self, index):
        """Get a device by index"""
        if 0 <= index < len(self.devices):
            return self.devices[index]
        return None

    def turn_all_off(self):
        """Turn off all devices"""
        for device in self.devices:
            device.pwr = False
        return "All devices turned off"

    def turn_all_on(self):
        """Turn on all devices"""
        for device in self.devices:
            device.pwr = True
        return "All devices turned on"
