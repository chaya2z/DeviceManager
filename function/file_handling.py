class FileHandling:
    @staticmethod
    def load_actual_brightness():
        actual_brightness_pass = '/sys/class/backlight/intel_backlight/actual_brightness'
        with open(actual_brightness_pass) as f:
            s = f.read()
        f.close()
        return s

    @staticmethod
    def write_brightness(brightness_value):
        update_value = brightness_value
        brightness_pass = '/sys/class/backlight/intel_backlight/brightness'
        with open(brightness_pass, mode='w') as f:
            f.write(update_value)
        f.close()
