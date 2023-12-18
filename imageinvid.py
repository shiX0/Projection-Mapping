import tkinter as tk
import cv2
from PIL import Image, ImageTk

class VideoApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Open the video capture device (default camera, 0)
        self.cap = cv2.VideoCapture(0)

        # Create a label to display the video feed
        self.label = tk.Label(window)
        self.label.pack()

        # Create an Exit button
        self.exit_button = tk.Button(window, text="Exit", command=self.exit_app)
        self.exit_button.pack()

        # Initialize the video playback
        self.update()

    def exit_app(self):
        self.cap.release()
        self.window.quit()

    def update(self):
        # Read a frame from the video source
        ret, frame = self.cap.read()

        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to a PhotoImage object and display it on the label
            img = Image.fromarray(frame_rgb)
            img = ImageTk.PhotoImage(image=img)
            self.label.img = img
            self.label.configure(image=img)

        # Repeat this update method every 10 milliseconds
        self.window.after(10, self.update)

# Create a Tkinter window
root = tk.Tk()
app = VideoApp(root, "Video Player")

root.mainloop()
