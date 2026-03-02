class ConfigManager(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.key = self.get_key()
    
    def get_key(self):
        with open(self.config_file, "r") as f:
            data = f.read()
            f.close()
        return data

        