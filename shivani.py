from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import random,os
from tkinter import messagebox
import tempfile
from time import strftime




class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # =============Variables==============
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        # Product Categories list
        self.Category=["Select Option","Grocery","Snacks","Personalcare"]

        # SubCatGrocery
        self.SubCatGrocery=["Fruits","Dairy","vegetables"]
        self.Fruits=["Apple","orange","coconut"]
        self.price_Apple=30
        self.price_orange=20
        self.price_coconut=50

        self.Dairy=["Milk","breads","eggs"]
        self.price_Milk=30
        self.price_breads=40
        self.price_eggs=10

        self.vegetables=["potato","tomato","onion"]
        self.price_potato=25
        self.price_tomato=15
        self.price_onion=20

        self.SubCatSnacks=["Chips","chocolates","Biscuits"]
        self.Chips=["Lays","kurkure","nachos"]
        self.price_Lays=25
        self.price_kurkure=30
        self.price_nachos=35

        self.chocolates=["perk","Munch","kitkat"]
        self.price_perk=30
        self.price_Munch=40
        self.price_kitkat=50

        self.Biscuits=["cookies","Manaco","Marigold"]
        self.price_cookies=80
        self.price_Manaco=50
        self.price_Marigold=60


        self.SubCatPersonalcare=["Facewash","Shampoo","Soap"]
        self.Facewash=["Himalaya","Everyuth","Nivea"]
        self.price_Himalaya=250
        self.price_Everyuth=350
        self.price_Nivea=400

        self.Shampoo=["Loreal","Biotique","Mamaearth"]
        self.price_Loreal=450
        self.price_Biotique=300
        self.price_Mamaearth=500

        self.Soap=["Dove","Pears","Lux"]
        self.price_Dove=100
        self.price_Pears=80
        self.price_Lux=60

        # Image1
        img=Image.open(r"C:\Users\shiva\OneDrive\Desktop\Mini Project\image\shopping-cart-supermarket-empty-shelves-40320116.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        # Image2
        img_1=Image.open(r"C:\Users\shiva\OneDrive\Desktop\Mini Project\image\raw-fruit-vegetable-raw-fruit-vegetable-isolated-104266586.jpg")
        img_1=img_1.resize((500,130),Image.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)


        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)

        # Image3
        img_2=Image.open(r"C:\Users\shiva\OneDrive\Desktop\Mini Project\image\1000_F_113767529_ij6S3k2rMWlBA4fIj4xbNAKa2BYV8W7h.jpg")
        img_2=img_2.resize((520,130),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)


        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=500,height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white")
        lbl_title.place(x=0,y=130,width=1530,height=45)

    

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

         # Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


         # Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

         # Category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # Subcategory
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubcategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubcategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
        
        
        # Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        # Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=24)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        # Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=0,y=150,width=980,height=340)

        # Image1
        img12=Image.open(r"C:\Users\shiva\OneDrive\Desktop\Mini Project\image\shopping-cart-supermarket-empty-shelves-40320116.jpg")
        img12=img12.resize((490,340),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        
        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height=340)

        # Image2
        img_13=Image.open(r"C:\Users\shiva\OneDrive\Desktop\Mini Project\image\raw-fruit-vegetable-raw-fruit-vegetable-isolated-104266586.jpg")
        img_13=img_13.resize((490,340),Image.LANCZOS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)


        lbl_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=490,y=0,width=500,height=340)


        # Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)


        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)




        # RightFrame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        
         # Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

         # Subtotal
        self.lblSubTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_Bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_Bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
        #==========================Function Declaration======================

    def welcome(self):
      self.textarea.delete(1.0,END)
      self.textarea.insert(END,"\t\t Welcome To MiniMall")
      self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
      self.textarea.insert(END,f"\n Customer name:{self.c_name.get()}")
      self.textarea.insert(END,f"\n Phone number:{self.c_phon.get()}")
      self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

      self.textarea.insert(END,"\n==================================================")
      self.textarea.insert(END,"\n Products\t\t\tQty\tPrice")
      self.textarea.insert(END,"\n==================================================")
    def AddItem(self):
          Tax=1
          self.n=self.prices.get()
          self.m=self.qty.get()*self.n
          self.l.append(self.m)
          if self.product.get()=="":
                messagebox.showerror("Error","Please Select the product Name")
          else:
                self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
                self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
                self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
                self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
          if self.product.get()=="":
                messagebox.showerror("Error","Please Add To Cart Product")
          else:
                text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                self.welcome()
                self.textarea.insert(END,text)
                self.textarea.insert(END,"\n================================================")
                self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
                self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
                self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
                self.textarea.insert(END,"\n================================================")

    def save_bill(self):
          op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
          if op>0:
                self.bill_data=self.textarea.get(1.0,END)
                f1=open(r"C:\Users\shiva\OneDrive\Desktop\Mini Project\Bill"+str(self.bill_no.get())+"txt",'w')
                f1.write(self.bill_data)
                op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
                f1.close()

    def iprint(self):
          q=self.textarea.get(1.0,"end-1c")
          filename=tempfile.mktemp('.txt')
          open(filename,'w').write(q)
          os.startfile(filename,"print")

    def find_bill(self):
          found="no"
          for i in os.listdir(r"C:\Users\shiva\OneDrive\Desktop\Mini Project\Bill"):
                if i.split('.')[0]==self.search_bill.get():
                      f1=open(r"C:\Users\shiva\OneDrive\Desktop\Mini Project\Bill",{i},'r')
                      self.textarea.delete(1.0,END)
                      for d in f1:
                            self.textarea.insert(END,d)
                      f1.close()
                      found="yes"
          if found=='no':
                      messagebox.showerror("Error","Invaid Bill No.")

    def clear(self):
          self.textarea.delete(1.0,END)
          self.c_name.set("")
          self.c_phon.set("")
          self.c_email.set("")
          x=random.randint(1000,9999)
          self.bill_no.set(str(x))
          self.search_bill.set("")
          self.product.set("")
          self.prices.set(0)
          self.qty.set(0)
          self.l=[0]
          self.total.set("")
          self.sub_total.set("")
          self.tax_input.set('')
          self.welcome()
                


                      
                


                      


    







    def Categories(self,event=""):
          if self.Combo_Category.get()=="Grocery":
                self.ComboSubcategory.config(value=self.SubCatGrocery)
                self.ComboSubcategory.current(0)
 
          if self.Combo_Category.get()=="Snacks":
                self.ComboSubcategory.config(value=self.SubCatSnacks)
                self.ComboSubcategory.current(0)

          if self.Combo_Category.get()=="Personalcare":
                self.ComboSubcategory.config(value=self.SubCatPersonalcare)
                self.ComboSubcategory.current(0)

    def Product_add(self,event=""):
          if self.ComboSubcategory.get()=="Fruits":
                self.ComboProduct.config(value=self.Fruits)
                self.ComboProduct.current(0)

          if self.ComboSubcategory.get()=="Dairy":
                self.ComboProduct.config(value=self.Dairy)
                self.ComboProduct.current(0)

          if self.ComboSubcategory.get()=="vegetables":
                self.ComboProduct.config(value=self.vegetables)
                self.ComboProduct.current(0)

          # Snacks
          if self.ComboSubcategory.get()=="Chips":
               self.ComboProduct.config(value=self.Chips)
               self.ComboProduct.current(0)

          if self.ComboSubcategory.get()=="chocolates":
               self.ComboProduct.config(value=self.chocolates)
               self.ComboProduct.current(0)

          if self.ComboSubcategory.get()=="Biscuits":
               self.ComboProduct.config(value=self.Biscuits)
               self.ComboProduct.current(0)

          # Personalcare
          if self.ComboSubcategory.get()=="Facewash":
                    self.ComboProduct.config(value=self.Facewash)
                    self.ComboProduct.current(0)

          if self.ComboSubcategory.get()=="Shampoo":
                    self.ComboProduct.config(value=self.Shampoo)
                    self.ComboProduct.current(0)

          if self.ComboSubcategory.get()=="Soap":
                    self.ComboProduct.config(value=self.Soap)
                    self.ComboProduct.current(0)

    def price(self,event=""):
          # Grocery
          # Fruits
          if self.ComboProduct.get()=="Apple":
                self.ComboPrice.config(value=self.price_Apple)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="orange":
                self.ComboPrice.config(value=self.price_orange)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="coconut":
                self.ComboPrice.config(value=self.price_coconut)
                self.ComboPrice.current(0)
                self.qty.set(1)

          # Dairy
                
          if self.ComboProduct.get()=="Milk":
                self.ComboPrice.config(value=self.price_Milk)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="breads":
                self.ComboPrice.config(value=self.price_breads)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="eggs":
                self.ComboPrice.config(value=self.price_eggs)
                self.ComboPrice.current(0)
                self.qty.set(1)

           # vegetables
          if self.ComboProduct.get()=="potato":
                self.ComboPrice.config(value=self.price_potato)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="tomato":
                self.ComboPrice.config(value=self.price_tomato)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="onion":
                self.ComboPrice.config(value=self.price_onion)
                self.ComboPrice.current(0)
                self.qty.set(1)

           # snacks
           # Chips
                
          if self.ComboProduct.get()=="Lays":
                self.ComboPrice.config(value=self.price_Lays)
                self.ComboPrice.current(0)
                self.qty.set(1)
                
          if self.ComboProduct.get()=="kurkure":
                self.ComboPrice.config(value=self.price_kurkure)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="nachos":
                self.ComboPrice.config(value=self.price_nachos)
                self.ComboPrice.current(0)
                self.qty.set(1)

           # chocolates
                
          if self.ComboProduct.get()=="perk":
                self.ComboPrice.config(value=self.price_perk)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Munch":
                self.ComboPrice.config(value=self.price_Munch)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="kitkat":
                self.ComboPrice.config(value=self.price_kitkat)
                self.ComboPrice.current(0)
                self.qty.set(1)

           # Biscuits
                
          if self.ComboProduct.get()=="cookies":
                self.ComboPrice.config(value=self.price_cookies)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Manaco":
                self.ComboPrice.config(value=self.price_Manaco)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Marigold":
                self.ComboPrice.config(value=self.price_Marigold)
                self.ComboPrice.current(0)
                self.qty.set(1)

           # personal care
           # Facewash
                
          if self.ComboProduct.get()=="Himalaya":
                self.ComboPrice.config(value=self.price_Himalaya)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Everyuth":
                self.ComboPrice.config(value=self.price_Everyuth)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Nivea":
                self.ComboPrice.config(value=self.price_Nivea)
                self.ComboPrice.current(0)
                self.qty.set(1)
 
            # Shampoo
                
          if self.ComboProduct.get()=="Loreal":
                self.ComboPrice.config(value=self.price_Loreal)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Biotique":
                self.ComboPrice.config(value=self.price_Biotique)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Mamaearth":
                self.ComboPrice.config(value=self.price_Mamaearth)
                self.ComboPrice.current(0)
                self.qty.set(1)

            # Soap
                
          if self.ComboProduct.get()=="Dove":
                self.ComboPrice.config(value=self.price_Dove)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Pears":
                self.ComboPrice.config(value=self.price_Pears)
                self.ComboPrice.current(0)
                self.qty.set(1)

          if self.ComboProduct.get()=="Lux":
                self.ComboPrice.config(value=self.price_Lux)
                self.ComboPrice.current(0)
                self.qty.set(1)
        
                
      


      







                
                













        
        
        
        
        
































if __name__== '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
        