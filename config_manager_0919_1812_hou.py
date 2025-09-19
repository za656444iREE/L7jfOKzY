# 代码生成时间: 2025-09-19 18:12:45
import json
from scrapy.exceptions import NotConfigured

"""
ConfigManager is a class designed to handle configuration files for Scrapy projects.
It provides a simple interface to read, write, and update configuration settings."""

class ConfigManager:
    def __init__(self, filename):
        """
        Initialize the ConfigManager with a configuration file.
        :param filename: The path to the configuration file.
        """
        self.filename = filename
        self.config = {}
        self.load_config()

    def load_config(self):
        """
        Load configuration settings from the file.
        """
        try:
            with open(self.filename, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise NotConfigured(f"The configuration file {self.filename} was not found.")
        except json.JSONDecodeError as e:
            raise NotConfigured(f"Failed to parse the configuration file: {e}")

    def get_config(self, key, default=None):
        """
        Retrieve a configuration setting by key.
        :param key: The key of the configuration setting.
        :param default: The default value to return if the key is not found.
        """
        return self.config.get(key, default)

    def set_config(self, key, value):
        """
        Set a configuration setting.
        :param key: The key of the configuration setting.
        :param value: The value to set.
        """
        self.config[key] = value
        self.save_config()

    def save_config(self):
        """
        Save the current configuration settings to the file.
        """
        with open(self.filename, 'w') as f:
            json.dump(self.config, f, indent=4)

    def remove_config(self, key):
        """
        Remove a configuration setting.
        :param key: The key of the configuration setting to remove.
        """
        if key in self.config:
            del self.config[key]
            self.save_config()

# Example usage:
if __name__ == '__main__':
    config_manager = ConfigManager('config.json')
    # Get a configuration setting
    setting = config_manager.get_config('setting_name', 'default_value')
    print(f"The configuration setting is: {setting}")
    # Set a configuration setting
    config_manager.set_config('setting_name', 'new_value')
    # Remove a configuration setting
    config_manager.remove_config('setting_name')
