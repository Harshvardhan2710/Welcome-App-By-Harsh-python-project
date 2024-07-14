from tkinter import *
from datetime import *

root = Tk()
root.title("Welcome App by harsh")
root.geometry("500x500+100+50")
f = ("Arial", 30, "bold")

def welcome():
	name = ent_name.get()
	dt = datetime.now()
	hr = dt.hour
	if hr < 12:
		msg = "Good Morning " + name
	elif hr < 16:
		msg = "Good Afternoon " + name
	else:
		msg = "Good Evening " + name
	lab_ans.configure(text=msg)

lab_name = Label(root, text="Enter Name", font=f)
ent_name = Entry(root, font=f)
btn_submit = Button(root, text="submit", font=f, command=welcome)
lab_ans = Label(root, font=f)

lab_name.pack(pady=20)
ent_name.pack(pady=20)
btn_submit.pack(pady=20)
lab_ans.pack(pady=20)

root.mainloop()