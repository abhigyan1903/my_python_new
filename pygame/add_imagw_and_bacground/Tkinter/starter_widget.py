from tkinter import *
from datetime import date as d
window=Tk()
window.title("getting started with widgets in tkinter")
window.geometry("600x600")
label_1=Label(window,text="Hey There!!",fg="white",bg="black",width=300,height=5)
label=Label(window,text="Enter Your Name",fg="black",bg="red",width=50,height=2)
entry=Entry()

def display():
    name=entry.get()
    global message    
    message="Welcoome to this aplication \n Todays date is : "
    greet="hello   "+name +" \n"
    text_box.insert(END,greet)      
    text_box.insert(END,message)
    text_box.insert(END,d.today())
        
    
    
button=Button(window,text="Submit",fg="black",bg="yellow",width=20,height=2,command=display)
text_box=Text(height=5,bg="lightblue",)


label_1.pack()
label.pack()
entry.pack()
button.pack()
text_box.pack()
window.mainloop()