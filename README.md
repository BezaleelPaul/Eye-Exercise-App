
EYE EXERCISE APP
                                                                                 
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


>  ![Image](https://github.com/user-attachments/assets/5bbaf6d9-cd25-467a-a053-5dae34f63ff9)
`

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
