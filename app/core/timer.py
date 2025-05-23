# app/core/timer.py
import time
import threading
from PyQt5.QtCore import QObject, pyqtSignal

class TimerService(QObject):
    timer_updated = pyqtSignal(int)
    timer_completed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self._is_running = False
        self._thread = None
        self.duration = 0

    def start(self, duration):
        self.duration = duration
        self._is_running = True
        self._thread = threading.Thread(target=self._run_timer, daemon=True)
        self._thread.start()

    def stop(self):
        self._is_running = False

    def _run_timer(self):
        start_time = time.time()
        while self._is_running and (time.time() - start_time) < self.duration:
            remaining = int(self.duration - (time.time() - start_time))
            self.timer_updated.emit(remaining)
            time.sleep(0.1)
        
        if self._is_running:
            self.timer_completed.emit()