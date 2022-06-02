from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    tick_label.config(text='')

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60

    if reps % 2 == 1 and reps != 9:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=RED)
    else:
        reset_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global reps
    global timer

    count_min = math.floor(count/60)
    count_second = count % 60
    if count_second in range(10):
        count_second = str(0) + str(count_second)

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_second}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_label.config(text='✔'*int(reps/2))
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 50, 'normal'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

window.mainloop()