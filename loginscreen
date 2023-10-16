# imports all required tkinter libraries
from tkinter import *
import tkinter as tk
root = Tk()
from tkinter import ttk
from tkinter import messagebox
# creates the tk gui
root.geometry()
root.geometry("510x510")
root.title("Control")

#creates the gui for the future
def createGUI(user_firstname):
  #a label for the video
  vidlabel = Label(root, text="Video")
  vidlabel.grid(row=0, column=0)
  # the actual video
  video = tk.Canvas(root, width=200, height =200,background='black')
  video.grid(row=1,column=0)
  # a label stating if there is feed
  feedlabel = Label(root, text="No Feed")
  feedlabel.grid(row=2, column=0)
  # a button for moving forward
  forwardbutton = Button(root, text="Forward")
  forwardbutton.grid(row=1,column=6)
  # a button for moving backward
  backbutton = Button(root, text="Backward")
  backbutton.grid(row=1,column=7)
  # a button for turning right
  rightbutton = Button(root, text="Right")
  rightbutton.grid(row=1,column=8)
  # a button for turning left
  leftbutton = Button(root, text="Left")
  leftbutton.grid(row=1,column=9)
  # a button for stopping
  stopbutton = Button(root, text="Stop")
  stopbutton.grid(row=2,column=6)
  # a button for logging out
  logout = Button(root, text="Logout", command=root.destroy)
  logout.grid(row=2,column=7)
  # displays a message saying "Welcome," username
  messagebox.showinfo("Logged in!", "Welcome, " + user_firstname)
