
# impor libraries
import tkinter as tk
# this pillow library which reads image and also convert array to image
from PIL import Image, ImageTk
import cv2 as cv

############## Window Setup #################
# Setupt the window
window = tk.Tk()
# set the title of window
window.title("OpenCV Basics")
# set the size of window
window.geometry("1000x600")
# disable the resizing so that window remains original size 
window.resizable(width=False, height=False)
############## Window Setup #################

# create a label to capture the video frames
label = tk.Label(window)
label.grid(row=80, column=80)

# capture the webcam
cap = cv.VideoCapture(0)
# setting the frame size
cap.set(3, 500) # width
cap.set(4, 400) # height

# define function to show the frames
def show_frames():
    # read the frame
    Success, frame = cap.read()
    # flip frame
    frame = cv.flip(frame, 1)  # 1 for flip on y and 0 for flip on x -1 means flip on both x and y
    # convert to RGB
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # this frame is readed in the form of array so you need to convert
    # it to image using pillow libray Image module
    img = Image.fromarray(frame)
    # now convert this image into Photoimage
    imgtk = ImageTk.PhotoImage(image=img)
    # now give this photo image to label
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # repeat after an interval to capture continiously
    label.after(20, show_frames)


# show frames
show_frames()
# run the application
window.mainloop()