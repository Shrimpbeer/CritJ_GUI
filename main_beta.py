# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

##################### Data ######################################################
# dont change this
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
        58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

##################### Data input ################################################
#change these three arrays, X Y Position and Criticality
xList = [0, 2, 1, 1, 0, 0, -1, -3, -2, -2, -3, -4, -3, -5, -6, -8, -8, -6, -8, -10, -11, -12, -10, -9, -9, -10, -10,
         -11, -9, -8, -8, -6, -4, -4, -5, -6, -8, -6, -4, -5, -6, -7, -6, -7, -7, -7, -5, -3, -5, -5, -7, -9, -8, -10,
         -12, -13, -14, -15, -16, -18, -20, -22, -23, -23, -22, -21, -19, -17, -18, -19, -19, -20, -19, -21, -20, -19,
         -18]
yList = [0, -1, -1, 0, 1, 0, 2, 4, 2, 0, -1, -3, -1, -1, -1, 0, 2, 3, 2, 4, 2, 2, 2, 4, 2, 0, 0, -2, -2, 0, 2, 1, 1, 1,
         3, 5, 7, 9, 10, 9, 7, 7, 5, 6, 7, 7, 8, 6, 6, 8, 9, 10, 8, 8, 10, 9, 8, 7, 9, 9, 10, 8, 9, 8, 10, 12, 14, 15,
         16, 18, 17, 17, 16, 18, 19, 17, 19]
K_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
        58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

Ego_v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
        58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

##################### find the boundary for plot ################################
max_x = -500
min_x = 500
max_y = -500
min_y = 500
max_k = -500
min_k = 500
max_ev = -500
min_ev = 500

for e in xList:
    if e > max_x:
        max_x = e
    if e < min_x:
        min_x = e
for e in yList:
    if e > max_y:
        max_y = e
    if e < min_y:
        min_y = e
for e in K_value:
    if e > max_k:
        max_k = e
    if e < min_k:
        min_k = e
for e in Ego_v:
    if e > max_ev:
        max_ev = e
    if e < min_ev:
        min_ev = e

################ Initialization ##########################################
window = tk.Tk()
window.title("Cute Picture") # 摸摸哒
window.geometry("800x800")

############## Frame 1 / upper area of GUI ###############################

frame1 = tk.Frame(height=400, width=800)
frame1.pack()
# tk.Label(window, text="小车位置", bg="gray", font=LARGE_FONT).pack()

f = Figure(figsize=(10, 8), dpi=80)

a = f.add_subplot(221)
b = f.add_subplot(222)
c = f.add_subplot(212)

a.set(xlim=[min_x, max_x], ylim=[min_y, max_y], title="Position", xlabel="X Position", ylabel="Y Position")
a.plot(xList[0], yList[0], "-ro")

b.set(xlim=[0, 75], ylim=[min_k, max_k], title="Criticality trajectory", xlabel="Time", ylabel="Criticality")
b.plot(time, K_value, "-g")
MarkersOn = [0]
b.plot(0, K_value[0], "-gD", markevery=MarkersOn)
# b.annotate(str(K_value[0]), xy=(0, K_value[0]+5))
b.text(10, max_k*0.8, "Criticality = " + str(K_value[0]),
       bbox={"facecolor": "red", "alpha": 0.5, "pad": 10})

c.set(xlim=[0, 75], ylim=[min_ev, max_ev], title="Ego car velocity", xlabel="Time", ylabel="Velocity")
c.plot(time, Ego_v, "-b")
MarkersOn_v = [0]
c.plot(0, Ego_v[0], "-bs", markevery=MarkersOn_v)

f.tight_layout()
canvas = FigureCanvasTkAgg(f, frame1)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

############## Frame 2 / The Scale / slider ##############################
frame2 = tk.Frame(height=0, width=400)
frame2.pack()
l = tk.Label(window, fg="black", font=LARGE_FONT, width=30, height=2, text="Initial position and criticality")
l.pack()

#### Scale will triger this function to show the actual value in slider ##
def print_selection(v):
    realtime = float(v)/10
    l.config(text="Time point: " + str(realtime) + " second")
    a.clear()
    b.clear()
    c.clear()
    a.set(xlim=[min_x, max_x], ylim=[min_y, max_y], title="Position", xlabel="X Position", ylabel="Y Position")
    a.plot(xList[int(v)], yList[int(v)], "-ro")

    b.set(xlim=[0, 75], ylim=[min_k, max_k], title="Criticality trajectory", xlabel="Time", ylabel="Criticality")
    b.plot(time, K_value, "-g")
    MarkersOn = int(v)
    b.plot(int(v), K_value[int(v)], "-gD", markevery=MarkersOn)
    # b.annotate(str(K_value[int(v)]), xy=(int(v), K_value[int(v)] + 5))
    b.text(10, max_k * 0.8, "Criticality = " + str(K_value[int(v)]),
           bbox={"facecolor": "red", "alpha": 0.5, "pad": 10})

    c.set(xlim=[0, 75], ylim=[min_ev, max_ev], title="Ego car velocity", xlabel="Time", ylabel="Velocity")
    c.plot(time, Ego_v, "-b")
    MarkersOn_v = int(v)
    c.plot(int(v), Ego_v[int(v)], "-bs", markevery=MarkersOn_v)

    canvas.draw()
   # b.clear()

######The scale/Slider that can set to be at a time point and trigered to show position and criticality###
s = tk.Scale(window, from_=0, to=75, orient=tk.HORIZONTAL, length=400, showvalue=0, tickinterval=5, \
             resolution=1, command=print_selection)
s.pack()

###############################################
window.mainloop()