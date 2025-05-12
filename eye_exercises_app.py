import customtkinter as ctk
from tkinter import messagebox
import threading
import time
import pystray
from PIL import Image, ImageDraw
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class EyeExerciseApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Eye Exercise Assistant")
        self.geometry("600x500")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.hide_window)

        self.total_seconds = 20 * 60  # 20 minutes
        self.remaining_seconds = self.total_seconds
        self.timer_running = False
        self.app_running = True  # Used for safely terminating thread

        self.create_widgets()
        self.create_tray_icon()
        self.start_timer_thread()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="👁️ Eye Exercise Assistant", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=15)

        self.timer_label = ctk.CTkLabel(self, text=self.format_time(self.remaining_seconds), font=ctk.CTkFont(size=30, weight="bold"))
        self.timer_label.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        self.check_frame = ctk.CTkFrame(self)
        self.check_frame.pack(pady=20)

        self.check_20 = ctk.CTkCheckBox(self.check_frame, text="20-20-20 Rule")
        self.check_palming = ctk.CTkCheckBox(self.check_frame, text="Palming")
        self.check_rotation = ctk.CTkCheckBox(self.check_frame, text="Circular Eye Rotation")
        self.check_focus = ctk.CTkCheckBox(self.check_frame, text="Focus Shifting")

        self.check_20.pack(anchor="w", pady=3)
        self.check_palming.pack(anchor="w", pady=3)
        self.check_rotation.pack(anchor="w", pady=3)
        self.check_focus.pack(anchor="w", pady=3)

        self.reset_button = ctk.CTkButton(self, text="🔄 Reset Timer & Checklist", command=self.reset_all)
        self.reset_button.pack(pady=20)

    def format_time(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02}:{secs:02}"

    def update_timer(self):
        while self.app_running:
            if self.timer_running and self.remaining_seconds > 0:
                self.remaining_seconds -= 1
                percent = 1 - (self.remaining_seconds / self.total_seconds)

                try:
                    if self.winfo_exists():
                        self.after(0, lambda: self.timer_label.configure(text=self.format_time(self.remaining_seconds)))
                        self.after(0, lambda: self.progress_bar.set(percent))
                except Exception as e:
                    print("UI update error:", e)

                time.sleep(1)

            elif self.remaining_seconds == 0 and self.timer_running:
                self.timer_running = False
                self.show_reminder()
                time.sleep(1)

            else:
                time.sleep(0.2)

    def start_timer_thread(self):
        self.timer_running = True
        threading.Thread(target=self.update_timer, daemon=True).start()

    def show_reminder(self):
        if self.winfo_exists():
            self.after(100, lambda: messagebox.showinfo("Reminder", "20 minutes done!\nTime to do your eye exercises. ✅"))

    def reset_all(self):
        self.remaining_seconds = self.total_seconds
        if self.winfo_exists():
            self.timer_label.configure(text=self.format_time(self.remaining_seconds))
            self.progress_bar.set(0)
            self.check_20.deselect()
            self.check_palming.deselect()
            self.check_rotation.deselect()
            self.check_focus.deselect()
        self.timer_running = True

    def create_tray_icon(self):
        def create_image():
            image = Image.new("RGB", (64, 64), color="black")
            draw = ImageDraw.Draw(image)
            draw.ellipse((16, 16, 48, 48), fill="blue")
            return image

        def on_quit(icon, item):
            self.app_running = False  # Stop the background thread
            icon.stop()  # Stop the tray icon
            self.after(0, self.quit)  # Gracefully quit the tkinter main loop


        def on_show(icon, item):
            self.after(0, self.deiconify)

        menu = pystray.Menu(
            pystray.MenuItem("Show App", on_show),
            pystray.MenuItem("Quit", on_quit)
        )

        self.icon = pystray.Icon("eye_exercise_tray", create_image(), "Eye Exercise Assistant", menu)

        def run_tray():
            self.icon.run()

        threading.Thread(target=run_tray, daemon=True).start()

    def hide_window(self):
        self.withdraw()

if __name__ == "__main__":
    app = EyeExerciseApp()
    app.mainloop()
