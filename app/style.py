# For current datetime label
HOME_LIVE_DATE = """
QLabel {
    color: #FACC15;
    font-size: 18px;
    font-weight: bold;
    background-color: transparent;
}
"""

# For countdown label
HOME_COUNTDOWN = """
QLabel {
    color: #22D3EE;
    font-size: 16px;
    font-weight: bold;
    background-color: transparent;
}
"""

# For stop reminder button (Red theme)
HOME_STOP_BUTTON = """
QPushButton {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #EF4444,
        stop: 1 #DC2626
    );
    color: white;
    border: none;
    padding: 8px 14px;
    border-radius: 6px;
    font-weight: bold;
    font-size: 14px;
}
QPushButton:hover {
    background-color: #B91C1C;
}
QPushButton:pressed {
    background-color: #991B1B;
}
"""

# Optional: You can use this in the global/main stylesheet
HOME_MAIN_STYLE = """
QWidget {
    background-color: #1C1A27;
    color: #E2E8F0;
    font-family: Segoe UI, sans-serif;
}

QGroupBox {
    border: 2px solid #64748B;
    border-radius: 8px;
    margin-top: 30px;
    padding: 17px;
    font-weight: bold;
    color: #F8FAFC;
    font-size: 15px;
    background-color: rgba(255, 255, 255, 0.03);
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    background-color: transparent;
}

QLabel {
    color: #F1F5F9;
    background-color: transparent;
    font-size: 15px;
}

QLineEdit {
    border: 1px solid #94A3B8;
    background-color: #0F172A;
    color: #F8FAFC;
    border-radius: 6px;
    padding: 8px;
    font-size: 14px;
}

QComboBox {
    border: 1px solid #94A3B8;
    background-color: #1E293B;
    color: #F8FAFC;
    border-radius: 6px;
    padding: 6px;
    min-width: 100px;
    font-size: 15px;
}

QComboBox QAbstractItemView {
    background-color: #1E293B;
    color: #F8FAFC;
    selection-background-color: #3B82F6;
    border: 1px solid #94A3B8;
}

QPushButton {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #2C3A5A,
        stop: 1 #1E2A47
    );
    color: #E2E8F0;
    border: 1px solid #334155;
    padding: 10px 15px;
    border-radius: 6px;
    font-weight: bold;
    font-size: 14px;
}

QPushButton:hover {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #3B4D6D,
        stop: 1 #2A3A58
    );
    border: 1px solid #475569;
}

QPushButton:pressed {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #1E293B,
        stop: 1 #1C2433
    );
    border: 1px solid #334155;
}

"""

REMINDER_RUNNING =  """
QPushButton {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #2C3A5A,
        stop: 1 #1E2A47
    );
    color: #E2E8F0;
    border: 1px solid #334155;
    padding: 10px 15px;
    border-radius: 6px;
    font-weight: bold;
    font-size: 14px;
}

QPushButton:hover {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #3B4D6D,
        stop: 1 #2A3A58
    );
    border: 1px solid #475569;
}

QPushButton:pressed {
    background: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 0,
        stop: 0 #1E293B,
        stop: 1 #1C2433
    );
    border: 1px solid #334155;
}
"""

# For start reminder button (Blue theme)
START_BUTTON = """
QPushButton {
    background-color: #3b82f6;
    color: white;
    border: none;
    padding: 15px 25px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    min-width: 180px;
}
QPushButton:hover {
    background-color: #2563eb;
}
"""

IMAGE_LABEL_STYLE = """
QLabel {
    border: 2px solid transparent;
    border-radius: 8px;
    padding: 5px;
    background-color: #F8F8FB;
}
QLabel:hover {
    border: 2px solid #3b82f6;
    background-color: #dbeafe;
}
"""



POPUP_STYLES = {
    "dialog": "background-color: #1C1A27;",
    "title": """
        font-size: 42px;
        font-weight: bold;
        color: white;
        margin-bottom: 20px 0;
    """,
    "message": """
        font-size: 28px;
        color: #C084FC;
        font-weight: bold;
        margin: 20px 0;
    """,
    "time_label": "font-size: 25px; color: #64748b;",
    "triggered_label": "font-size: 16px; color: #94a3b8;",
    "restart_button": """
        QPushButton {
            background-color: #10b981;
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            min-width: 180px;
        }
        QPushButton:hover {
            background-color: #059669;
        }
    """,
    "snooze_button": """
        QPushButton {
            background-color: #f59e0b;
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            min-width: 180px;
        }
        QPushButton:hover {
            background-color: #d97706;
        }
    """,
    "close_button": """
        QPushButton {
            background-color: #3b82f6;
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            min-width: 180px;
        }
        QPushButton:hover {
            background-color: #2563eb;
        }
    """
}
