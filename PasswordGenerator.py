from tkinter import*
from tkinter import ttk
import string
import random 
class pg:
    def __init__(self,root):
        self.root=root
        self.root.title("Password Generator")
        self.root.geometry("350x450")
        self.root.resizable(0,0)
        self.root.config(bg="#f0ffff")
        
        
        
        def generator():
            small_a=string.ascii_lowercase
            capital_a=string.ascii_uppercase
            number=string.digits
            special_ch=string.punctuation
            all=small_a + capital_a + special_ch + number
            all1=small_a + capital_a
            password_length=int(self.length_box.get())
            
            if choice.get()==1:
                self.e1.insert(0,random.sample(small_a,password_length))
            if choice.get()==2:
                self.e1.insert(0,random.sample(all1,password_length))
            if choice.get()==3:
                self.e1.insert(0,random.sample(all,password_length))
            #password=random.sample(all,password_length)
            #self.e1.insert(0,password)
        def clear():
            global expression
            expression=""
            input_text.set("")
        def click(item):
            global expression
            expression=expression+str(item)
            input_text.set(expression)
        expression=""
        input_text=StringVar()
            
            
            
        self.l1=Label(self.root,text="",bd="7",bg="#48d1cc")
        self.l1.pack(side="top",fill=BOTH)
        self.l2=Label(self.root,text="Password Generator",font="Minion 15 bold",bd="15",bg="white",fg="black")
        self.l2.pack(side="top",fill=BOTH)
        self.l3=Label(self.root,text="Password Strength",font="ariel 12",bg="#f0ffff",fg="#008080")
        self.l3.place(x=105,y=100)
        self.l4=Label(self.root,text="Password Length",bg="#f0ffff",fg="#008080",font="ariel 12")
        self.l4.place(x=105,y=250)
        self.b1=Button(self.root,text="Generate",width="12",bd="2",height="1",font="ariel 11",bg="#48d1cc",command=generator)
        self.b1.place(x=110,y=320)
        self.b2=Button(self.root,text="reset",width="12",bd="2",height="1",font="ariel 11",bg="#48d1cc",command=lambda:clear())
        self.b2.place(x=110,y=380)
        self.e1=Entry(self.root,textvariable=input_text,width=18,bd=2,font="ariel 12")
        self.e1.place(x=84,y=355)
        
        choice=IntVar()
        self.r1=Radiobutton(self.root,text="weak",bg="white",font="ariel 10",value=1,variable=choice)
        self.r1.place(x=135,y=125)
        self.r2=Radiobutton(self.root,text="medium",bg="white",font="ariel 10",value=2,variable=choice)
        self.r2.place(x=135,y=165)
        self.r3=Radiobutton(self.root,text="strong",bg="white",font="ariel 10",value=3,variable=choice)
        self.r3.place(x=135,y=205)
        
        self.length_box=Spinbox(self.root,from_=5,to_=15,width=6,font="ariel 10")
        self.length_box.place(x=140,y=275)
        

def main(): 
    root=Tk()
    gui=pg(root)
    root.mainloop()
    
if __name__=="__main__":
    main()