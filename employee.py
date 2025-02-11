from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Yogi Fashion | Developed by Vivek")
        self.root.config(bg="white")
        self.root.focus_force()

        #=== SearchFrame ===

        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #=== Options ===
        cmb_search=ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame)


if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root,mainloop()