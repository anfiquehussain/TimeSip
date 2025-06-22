# ⏱️ TimeSip

**TimeSip** is a minimalist and powerful desktop reminder application built with PyQt5. It helps you set reminders effortlessly and stay on track with tasks by offering full-screen alerts, snooze functionality, and tray integration.

---

## 🚀 Features

- ⏰ Set reminders in seconds, minutes, hours, days, months, or years  
- 💬 Custom reminder messages  
- 🔄 Restart or snooze reminders directly from popups  
- 🖥️ Full-screen popup alerts that grab your attention  
- 🗃️ System tray integration – minimizes to tray on close  

---

## 🧰 Tech Stack

Built with:

- `PyQt5` for the UI  
- `PyInstaller` for packaging into an executable  
- `pefile`, `pywin32-ctypes` for Windows-specific support  
- Cross-platform support with clean modular structure

## 📦 Installation
### Clone the repo
```
git clone https://github.com/anfiquehussain/TimeSip.git
```
```
cd TimeSip
```

### Create a virtual environment
```
python -m venv venv
```
```
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run the app
```
python main.py
```
## 💡 Roadmap
- Sound alert option
- Multi-reminder support
- Reminder history/logs
- Auto-start on boot (Windows/Mac)
