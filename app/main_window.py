from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QMessageBox, QApplication, QSystemTrayIcon,QLabel
)
from PyQt5.QtCore import Qt
from .core.timer import TimerService
from .core.tray import SystemTrayManager
from .ui.components import DateTimeWidget, CountdownWidget, TimeSettingsGroup, MessageGroup
from .ui.popups.reminder_popup import ReminderPopup
from .utils import convert_to_seconds
from .style import HOME_MAIN_STYLE, HOME_LIVE_DATE, HOME_COUNTDOWN,REMINDER_RUNNING,IMAGE_LABEL_STYLE
from PyQt5.QtGui import QPixmap
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.timer_service = TimerService()
        self.tray = SystemTrayManager(self)
        self._setup_ui()
        self._connect_signals()
        
    def _setup_ui(self):
        self.setWindowTitle("🕒 TimeSip")
        self.setGeometry(100, 100, 700, 550)
        self.setStyleSheet(HOME_MAIN_STYLE)

        # Image label
        self.image_label = QLabel()  # create QLabel first
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, '..', 'icons', 'timesip.png')
        icon_path = os.path.normpath(icon_path)
        pixmap = QPixmap(icon_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.image_label.setAlignment(Qt.AlignCenter)  # center the image
        self.image_label.setStyleSheet(IMAGE_LABEL_STYLE)

        
        # Create components
        self.datetime_widget = DateTimeWidget()
        self.datetime_widget.setStyleSheet(HOME_LIVE_DATE)
        self.countdown_widget = CountdownWidget()
        self.countdown_widget.setStyleSheet(HOME_COUNTDOWN)
        self.time_settings = TimeSettingsGroup()
        self.message_group = MessageGroup()
        self.start_btn = QPushButton("🚀 Start Reminder")
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        
        # Add widgets - image on top
        main_layout.addWidget(self.image_label)
        main_layout.addWidget(self.datetime_widget)
        main_layout.addWidget(self.countdown_widget)
        main_layout.addWidget(self.time_settings)
        main_layout.addWidget(self.message_group)
        main_layout.addWidget(self.start_btn)
        
        self.setLayout(main_layout)


    def _connect_signals(self):
        self.start_btn.clicked.connect(self.start_reminder)
        self.countdown_widget.stop_button.clicked.connect(self.stop_reminder)
        self.timer_service.timer_updated.connect(self.update_countdown)
        self.timer_service.timer_completed.connect(self.show_reminder)

    def start_reminder(self):
        try:
            value = float(self.time_settings.duration)
            unit = self.time_settings.unit
            message = self.message_group.message
            
            if value <= 0 or not message:
                raise ValueError
                
            seconds = convert_to_seconds(value, unit)
            self.timer_service.start(seconds)
            self.countdown_widget.show()
            self.start_btn.setEnabled(False)
            self.update_start_button(running=True)
            
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please check your inputs")

    def stop_reminder(self):
        self.timer_service.stop()
        self.countdown_widget.hide()
        self.start_btn.setEnabled(True)
        self.update_start_button(running=False)

    def update_countdown(self, seconds):
        self.countdown_widget.update_countdown(seconds)
    
    def update_start_button(self, running: bool):
        if running == True:
            self.start_btn.setText("⏳ Reminder Running...")
            self.start_btn.setEnabled(False)
            self.start_btn.setStyleSheet(REMINDER_RUNNING)
        elif running == False:
            self.start_btn.setText("🚀 Start Reminder")
            self.start_btn.setEnabled(True)
            self.start_btn.setStyleSheet("")




    def show_reminder(self):
        """Show reminder popup"""
        # Hide countdown elements
        self.countdown_widget.hide()
        self.start_btn.setEnabled(True)
        self.update_start_button(running=False) 

        # Show system tray notification if available
        if hasattr(self.tray, 'tray_icon') and self.tray.tray_icon.isVisible():
            self.tray.tray_icon.showMessage(
                "⏰ REMINDER ALERT",
                self.message_group.message,
                QSystemTrayIcon.Critical,
                10000  # Show for 10 seconds
            )

        # Create popup dialog
        popup = ReminderPopup(self.message_group.message)
        
        # Connect buttons to actions
        popup.restart_btn.clicked.connect(lambda: self.handle_popup_action("restart", popup))
        popup.snooze_btn.clicked.connect(lambda: self.handle_popup_action("snooze", popup))
        popup.close_btn.clicked.connect(lambda: self.handle_popup_action("close", popup))
        
        # Store reference to popup
        self.popup_dialog = popup
        
        # Show popup
        popup.show()



    def handle_popup_action(self, action, popup):
        """Handle popup button actions"""
        # Close popup first
        if popup:
            popup.close()
        
        if action == "restart":
            # Restart with original timer settings
            self.restart_reminder()
                
        elif action == "snooze":
            # Snooze for 5 minutes
            self.snooze_reminder(300)

    def restart_reminder(self):
        """Restart the timer with original duration"""
        if hasattr(self.timer_service, 'duration'):
            self.timer_service.start(self.timer_service.duration)
            self.countdown_widget.show()
            self.start_btn.setEnabled(False)
            self.update_start_button(running=True)

    def snooze_reminder(self, seconds):
        """Handle snooze functionality"""
        self.timer_service.start(seconds)
        self.countdown_widget.show()
        self.start_btn.setEnabled(False)
        self.update_start_button(running=True)
                
    def show_normal(self):
        self.show()
        self.raise_()
        self.activateWindow()

    def quit_app(self):
        self.timer_service.stop()
        QApplication.quit()

    def closeEvent(self, event):
        """Override close event to hide the window instead of closing"""
        self.hide()
        event.ignore()
