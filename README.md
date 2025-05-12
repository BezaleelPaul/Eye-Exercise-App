
 _______           _______    _______           _______  _______  _______ _________ _______  _______ 
(  ____ \|\     /|(  ____ \  (  ____ \|\     /|(  ____ \(  ____ )(  ____ \\__   __/(  ____ \(  ____ \
| (    \/( \   / )| (    \/  | (    \/( \   / )| (    \/| (    )|| (    \/   ) (   | (    \/| (    \/
| (__     \ (_) / | (__      | (__     \ (_) / | (__    | (____)|| |         | |   | (_____ | (__    
|  __)     \   /  |  __)     |  __)     ) _ (  |  __)   |     __)| |         | |   (_____  )|  __)   
| (         ) (   | (        | (       / ( ) \ | (      | (\ (   | |         | |         ) || (      
| (____/\   | |   | (____/\  | (____/\( /   \ )| (____/\| ) \ \__| (____/\___) (___/\____) || (____/\
(_______/   \_/   (_______/  (_______/|/     \|(_______/|/   \__/(_______/\_______/\_______)(_______/
                                                                                                     






---

# 👁️ Eye Exercises App

**A sleek desktop app designed to protect your vision.** This lightweight, minimal tool reminds users to take regular screen breaks and do simple eye exercises—crucial for long coding sessions or screen-heavy workflows.

🧠 _Built with Python, featuring a modern dark-mode GUI and system tray integration._

---

## 🚀 Features

- ⏰ **Custom periodic reminders** for eye relief exercises
- 🌙 **Dark mode UI** with Discord-inspired aesthetics
- 🪟 **System tray support** using `pystray`
  - Start / Pause reminders
  - Exit gracefully
- 💻 Designed to run in the background with minimal distraction

---

## 📸 Screenshot

> _You can paste a screenshot here to show the app UI_  
> Example: `![App Screenshot](assets/screenshot.png)`

---

## 🛠️ Technologies Used

- `Python 3.13`
- `Tkinter` for GUI
- `pystray` for system tray
- `PIL` for icon rendering
- `threading`, `time`, and `sys` for background logic

---

## 📦 Building the EXE (optional)

If you want to create a standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed eye_exercises_app.py
