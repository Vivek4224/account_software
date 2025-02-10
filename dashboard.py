from tkinter import*
from PIL import Image,ImageTk
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Yogi Fashion | Developed by Vivek")
        self.root.config(bg="white")

        #=== Title ===
        self.icon_title=PhotoImage(file="images/logo.png")
        title=Label(self.root,text="ogi Fashion",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w").place(x=0,y=0,relwidth=1,height=70)

        #=== btn_logout ===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        #=== Clock ===
        self.lbl_clock=Label(self.root,text="Welcome to Yogi Fashion\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #=== Left Menu ===
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)

        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",image=self.icon_side,compound=LEFT,padx=20,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

root=Tk()
obj=IMS(root)
root,mainloop()