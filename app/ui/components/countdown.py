# app/ui/components/countdown.py
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from app.style import HOME_STOP_BUTTON

class CountdownWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.countdown_label = QLabel()
        self.stop_button = QPushButton("🛑 Stop Reminder")
        self.stop_button.setStyleSheet(HOME_STOP_BUTTON)
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.countdown_label)
        layout.addStretch()
        layout.addWidget(self.stop_button)
        self.hide()

    def update_countdown(self, seconds):
        hrs, rem = divmod(seconds, 3600)
        mins, secs = divmod(rem, 60)
        self.countdown_label.setText(f"⏳ Time remaining: {hrs:02d}:{mins:02d}:{secs:02d}")