#!/usr/bin/python3

import sys
import getpass
import os
from PyQt5.QtWidgets import *


class ShutdownMenu(QDialog):
    # CANCEL - EXIT - SUSPEND - REBOOT - SHUTDOWN
    cancel_button = None
    exit_button = None
    suspend_button = None
    reboot_button = None
    shutdown_button = None

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle("Shutdown menu")

        text = QLabel("Hello, " + getpass.getuser() + "! What would you like to do?")

        hbox = QHBoxLayout()

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel)

        self.exit_button = QPushButton("Log out")
        self.exit_button.clicked.connect(self.exit)

        self.suspend_button = QPushButton("Suspend")
        self.suspend_button.clicked.connect(self.suspend)

        self.reboot_button = QPushButton("Reboot")
        self.reboot_button.clicked.connect(self.reboot)

        self.shutdown_button = QPushButton("Shutdown")
        self.shutdown_button.clicked.connect(self.shutdown)

        vbox.addWidget(text)
        hbox.addWidget(self.cancel_button)
        hbox.addWidget(self.exit_button)
        hbox.addWidget(self.suspend_button)
        hbox.addWidget(self.reboot_button)
        hbox.addWidget(self.shutdown_button)
        vbox.addLayout(hbox)

        self.show()

    def cancel(self):
        self.disable_buttons()
        self.close()

    def exit(self):
        self.disable_buttons()
        self.close()

    def suspend(self):
        self.disable_buttons()
        suspend_dbus()
        self.close()

    def reboot(self):
        self.disable_buttons()
        reboot_dbus()
        self.close()

    def shutdown(self):
        self.disable_buttons()
        shutdown_dbus()
        self.close()

    def disable_buttons(self):
        self.cancel_button.setEnabled(False)
        self.exit_button.setEnabled(False)
        self.suspend_button.setEnabled(False)
        self.reboot_button.setEnabled(False)
        self.shutdown_button.setEnabled(False)


def exit_system():
    os.system("i3-msg exit")


def suspend_dbus():
    os.system("lock")
    os.system("dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 \"org.freedesktop.login1.Manager.Suspend\" boolean:true")


def reboot_dbus():
    os.system("dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 \"org.freedesktop.login1.Manager.Reboot\" boolean:true")


def shutdown_dbus():
    os.system("dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 \"org.freedesktop.login1.Manager.PowerOff\" boolean:true")


if __name__ == '__main__':
    if len(sys.argv) is 1:
        app = QApplication(sys.argv)
        dl = ShutdownMenu()
        sys.exit(app.exec_())
    else:
        if sys.argv[1] == "logout":
            exit_system()
        elif sys.argv[1] == "suspend":
            suspend_dbus()
        elif sys.argv[1] == "reboot":
            reboot_dbus()
        elif sys.argv[1] == "shutdown":
            shutdown_dbus()
