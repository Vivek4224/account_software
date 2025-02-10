from tkinter import*
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Yogi Fashion | Developed by Vivek")

        #=== Title ===
        self.icon_title=PhotoImage(file="images/logo.png")
        title=Label(self.root,text="ogi Fashion",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w").place(x=0,y=0,relwidth=1,height=70)


root=Tk()
obj=IMS(root)
root,mainloop()