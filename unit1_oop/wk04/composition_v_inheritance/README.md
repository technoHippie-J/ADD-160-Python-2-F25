# Smart Home Device Management System
- This file written by Claude Sonnet 4.5

A modular IoT device management framework demonstrating **inheritance** and **composition** design patterns in Python. Built as a walking skeleton that can be extended for real hardware integration.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Usage](#installation--usage)
- [Architecture](#architecture)
- [Extending the Framework](#extending-the-framework)
- [Assignment Requirements](#assignment-requirements)
- [Future Enhancements](#future-enhancements)

---

## 🎯 Overview

This project implements a smart home management system that demonstrates:
- **Inheritance**: Device hierarchy with specialized subclasses
- **Composition**: SmartHome class contains and manages device instances
- **Abstraction**: Abstract base classes with concrete implementations
- **Polymorphism**: Device-specific behaviors through method overriding

Currently implemented as a **walking skeleton** - a complete, working framework with simulated data that can be extended with real hardware integration.

---

## ✨ Features

### Current Implementation
- ✅ Multiple device types: RGB Lights, Tunable White Lights, Basic Lights, Thermostats, Switches
- ✅ Device management: Add, remove, list, and control devices
- ✅ Interactive CLI menu system with slow-text display
- ✅ Three connection modes:
  - **Remote**: Reads from `/etc/config.json`
  - **Local**: Reads from brand-specific JSON files
  - **Demo**: Uses hardcoded data (no external files needed)
- ✅ Automatic fallback to demo mode if JSON files are missing
- ✅ Works in both structured (folders) and flat (all files in one directory) layouts

### Device Capabilities
- **RGB Lights**: Color control (RGB values), scene modes (Party, Relax, Focus, Sleep)
- **Tunable White Lights**: Adjustable color temperature (2700K-6500K)
- **Basic Lights**: Simple on/off with toggle functionality
- **Thermostats**: Temperature and humidity monitoring/control
- **Switches**: Basic power switching

---

## 📁 Project Structure

### Full Structure (GitHub)
```
composition_v_inheritance/
│
├── __main__.py                 # Main entry point & CLI menu system
├── README.md                   # This file
│
├── network/
│   ├── smart_home.py          # SmartHome composition class
│   │
│   ├── devices/
│   │   ├── base_classes.py    # Device hierarchy (inheritance)
│   │   ├── connection.py      # Connection & config management
│   │   ├── demo_data.py       # Hardcoded demo configurations
│   │   │
│   │   ├── lights/            # Light device JSON configs
│   │   │   ├── philips.json
│   │   │   ├── ge.json
│   │   │   ├── samsung.json
│   │   │   └── ...
│   │   │
│   │   ├── thermostats/       # Thermostat JSON configs
│   │   │   ├── nest.json
│   │   │   ├── ecobee.json
│   │   │   └── ...
│   │   │
│   │   ├── switches/          # Switch JSON configs
│   │   │   ├── tplink.json
│   │   │   ├── wemo.json
│   │   │   └── ...
│   │   │
│   │   └── unknown/           # Generic fallback configs
│   │       ├── generic_light.json
│   │       ├── generic_thermostat.json
│   │       └── generic_switch.json
│   │
│   └── users/                 # Reserved for future user management
│
└── test_submission/           # Flat structure for Canvas submission
    ├── __main__.py
    ├── smart_home.py
    ├── base_classes.py
    ├── connection.py
    └── demo_data.py
```

### Minimal Structure (Canvas Submission)
```
any_folder/
├── __main__.py
├── smart_home.py
├── base_classes.py
├── connection.py
└── demo_data.py
```

---

## 🚀 Installation & Usage

### Option 1: Full Structure (Recommended for Development)

```bash
# Clone or download the repository
cd composition_v_inheritance

# Run the program
python __main__.py

# When prompted for connection type:
# - [L]ocal - Uses JSON configs from lights/, thermostats/, switches/ folders
# - [R]emote - Attempts to read /etc/config.json (likely unavailable)
# - [D]emo - Uses hardcoded data from demo_data.py (no files needed)
```

### Option 2: Flat Structure (Canvas Submission)

```bash
# Download the 5 required .py files:
# - __main__.py
# - smart_home.py
# - base_classes.py
# - connection.py
# - demo_data.py

# Place them in any folder
cd your_folder

# Run the program
python __main__.py

# Program will automatically work in demo mode
```

### Menu Navigation

```
Main Menu:
1. Add Device          → Select device type and add to system
2. View All Devices    → Display all devices with status
3. Control Device      → Turn on/off, adjust settings
4. Remove Device       → Remove device by number
5. Turn All Off        → Power off all devices
6. Turn All On         → Power on all devices
7. Exit                → Quit program
```

---

## 🏗️ Architecture

### Inheritance Hierarchy (Is-A Relationship)

```
Device (Abstract Base Class)
│
├── Light
│   ├── RGBLight           → Full color control + scenes
│   ├── TunableWhiteLight  → Adjustable color temperature
│   └── BasicLight         → Simple on/off
│
├── Thermostat             → Temperature/humidity control
│
└── Switch                 → Basic power switching
```

**Key Concepts:**
- `Device` is an **abstract base class** with common attributes (model, status, power, brand)
- All devices inherit `power()` method and must implement `get_info()` abstract method
- Subclasses add specialized attributes and methods

### Composition Structure (Has-A Relationship)

```python
SmartHome
├── devices: List[Device]     # SmartHome HAS-A collection of devices
│   ├── RGBLight instance
│   ├── Thermostat instance
│   ├── Switch instance
│   └── ...
└── Methods:
    ├── add_device()
    ├── remove_device()
    ├── list_devices()
    ├── turn_all_on()
    └── turn_all_off()
```

**Key Concepts:**
- `SmartHome` **contains** device instances (composition)
- Manages device lifecycle (add/remove)
- Provides system-wide operations (turn all on/off)

### Configuration System

```
connection.py
├── detect_net_type()      → Ask user: Remote/Local/Demo
├── get_info_json()        → Load config from JSON or demo_data
├── brand_chk()            → Extract brand from config
├── model_chk()            → Extract model from config
└── slow_tblok()           → Slow text display helper

demo_data.py
├── LIGHT_CONFIGS          → Hardcoded light configs (Philips, GE, etc.)
├── THERMOSTAT_CONFIGS     → Hardcoded thermostat configs
├── SWITCH_CONFIGS         → Hardcoded switch configs
└── get_demo_config()      → Retrieve demo config by device type
```

### Import Flexibility

Each file uses **dual import strategy** to work in both structures:

```python
# Example from base_classes.py
try:
    from . import connection      # Relative import (folder structure)
except ImportError:
    import connection             # Absolute import (flat structure)
```

This allows the code to run whether files are organized in folders or all in one directory.

---

## 🔧 Extending the Framework

This is a **walking skeleton** designed for future expansion. Here's how to extend it:

### Adding New Device Types

1. **Create the class** in `base_classes.py`:
```python
class SecurityCamera(Device):
    def __init__(self, model, status, pwr, brand="unknown", resolution="1080p"):
        super().__init__(model, status, pwr, category="Cameras", brand=brand)
        self.resolution = resolution
    
    def get_info(self):
        # Implement connection logic
        pass
    
    def start_recording(self):
        return f"Recording started at {self.resolution}"
```

2. **Add demo data** in `demo_data.py`:
```python
CAMERA_CONFIGS = {
    'ring': {
        "Brand": "Ring",
        "Model": "Stick Up Cam",
        "Category": "Cameras",
        "Resolution": "1080p"
    }
}
```

3. **Update menu** in `__main__.py`:
```python
def add_device_menu(home):
    # Add option:
    # "5. Security Camera"
    
    elif choice == "5":
        device = SecurityCamera(model="New Camera", status="active", pwr=False)
        device.get_info()
        home.add_device(device)
```

### Integrating Real Hardware

Replace simulated `get_info()` with actual hardware detection:

```python
# In base_classes.py - future implementation
class RGBLight(Light):
    def get_info(self):
        # Current: Simulated connection
        self.device_type = connection.detect_device_type()
        self.network_type = connection.detect_net_type()
        self.config_data, self.brand = connection.get_info_json(
            self.device_type, self.network_type)
        
        # Future: Real hardware connection
        # import requests
        # self.ip_address = connection.scan_network_for_lights()
        # response = requests.get(f"http://{self.ip_address}/api/config")
        # self.config_data = response.json()
        # self.brand = self.config_data['manufacturer']
```

### Adding User Management

The `users/` folder is reserved for future user authentication:

```python
# Future: network/users/user_manager.py
class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions  # ['add_device', 'remove_device', 'control']

class UserManager:
    def __init__(self):
        self.users = []
    
    def authenticate(self, username, password):
        # Implement authentication
        pass
```

---

## 📚 Assignment Requirements

This project fulfills the following assignment requirements:

### ✅ Inheritance
- [x] Base `Device` class with common attributes (model, status, power, brand)
- [x] Common method: `power()` to turn devices on/off
- [x] Abstract method: `get_info()` that subclasses must implement
- [x] `Light` subclass inheriting from `Device`
- [x] Three specialized light types: `RGBLight`, `TunableWhiteLight`, `BasicLight`
- [x] Each specialized class has unique attributes and methods
- [x] `Thermostat` subclass with temperature/humidity control

### ✅ Composition
- [x] `SmartHome` class that **contains** device instances
- [x] Methods to manage devices (add, remove, list)
- [x] System-wide operations (turn all on/off)

### ✅ User Interface
- [x] Interactive CLI menu system
- [x] Options to add, remove, view, and control devices
- [x] Device-specific controls (brightness, color, temperature)

### ✅ Additional Features (Beyond Requirements)
- [x] JSON configuration system for brand-specific device data
- [x] Demo mode for testing without external files
- [x] Automatic fallback mechanisms
- [x] Works in multiple deployment scenarios
- [x] Professional code structure and documentation

---

## 🚀 Future Enhancements

### Phase 1: Hardware Integration
- [ ] Network scanning for device discovery
- [ ] Protocol implementations (Zigbee, Z-Wave, WiFi)
- [ ] Real-time device status monitoring
- [ ] Device pairing/authentication

### Phase 2: Advanced Features
- [ ] Scheduling/automation (turn on lights at sunset)
- [ ] Scene management (save/load room configurations)
- [ ] Energy monitoring and reporting
- [ ] Voice control integration (Alexa, Google Home)

### Phase 3: UI Improvements
- [ ] Web dashboard (Flask/Django)
- [ ] Mobile app (React Native)
- [ ] Real-time WebSocket updates
- [ ] Device grouping (rooms, zones)

### Phase 4: Backend Services
- [ ] Database persistence (SQLite/PostgreSQL)
- [ ] User authentication and authorization
- [ ] API endpoints for external integrations
- [ ] Cloud synchronization

### Phase 5: Arduino/Microcontroller Integration
- [ ] Serial communication with Arduino devices
- [ ] Custom protocol for DIY devices
- [ ] Firmware update management
- [ ] Sensor data aggregation

---

## 🛠️ Technical Details

### Python Version
- Developed with Python 3.13
- Compatible with Python 3.7+

### Dependencies
- **Standard Library Only**: No external packages required
- `abc`: Abstract base classes
- `json`: Configuration file parsing
- `time`: Slow text display timing
- `sys`: Exit handling

### Design Patterns Used
- **Abstract Factory**: Device creation through menu system
- **Strategy**: Different connection modes (Remote/Local/Demo)
- **Composite**: SmartHome managing device collections
- **Template Method**: Device base class with customizable `get_info()`

---

## 📖 Learning Outcomes

This project demonstrates understanding of:

1. **Object-Oriented Programming**
   - Inheritance hierarchies
   - Composition vs inheritance ("is-a" vs "has-a")
   - Abstract base classes and interfaces
   - Polymorphism through method overriding

2. **Software Architecture**
   - Separation of concerns
   - Modular design
   - Configuration management
   - Error handling and fallbacks

3. **Professional Practices**
   - Walking skeleton development
   - Dual-mode operation (dev/production)
   - Graceful degradation
   - Extensible architecture

---

## 👤 Author

**Student Project** - ADD-160 Python 2 (Fall 2025)

**Purpose**: Demonstrate inheritance and composition design patterns while building a practical, extensible framework for future IoT projects.

---

## 📄 License

Educational project - free to use and modify for learning purposes.

---

## 🤝 Contributing

This is a class assignment, but suggestions for future enhancements are welcome! Feel free to fork the repository and experiment with your own additions.

---

## 📞 Support

For questions about this project:
1. Check the code comments - most functions are documented
2. Review the architecture diagram above
3. Try running in demo mode to see how it works

---

**Happy Coding!** 🎉

*Built as a walking skeleton - ready to evolve into a full-featured smart home system.*