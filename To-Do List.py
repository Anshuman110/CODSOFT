from tkinter import*
from tkinter import messagebox
from tkinter import ttk
class todo:
    def __init__(self,root):
        self.root=root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.root.config(bg="#cadcfe")
        root.resizable(0,0)
        self.l1=Label(self.root,text="To-Do List",font="ariel,15",width=10,bd=5,bg="#0b40a1",fg="white")
        self.l1.pack(side="top",fill=BOTH)
        
        self.l2=Label(self.root,text="Add Task",font="ariel,10",width=10,bd=2,bg="#0b40a1",fg="white")
        self.l2.place(x=40,y=50)
        
        self.l3=Label(self.root,text="Tasks",font="ariel,10",width=10,bd=2,bg="#0b40a1",fg="white")
        self.l3.place(x=40,y=180)
        self.t1=Listbox(self.root,height=5,bd=5,width=20,font="ariel,20")
        self.t1.place(x=20,y=220)
        self.text=Text(self.root,bd=5,height=2,width=20,font="ariel,10")
        self.text.place(x=20,y=90)
        
        def add():
            content=self.text.get(1.0,END)
            self.t1.insert(END,content)
            with open("data.txt","a") as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)
        def delete():
            delete_=self.t1.curselection()
            look=self.t1.get(delete_)
            with open("data.txt","r+") as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.t1.delete(delete_)
            
        with open("data.txt","r") as file:
            read=file.readlines()
            for i in read:
                ready=i.split()
                self.t1.insert(END,ready)
            file.close()
        self.button1=Button(self.root,text="Add",font="ariel,5",width=5,bd=1,bg="#0dda0f",fg="white",command=add)
        self.button1.place(x=260,y=95)
        self.button1=Button(self.root,text="Delete",font="ariel,5",width=8,bd=1,bg="#f8290a",fg="white",command=delete)
        self.button1.place(x=260,y=250)
        
def main():
    root=Tk()
    ui=todo(root)
    root.mainloop()
if __name__=="__main__":
    main()