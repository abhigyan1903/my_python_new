from tkinter import *
window=Tk()
window.title("product of two numbers")
window.geometry("600x600")
label_1=Label(window,text="Hey There!!",fg="white",bg="black",width=300,height=5)
label_2=Label(window,text="Enter Your First Number",fg="black",bg="dodgerblue",width=50,height=2)
label_3=Label(window,text="Enter Your Second Number",fg="black",bg="dodgerblue",width=50,height=2)
entry_1=Entry()
entry_2=Entry()
text_box=Text(height=5,bg='lightblue')
def product():
      num1=entry_1.get()
      num2=entry_2.get()
      result="The product of your numbers is   :",int(num1)*int(num2)
      text_box.insert(END,result)

button=Button(window,text="MUltiply",fg="Black",bg="yellow",width=20,height=2,command=product)



label_1.pack()
label_2.pack()
entry_1.pack()
label_3.pack()
entry_2.pack()
button.pack()
text_box.pack()
window.mainloop()