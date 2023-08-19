from tkinter import*
root=Tk()
root.title("Simple Calculator")
root.geometry("295x420")
root.resizable(0,0)
root.config(bg="#9E9E9E")
#l1=Label(root,text="",height=3)
#l1.pack(side="top",fill=BOTH)

def click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)
def clear():
    global expression
    expression=""
    input_text.set("")
def equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""
expression=""
input_text=StringVar()
e1=Entry(root,font="ariel,15",textvariable=input_text,width=24,bg="#eee",bd=5,justify=RIGHT)
e1.place(x=6,y=6)

b1=Button(root,text="1",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("1"))
b1.place(x=10,y=60)
b2=Button(root,text="2",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("2"))
b2.place(x=80,y=60)
b3=Button(root,text="3",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("3"))
b3.place(x=150,y=60)
b4=Button(root,text="4",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("4"))
b4.place(x=10,y=130)
b5=Button(root,text="5",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("5"))
b5.place(x=80,y=130)
b6=Button(root,text="6",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("6"))
b6.place(x=150,y=130)
b7=Button(root,text="7",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("7"))
b7.place(x=10,y=200)
b8=Button(root,text="8",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("8"))
b8.place(x=80,y=200)
b9=Button(root,text="9",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("9"))
b9.place(x=150,y=200)
b0=Button(root,text="0",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#37474F",command=lambda:click("0"))
b0.place(x=10,y=270)
b11=Button(root,text=".",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#B0BEC5",command=lambda:click("."))
b11.place(x=80,y=270)
b12=Button(root,text="=",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="Orange",command=lambda:equal())
b12.place(x=150,y=270)
b13=Button(root,text="+",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#B0BEC5",command=lambda:click("+"))
b13.place(x=220,y=270) 
b14=Button(root,text="-",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#B0BEC5",command=lambda:click("-"))
b14.place(x=220,y=200)
b15=Button(root,text="*",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#B0BEC5",command=lambda:click("*"))
b15.place(x=220,y=130)
b16=Button(root,text="/",width=5,height=2,bd=1,font="ariel,15",fg="white",bg="#B0BEC5",command=lambda:click("/"))
b16.place(x=220,y=60)
b17=Button(root,text="AC",width=24,height=2,bd=1,font="ariel,15",fg="white",bg="DodgerBlue",command=lambda:clear())
b17.place(x=10,y=340)
root.mainloop()
