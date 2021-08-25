from tkinter import Tk, mainloop, Label
# from tkinter.ttk import Label
from time import strftime

refresh_milisecond = 200
 
# creating tkinter window
root = Tk()
root.title('Clock')
 
# This function is used to  display time on the label
def time():
    string = strftime('%H:%M:%S')
    # string = strftime('%I:%M:%S %p')
    lbl.config(text = string)
    lbl.after(refresh_milisecond, time)
 
# Styling the label widget 

lbl = Label(root, font= ('calibri', 42, 'bold'),bg ='cyan',fg= 'red')

# Placing clock at the centre of the tkinter window
lbl.pack(anchor = 'center')

time()
mainloop()