import gc

class SmartDevice:
    device_count = 0

    def __init__(self, device_name, model_number, is_online=False) -> None:
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = {}
        self._device_info = lambda: {
            "name": self.device_name, "model": self.model_number}
        SmartDevice.device_count += 1

    def update_status(self, attribute, value):
        self.status[attribute] = value

    def get_status(self, attribute):
        return self.status.get(attribute, 'Attribute not found')

    def toggle_online(self):
        self.is_online = not self.is_online

    def reset(self):
        self.status = {}

    def __call__(self):
        return f"{self.device_name} (Model: {self.model_number})"
    
    def __del__(self):
        SmartDevice.device_count -= 1

    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, val):
        self._device_info = val
