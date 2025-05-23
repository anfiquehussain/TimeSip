# app/ui/popups/reminder_popup.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt, QDateTime
from app.style import POPUP_STYLES
import sys

class ReminderPopup(QWidget):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowFlags(
            Qt.Window | 
            Qt.WindowStaysOnTopHint | 
            Qt.FramelessWindowHint |
            Qt.WindowDoesNotAcceptFocus  # Adjust if focus is needed
        )
        self.message = message
        self._triggered_time = QDateTime.currentDateTime()
        self._setup_ui()
        self._setup_timers()
        self._setup_visibility_features()

    def _setup_ui(self):
        
        # Set window attributes - same as your working code
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_ShowWithoutActivating, False)  # Allow activation
        self.setStyleSheet(POPUP_STYLES["dialog"])
        
        # Main layout for centering - exactly like your working code
        main_layout = QVBoxLayout(self)
        main_layout.addStretch()

        # Content container - exactly like your working code
        content_widget = QWidget()
        content_widget.setStyleSheet("border: none;")
        content_widget.setFixedSize(800, 500)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setAlignment(Qt.AlignCenter)
        content_layout.setSpacing(30)

        # Title - exactly like your working code
        title = QLabel("⏰ REMINDER ALERT")
        title.setStyleSheet(POPUP_STYLES["title"])
        title.setAlignment(Qt.AlignCenter)
        title.setWordWrap(True)

        # Message - exactly like your working code
        message_label = QLabel(self.message)
        message_label.setStyleSheet(POPUP_STYLES["message"])
        message_label.setAlignment(Qt.AlignCenter)
        message_label.setWordWrap(True)

        # Time display - exactly like your working code
        time_widget = QWidget()
        time_layout = QVBoxLayout(time_widget)
        time_layout.setSpacing(10)
        
        self.time_label = QLabel()
        self.time_label.setStyleSheet(POPUP_STYLES["time_label"])
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.triggered_label = QLabel(
            f"Triggered at: {self._triggered_time.toString('dddd, MMMM d, yyyy - hh:mm:ss AP')}"
        )
        self.triggered_label.setStyleSheet(POPUP_STYLES["triggered_label"])
        self.triggered_label.setAlignment(Qt.AlignCenter)
        
        time_layout.addWidget(self.time_label)
        time_layout.addWidget(self.triggered_label)

        # Buttons - exactly like your working code
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
        buttons_layout.setSpacing(20)

        self.restart_btn = QPushButton("🔄 Restart Timer")
        self.restart_btn.setStyleSheet(POPUP_STYLES["restart_button"])
        self.restart_btn.setMinimumWidth(180)

        self.snooze_btn = QPushButton("⏸️ Snooze 5min")
        self.snooze_btn.setStyleSheet(POPUP_STYLES["snooze_button"])
        self.snooze_btn.setMinimumWidth(180)

        self.close_btn = QPushButton("✅ Close")
        self.close_btn.setStyleSheet(POPUP_STYLES["close_button"])
        self.close_btn.setMinimumWidth(180)

        buttons_layout.addWidget(self.restart_btn)
        buttons_layout.addWidget(self.snooze_btn)
        buttons_layout.addWidget(self.close_btn)

        # Add all elements to content layout - exactly like your working code
        content_layout.addWidget(title)
        content_layout.addWidget(message_label)
        content_layout.addWidget(time_widget)
        content_layout.addWidget(buttons_widget)

        # Add content to main layout - exactly like your working code
        main_layout.addWidget(content_widget, alignment=Qt.AlignCenter)
        main_layout.addStretch()

    def _setup_timers(self):
        # Timer for updating current time - exactly like your working code
        self._time_timer = QTimer(self)
        self._time_timer.timeout.connect(self._update_time)
        self._time_timer.start(1000)
        self._update_time()

    def _setup_visibility_features(self):
        """Set up features to ensure popup visibility"""
        # Flash timer for attention grabbing
        self.flash_timer = QTimer()
        self.flash_timer.timeout.connect(self._flash_window)
        self.flash_count = 0

    def _update_time(self):
        # Exactly like your working code
        current_time = QDateTime.currentDateTime().toString("dddd, MMMM d, yyyy - hh:mm:ss AP")
        self.time_label.setText(f"Current time: {current_time}")

    def show(self):
        """Show popup with enhanced visibility - based on your working code"""
        # Make it fullscreen first - exactly like your working code
        self.showFullScreen()
        # self.showNormal()  # Instead of showFullScreen
        self.activateWindow()
        self.raise_()
        
        # Platform-specific visibility enhancements - from your working code
        if sys.platform.startswith('win'):
            self._bring_to_front_windows()
            # Windows-specific methods - exactly like your working code
            try:
                import ctypes
                from ctypes import wintypes
                
                # Get window handle
                hwnd = int(self.winId())
                
                # Set window to foreground
                ctypes.windll.user32.SetForegroundWindow(hwnd)
                ctypes.windll.user32.SetWindowPos(
                    hwnd, -1, 0, 0, 0, 0, 
                    0x0001 | 0x0002 | 0x0040  # SWP_NOSIZE | SWP_NOMOVE | SWP_SHOWWINDOW
                )
            except Exception as e:
                print(f"Windows-specific window positioning failed: {e}")
        
        elif sys.platform.startswith('darwin'):  # macOS
            # macOS-specific methods - exactly like your working code
            self.raise_()
        
        # Start attention grabbing features
        self._start_attention_grabbing()

    def _start_attention_grabbing(self):
        """Start flashing to grab attention"""
        self.flash_count = 0
        self.flash_timer.start(300)  # Flash every 300ms

    def _flash_window(self):
        """Flash the window to grab attention"""
        self.flash_count += 1
        
        if self.flash_count > 10:  # Flash 5 times
            self.flash_timer.stop()
            return
            
        try:
            if sys.platform.startswith('win'):
                import ctypes
                hwnd = int(self.winId())
                # Flash both window and taskbar
                ctypes.windll.user32.FlashWindow(hwnd, True)
        except:
            pass

    def closeEvent(self, event):
        """Clean up when closing"""
        if hasattr(self, 'flash_timer'):
            self.flash_timer.stop()
        if hasattr(self, '_time_timer'):
            self._time_timer.stop()
        super().closeEvent(event)
    
    def _bring_to_front_windows(self):
        try:
            import ctypes
            hwnd = int(self.winId())
            ctypes.windll.user32.ShowWindow(hwnd, 4)  # SW_SHOWNOACTIVATE
            ctypes.windll.user32.SetWindowPos(
                hwnd, -1, 0, 0, 0, 0, 
                0x0001 | 0x0002 | 0x0020  # SWP_NOSIZE | SWP_NOMOVE | SWP_SHOWWINDOW
            )
        except Exception as e:
            print(f"Windows bring to front failed: {e}")