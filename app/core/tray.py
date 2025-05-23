# app/core/tray.py
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon

class SystemTrayManager(QSystemTrayIcon):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._setup_icon()
        self._setup_menu()

    def _setup_icon(self):
        icon = QIcon("icons/app_icon.png")  # Update with actual icon path
        self.setIcon(icon)

    def _setup_menu(self):
        menu = QMenu()
        show_action = menu.addAction("Show")
        show_action.triggered.connect(self.parent.show_normal)
        quit_action = menu.addAction("Quit")
        quit_action.triggered.connect(self.parent.quit_app)
        self.setContextMenu(menu)