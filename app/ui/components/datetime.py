# app/ui/components/datetime.py
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QLabel
from PyQt5.Qt import Qt

class DateTimeWidget(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self._timer = QTimer()
        self._timer.timeout.connect(self._update_time)
        self._timer.start(1000)
        self._update_time()

    def _update_time(self):
        current = QDateTime.currentDateTime()
        formatted = current.toString("dddd, MMMM d, yyyy  hh:mm:ss AP")
        self.setText(formatted)