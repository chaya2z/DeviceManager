class FileHandling:
    @staticmethod
    def load_actual_brightness():
        """
        Loading '/sys/class/backlight/intel_backlight/actual_brightness'

        :return: str value of the file
        """
        actual_brightness_pass = '/sys/class/backlight/intel_backlight/actual_brightness'
        with open(actual_brightness_pass) as f:
            current_brightness = f.read()
        f.close()
        return current_brightness

    @staticmethod
    def write_brightness(brightness_value):
        """
        Update brightness to '/sys/class/backlight/intel_backlight/brightness'

        :param brightness_value: new brightness value
        :return: None
        """
        update_value = brightness_value
        brightness_pass = '/sys/class/backlight/intel_backlight/brightness'
        with open(brightness_pass, mode='w') as f:
            f.write(update_value)
        f.close()
