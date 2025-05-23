# app/ui/components/time_settings.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox


class TimeSettingsGroup(QGroupBox):
    def __init__(self):
        super().__init__("⏱️ Time Settings")
        self.number_input = QLineEdit("5")
        self.time_unit_combo = QComboBox()
        self._setup_ui()

    def _setup_ui(self):
        time_layout = QVBoxLayout()
        time_input_layout = QHBoxLayout()

        # Duration input
        time_input_layout.addWidget(QLabel("Duration:"))
        self.number_input.setPlaceholderText("Enter number")
        self.number_input.setFixedWidth(100)
        time_input_layout.addWidget(self.number_input)

        # Time unit selection
        time_input_layout.addWidget(QLabel("Unit:"))
        self.time_unit_combo.addItems(["Seconds", "Minutes", "Hours", "Days", "Months", "Years"])
        self.time_unit_combo.setCurrentText("Minutes")
        self.time_unit_combo.setFixedWidth(100)
        time_input_layout.addWidget(self.time_unit_combo)

        time_input_layout.addStretch()
        time_layout.addLayout(time_input_layout)
        self.setLayout(time_layout)

    @property
    def duration(self):
        return self.number_input.text()

    @property
    def unit(self):
        return self.time_unit_combo.currentText()