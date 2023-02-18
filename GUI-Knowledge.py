from tkinter import *
from tkinter import ttk #theme
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมเตือนงานที่ต้องทำ')
GUI.geometry('500x400')

L1 = Label(GUI,text='โปรแกรมเตือนงานที่ต้องทำ',font=50,fg='blue')
L1.place(x=180,y=50)
####################
def Button1():
    text = ('การบ้่านคณิต,ส่งการบ้านลุง')
    messagebox.showinfo('วันนี้',text)

FB1 = LabelFrame(GUI,text='to do')
FB1.place(x=200,y=100)
B1 = ttk.Button(FB1,text='วันนี้',command=Button1)
B1.pack(ipadx=20,ipady=20)
####################
def Button2():
    text = ('สรุปเนื้อหาชีวะ')
    messagebox.showinfo('วันพรุ่งนี้',text)

FB2 = Frame(GUI)
FB2.place(x=200,y=200)
B2 = ttk.Button(FB1,text='วันพรุ่งนี้',command=Button2)
B2.pack(ipadx=20,ipady=20)
####################
def Button3():
    text = ('อ่าน short story จบ')
    messagebox.showinfo('ภายในอาทิตย์นี้',text)

FB3 = Frame(GUI)
FB3.place(x=200,y=300)
B3 = ttk.Button(FB1,text='ภายในอาทิตย์นี้',command=Button3)
B3.pack(ipadx=20,ipady=20)
####################
GUI.mainloop()
