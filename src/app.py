import sounddevice as sd
from PIL import Image, ImageTk
import tkinter as tk
import os

# File path
script_dir = os.path.dirname(os.path.abspath(__file__))

# Images path
mouth_shut_image_path = os.path.join(script_dir, "img/mouth-shut.png")
mouth_open_image_path = os.path.join(script_dir, "img/mouth-open.png")

# Load images
mouth_shut_image = Image.open(mouth_shut_image_path)
mouth_open_image = Image.open(mouth_open_image_path)

# Interface settings
window = tk.Tk()
window.title("Magic mouth")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Tkinter
mouth_shut_image_tk = ImageTk.PhotoImage(mouth_shut_image)
mouth_open_image_tk = ImageTk.PhotoImage(mouth_open_image)

image_item = canvas.create_image(0, 0, anchor=tk.NW, image=mouth_shut_image_tk)

# Audio settings
fs = 44100

def callback(indata, frames, time, status):
    # RMS (Root Mean Square) value
    rms_value = abs(indata).mean()

    # Set visible image in relation to RMS
    if rms_value > 0.01:
        canvas.itemconfig(image_item, image=mouth_open_image_tk)
    else:
        canvas.itemconfig(image_item, image=mouth_shut_image_tk)

# Listen to the microphone
with sd.InputStream(callback=callback, channels=1, samplerate=fs):
    # Start
    window.mainloop()
