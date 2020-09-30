from gui_window import GuiWindow
from function.file_handling import FileHandling
from function.permission_handling import PermissionHandler
import sys


def main():
    PermissionHandler.permission_error_handler()

    # loading current brightness value
    file_handling = FileHandling()
    current_brightness = file_handling.load_actual_brightness()

    # creating GUI window
    gui_window_class = GuiWindow()
    update_brightness = str(gui_window_class.creat_gui_window(current_brightness))

    # writing new brightness value
    file_handling.write_brightness(update_brightness)

    sys.exit(0)


if __name__ == '__main__':
    main()
