from Tkinter import Tk, Label, Entry, Button

my_app=Tk(className='PERSONAL IDENTITY')
L1=Label(my_app, text="Personal Identity", font=('Arial', 24))
L1.grid(row=0,column=0)
L2=Label(my_app, text="Name")
L2.grid(row=1,column=0, sticky='w')
L3=Label(my_app, text="Muhammad Irfan")
L3.grid(row=1, column=1)
L4=Label(my_app, text="NIM")
L4.grid(row=2, column=0, sticky='w')
L5=Label(my_app, text="L200184165")
L5.grid(row=2,column=1, sticky='w')
L6=Label(my_app, text="Favourite Book")
L6.grid(row=3, column=0, sticky='w')
L7=Label(my_app, text="Konspirasi Alam Semesta")
L7.grid(row=3, column=1, sticky='w')
L8=Label(my_app, text="Idola dikalangan sahabat")
L8.grid(row=4, column=0, sticky='w')
L9=Label(my_app, text="Abu Bakar")
L9.grid(row=4, column=1, sticky='w')
L10=Label(my_app, text="Motto")
L10.grid(row=5, column=0, sticky='w')
L11=Label(my_app, text="JUST DO IT")
L11.grid(row=5, column=0, sticky='w')
def close():
    my_app.destroy()
B=Button(my_app, text='Close', command=close)
B.grid(row=6,column=1)
my_app.mainloop()
