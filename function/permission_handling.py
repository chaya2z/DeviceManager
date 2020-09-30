import os
import sys


class PermissionHandler:
    @staticmethod
    def permission_error_handler():
        if os.getegid() != 0:
            print("You must be root to run DeviceManager!")
            sys.exit()
        elif os.getegid() == 0:
            pass
