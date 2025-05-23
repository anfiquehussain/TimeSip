from PyQt5.QtWidgets import QApplication

def center_on_screen(widget):
    frame_geo = widget.frameGeometry()
    center_point = QApplication.desktop().availableGeometry().center()
    frame_geo.moveCenter(center_point)
    widget.move(frame_geo.topLeft())


def convert_to_seconds(value, unit):
    conversions = {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days": 86400,
        "Months": 2592000,  # 30 days
        "Years": 31536000   # 365 days
    }
    return value * conversions.get(unit, 60)