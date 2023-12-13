from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox



class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")


        #title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="SMART STOCK",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)


        #logout 
        btn_logout=Button(self.root,text="Logout",font=("timesnewroman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #clock
        
        self.lbl_clock=Label(self.root,text="WELCOME TO SMART STOCK \t\t Date: DD-MM-YYYY Time:HH-MM-SS",font=("times new roman",15,),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #==========Prodcut frame
        self.var_search=StringVar()

        
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)
        
        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        #==Product search Frame===========
        ProductFrame2=Frame(ProductFrame1,bd=4,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)
        
        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        
        lbl_search=Label(ProductFrame2, text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)
        txt_search=Entry(ProductFrame2, textvariable=self.var_search,font=("times new roman",15,),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

        #==Product details Frame===========
        ProductFrme3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrme3.place(x=2,y=140,width=398,height=385)

        
        scrolly=Scrollbar(ProductFrme3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrme3,orient=HORIZONTAL)
        
        self.product_table=ttk.Treeview(ProductFrme3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)#this is sone to activate the scroll
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("pid",text="PID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="QTY")
        self.product_table.heading("status",text="Status")
        self.product_table["show"]="headings"
        
        
        #to reduce the text size in theb down box
        self.product_table.column("pid",width=90)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=100)
        
       
        self.product_table.pack(fill=BOTH,expand=1)
        #self.product_table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrme3,text="NOTE:'Enter 0 Quantity to remove product from the cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
        #CUSTOMER FRAME==============================================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        
        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame, text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame, textvariable=self.var_cname,font=("times new roman",13,),bg="lightyellow").place(x=80,y=35,width=180)
        
        lbl_contact=Label(CustomerFrame, text="Contact",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(CustomerFrame, textvariable=self.var_contact,font=("times new roman",13,),bg="lightyellow").place(x=380,y=35,width=140)
        
        #cal Cart frame==========
        Cal_Cart_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
        
        #calculator frame=========
        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state="readonly")
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text=7,font=("arial",15,"bold"),bd=5,width=4,pady=10).grid(row=1,column=0)

        #Cart frame==============
        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)
        cartTitle=Label(cart_Frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        
        
        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)
        
        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)#this is sone to activate the scroll
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        self.CartTable.heading("status",text="Status")
        self.CartTable["show"]="headings"
        
        
        #to reduce the text size in theb down box
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.column("status",width=90)
        
       
        self.CartTable.pack(fill=BOTH,expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)
        
        #ADD CARTWidgets BUTTONS================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        

        Add_cartWidgetsFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Add_cartWidgetsFrame.place(x=420,y=550,width=530,height=110)
        
        lbl_p_name=Label(Add_cartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_cartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_cartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_cartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_cartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_qty=Entry(Add_cartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock=Label(Add_cartWidgetsFrame,text="In Stock [9999]",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        btn_clear_cart=Button(Add_cartWidgetsFrame,text="clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_cartWidgetsFrame,text="Add | Update cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)

        # 
        
if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()
