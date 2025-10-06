from abc import ABC, abstractmethod

try:
    from . import connection
except ImportError:
    import connection

"""
Contains base device and device category classes
"""


class Device(ABC):
    def __init__(self, model, status="unknown", pwr=False, category="unknown", brand="unknown", local=1, web=0):
        self.model = model
        self.status = status
        self.pwr = pwr
        self.category = category
        self.brand = brand
        self.local = local
        self.web = web

    def power(self, pwr):
        if pwr:
            self.pwr = True
        else:
            self.pwr = False

    @abstractmethod
    def get_info(self):
        """Gets device details according to its particular method"""
        pass


class Light(Device):

    def __init__(self, model, status, pwr, category="Lights", brand="unknown", local=1, web=0, dimmer=0, dim_set=None):
        super().__init__(model, status, pwr, category, brand, local, web)
        self.dimmer = dimmer
        self.dim_set = dim_set

        self.device_type = None
        self.network_type = None
        self.config_data = None

    def get_info(self):
        """Gets device info by calling a module that contains methods for different frameworks' connection methods"""
        self.device_type = 'lights'
        self.network_type = connection.detect_net_type()
        self.config_data, self.brand = connection.get_info_json(
            self.device_type, self.network_type)

        if self.config_data:
            new_model = connection.model_chk(self.config_data)
            if new_model:
                self.model = new_model

    def is_dimmer(self):
        if self.config_data is None:
            self.get_info()

        dimmer = connection.dimmer_chk(self.config_data)
        return bool(dimmer)


class RGBLight(Light):
    """Lights with RGB color control"""

    def __init__(self, model, status, pwr, brand="unknown", rgb_color=(255, 255, 255), scene_mode="Normal"):
        super().__init__(model, status, pwr, brand=brand, dimmer=0)
        self.rgb_color = rgb_color
        self.scene_mode = scene_mode

    def set_color(self, r, g, b):
        """Set RGB color"""
        if all(0 <= val <= 255 for val in [r, g, b]):
            self.rgb_color = (r, g, b)
            return f"Color set to RGB({r}, {g}, {b})"
        return "Invalid RGB values (0-255)"

    def set_scene(self, scene):
        """Set lighting scene"""
        valid_scenes = ["Normal", "Party", "Relax", "Focus", "Sleep"]
        if scene in valid_scenes:
            self.scene_mode = scene
            return f"Scene set to {scene}"
        return f"Invalid scene"


class TunableWhiteLight(Light):
    """Lights with adjustable color temperature (warm to cool white)"""

    def __init__(self, model, status, pwr, brand="unknown", color_temp=3000):
        super().__init__(model, status, pwr, brand=brand, dimmer=0)
        self.color_temp = color_temp

    def set_color_temp(self, temp):
        """Adjust white color temperature"""
        if 2700 <= temp <= 6500:
            self.color_temp = temp
            return f"Color temperature set to {temp}K"
        return "Invalid color temperature (2700-6500K)"


class BasicLight(Light):
    """Simple on/off lights - no dimming, no color or temp control"""

    def __init__(self, model, status, pwr, brand="unknown"):
        super().__init__(model, status, pwr, brand=brand, dimmer=0)

    def toggle(self):
        """Simple toggle function for on/off states"""
        self.pwr = not self.pwr
        return f"Light {'on' if self.pwr else 'off'}"


class Thermostat(Device):

    def __init__(self, model, status, pwr, category="Thermostats", brand="unknown", local=1, web=0, tmp=0, hmd=0):
        super().__init__(model, status, pwr, category, brand, local, web)
        self.tmp = tmp
        self.hmd = hmd

        self.device_type = None
        self.network_type = None
        self.config_data = None

    def get_info(self):
        """Gets device info"""
        self.device_type = 'thermostats'
        self.network_type = connection.detect_net_type()
        self.config_data, self.brand = connection.get_info_json(
            self.device_type, self.network_type)

        if self.config_data:
            new_model = connection.model_chk(self.config_data)
            if new_model:
                self.model = new_model


class Switch(Device):

    def __init__(self, model, status, pwr, category="Switches", brand="unknown", local=1, web=0, state=0):
        super().__init__(model, status, pwr, category, brand, local, web)
        self.state = state

        self.device_type = None
        self.network_type = None
        self.config_data = None

    def get_info(self):
        """Gets device info"""
        self.device_type = 'switches'
        self.network_type = connection.detect_net_type()
        self.config_data, self.brand = connection.get_info_json(
            self.device_type, self.network_type)

        if self.config_data:
            new_model = connection.model_chk(self.config_data)
            if new_model:
                self.model = new_model
