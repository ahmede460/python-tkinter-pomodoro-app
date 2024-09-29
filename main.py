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
def reset():
   window.after_cancel(timer)
   canvas.itemconfig(timer_text, text= f"00:00")
   rounds_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
   
    if reps % 2 == 0:
       count_down_minutes(WORK_MIN * 60)
    else:
       count_down_minutes(SHORT_BREAK_MIN * 60)
       


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down_minutes(count):
    global timer
    r_text = ""
    mins = math.floor(count/60)
    secs = count % 60
    if secs < 10:
       secs = f"0{secs}"
    # if mins < 10:
    #    secs = f"0{mins}"
    timer = window.after(1000,count_down_minutes,count - 1)
    if count > -1:
      canvas.itemconfig(timer_text, text= f"{mins}:{secs}")
    
    global reps 
    if count == 0:
        reps +=1
        session = math.floor(reps/2)
        for _ in range(session):
            r_text +="✅"
        rounds_label.config(text=r_text)
        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO APP")
window.minsize(width=350,height=450)
window.config(bg=YELLOW)

canvas = Canvas(height=250,width=210,bg=YELLOW, highlightthickness=0)
tomato_foto = PhotoImage(file="./tomato.png")
tomato_img = canvas.create_image(103,112, image= tomato_foto)
timer_text = canvas.create_text(103,135, text="00:00",fill="black",font=(FONT_NAME, 24, "bold"))
canvas.place(x=80,y=100)

#Buttons

start_button = Button(text="START",width=10,command=start_timer)
start_button.place(x=20,y=340)

reset_button = Button(text="RESET",width=10, command=reset)
reset_button.place(x=250,y=340)



#Labels

main_title = Label(text="TIMER",font=(FONT_NAME, 24, "bold"),bg=YELLOW, fg=RED)
main_title.place(x=130,y=0)

rounds_label = Label(text="",font=(FONT_NAME, 24, "bold"),bg=YELLOW,fg=GREEN)
rounds_label.place(x=80,y=380)


window.mainloop()
