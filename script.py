from gui_window import GuiWindow


def main():
    brightness_pass = '/sys/class/backlight/intel_backlight/actual_brightness'
    with open(brightness_pass) as f:
        s = f.read()

    print("Now brightness is " + s)

    gui_window_class = GuiWindow()
    print("set brightness: " + str(gui_window_class.creat_gui_window(s)))


if __name__ == '__main__':
    main()
