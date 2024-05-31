import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import threading
import time

class UserPrompt:
    def __init__(self, root):
        self.root = root
        self.root.title("User Details Prompt")
        self.root.attributes('-topmost', True)  # Keep the window on top
        self.root.overrideredirect(True)  # Remove window decorations
        
        # Load logo image
        logo_image = Image.open("KNLS.png")  # Replace "KNLS.png" with your logo image file
        logo_image = logo_image.resize((100, 100))
        self.logo_photo = ImageTk.PhotoImage(logo_image)
        
        # Create a frame for the logo
        self.logo_frame = tk.Frame(root)
        self.logo_frame.pack(side=tk.TOP, fill=tk.X)
        self.logo_label = tk.Label(self.logo_frame, image=self.logo_photo)
        self.logo_label.pack(pady=10)
        
        self.frame = tk.Frame(root, bd=4, relief=tk.RAISED)
        self.frame.pack_propagate(False)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.pack(padx=10, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack(padx=20, pady=5)
        
        self.phone_label = tk.Label(self.frame, text="Phone Number:")
        self.phone_label.pack(padx=10, pady=5)
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.pack(padx=20, pady=5)

        self.email_label = tk.Label(self.frame, text="Email:")
        self.email_label.pack(padx=10, pady=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack(padx=20, pady=5)

        self.purpose_label = tk.Label(self.frame, text="Purpose:")
        self.purpose_label.pack(padx=10, pady=5)
        
        self.purpose_var = tk.StringVar()
        self.study_radiobutton = tk.Radiobutton(self.frame, text="Study", variable=self.purpose_var, value="Study")
        self.study_radiobutton.pack(padx=10, pady=5)
        self.research_radiobutton = tk.Radiobutton(self.frame, text="Research", variable=self.purpose_var, value="Research")
        self.research_radiobutton.pack(padx=10, pady=5)
        
        self.id_label = tk.Label(self.frame, text="ID:")
        self.id_label.pack(padx=10, pady=5)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.pack(padx=20, pady=5)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit_details, bg="blue", fg="white")
        self.submit_button.pack(padx=10, pady=10)
        
        # Center the window on the screen and occupy half of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width = screen_width // 2
        height = screen_height // 2
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Make the window modal
        self.root.grab_set()
        self.root.focus_set()
        
        # Bind the close button to prevent closing the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.root.wait_window()
        
    def submit_details(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        purpose = self.purpose_var.get()
        user_id = self.id_entry.get()
        
        if not name or not phone_number:
            messagebox.showwarning("Input Error", "Both Name and phone number are required.")
            return
        
        self.root.destroy()  # Close the prompt window
        
        # Allocate time slot
        current_time = datetime.now()
        end_time = current_time + timedelta(hours=2)
        
        welcome_message = f"Welcome, {name}, to KNLS E-learning. Your session ends at {end_time.strftime('%H:%M')} after two hours."
        messagebox.showinfo("Welcome", welcome_message)
        
        # Here you would save the user details and the time slot to a file or database
        
        # Schedule prompt to appear again after two hours
        threading.Thread(target=self.schedule_next_prompt, args=(end_time,)).start()
        
        print(f"Details Submitted:\nName: {name}\nPhone Number: {phone_number}\nEmail: {email}\nPurpose: {purpose}\nID: {user_id}\nSession Ends: {end_time}")
        
    def schedule_next_prompt(self, end_time):
        current_time = datetime.now()
        time_to_wait = (end_time - current_time).total_seconds()
        if time_to_wait > 0:
            time.sleep(time_to_wait)
        self.main()  # Restart the prompt

    def on_close(self):
        # Override closing behavior
        pass

    @staticmethod
    def main():
        root = tk.Tk()
        app = UserPrompt(root)
        root.mainloop()

if __name__ == "__main__":
    UserPrompt.main()
