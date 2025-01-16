from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import pygame
from pygame import mixer

# Initialize pygame mixer
mixer.init()

# Initialize tkinter
root = Tk()
root.geometry("1000x500")

# Set window to stay on top
root.attributes("-topmost", True)

# Load GIF and audio file
img = Image.open("chitti-img1.gif")
frames = [ImageTk.PhotoImage(img.resize((1000, 500))) for img in ImageSequence.Iterator(img)]

# Function to play GIF
def play_gif(frame_index=0):
    if frame_index == 0:  # Start audio when the GIF starts
        mixer.music.load("audio-chitti.mp3")
        mixer.music.play()

    # Set the current frame
    lbl.config(image=frames[frame_index])
    frame_index += 1

    # Check if it's the last frame
    if frame_index < len(frames):
        # Schedule the next frame with a reduced delay for faster speed
        root.after(40, play_gif, frame_index)
    else:
        # Close the window after playing the GIF once
        root.destroy()

# Set up label to display GIF
lbl = Label(root)
lbl.place(x=0, y=0)

# Start playing GIF
play_gif()
root.mainloop()



