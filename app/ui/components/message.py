# app/ui/components/message.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLineEdit

class MessageGroup(QGroupBox):
    def __init__(self):
        super().__init__("💬 Reminder Message")
        self.message_input = QLineEdit()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()
        self.message_input.setPlaceholderText("Enter your reminder message here...")
        self.message_input.setText("Time's up!")
        layout.addWidget(self.message_input)
        self.setLayout(layout)

    @property
    def message(self):
        return self.message_input.text().strip()