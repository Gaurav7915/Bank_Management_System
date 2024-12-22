from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import date
from random import randint
root = Tk()
root.minsize(height= 500, width = 600)
img = ImageTk.PhotoImage(Image.open("image4.jpeg"))
import sqlite3
connection = sqlite3.connect("bank.db")
csr = connection.cursor()
l1 = Label (root , image = img)
l1.place(x = 0, y = 0)
root.title("SWISS BANK")

def next():
        l1.place_forget()
        l2.place_forget()
        lf1.pack(expand = "yes", fill = "both")
        l3.place(x = 40, y = 0)
        e1.place(x = 280, y = 0)
        b1.place(x = 200, y = 100)
        e4.place(x  = 280 , y = 50)
        l6.place(x = 40 , y = 50)

        
def login():
        c = e1.get()
        e = "("+c+",)"
        d  = e4.get()
        dd = "("+d+",)"
        ab = csr.execute("select acc from user")
        ab1 = ab.fetchall()
        for i in ab1:
                j = str(i)
                if j==e:
                        command = "select passwd from user where acc ="+c
                        abb = csr.execute(command)
                        aab = abb.fetchall()
                        xyz = str(aab[0])
                        if dd==xyz:
                                msg = messagebox.showinfo("welcome", "User")
                                lf1.pack_forget()
                                l3.place_forget()
                                e1.place_forget()
                                b1.place_forget()
                                lf2.pack(expand = "yes" , fill = "both")
                                b2.place(x = 50 , y = 0)
                                b30.place(x = 50, y = 200)
                                b4.place(x = 265, y = 400)
                                b5.place(x = 350 , y = 0)
                                b6.place(x = 350 , y = 200)
                                break
                else:
                        continue
        else:
                msg=messagebox.showinfo("ERROR","PLEASE CHECK PARTICULARS AGAIN")


def view_balance():
        c = e1.get()
        command = "select bal from user where acc="+c
        b = csr.execute(command)
        a = b.fetchall()
        aa = a[0]
        aaa = str(aa[0])
        d = "Balance is = "+ aaa
        msg = messagebox.showinfo("", d)


def loan():
      file = open("loan.txt",'r')
      content = file.read()
      r1 = Tk()
      text = Text(r1)
      text.insert(INSERT,content)
      text.config(state = DISABLED)
      text.pack()
      r1.mainloop()


def transaction():
        lf2.pack_forget()
        b2.place_forget()
        b30.place_forget()
        b4.place_forget()
        b5.place_forget()
        b6.place_forget()
        lf3.pack(expand = "yes", fill = "both")	
        b7.place(x = 0 , y = 0)
        b8.place(x = 400 , y = 0)
        b9.place(x = 200, y = 200)
        b14.place(x = 280, y = 430)

        
def withdraw():
	lf3.pack_forget()
	b7.place_forget()
	b8.place_forget()
	b9.place_forget()
	b14.place_forget()
	root.config(bg = "lightblue1")
	l4.place(x = 20, y = 20)
	e2.place(x = 300, y = 20)
	b10.place(x = 200 , y = 80)
	b12.place(x = 200, y = 180)


def confirm_withdraw():
      dat = str(date.today())
      a = e1.get()
      ab = int(a)
      withdrawal_amt = e2.get()
      command = "select bal from user where acc="+a
      c= csr.execute(command)
      original_bal = c.fetchall()
      aa = original_bal[0]
      bb = aa[0]
      new_bal = bb - int(withdrawal_amt)
      if new_bal>=0:
            csr.execute("update user set bal = ? where acc = ?",(new_bal,a))
            csr.execute("insert into details (acc, date, withdraw , bal) values (?,?,?,?)",(ab ,dat, withdrawal_amt, new_bal))
            connection.commit()
            msg = messagebox.showinfo("congo","transaction success")
      else:
            msg = messagebox.showinfo("Error","Insufficient Balance")
	
	
def deposit():
	lf3.pack_forget()
	b7.place_forget()
	b8.place_forget()
	b9.place_forget()
	b14.place_forget()
	root.config(bg = "lightblue1")
	l5.place(x = 20, y = 20)
	e3.place(x = 300, y = 20)
	b11.place(x = 200, y = 80)
	b13.place(x = 200, y = 180)
	
	
def confirm_deposit():
	dat = str(date.today())
	a = e1.get()
	ab = int(a)
	deposit_amt = e3.get()
	command = "select bal from user where acc="+a
	c= csr.execute(command)
	original_bal = c.fetchall()
	aa = original_bal[0]
	bb = aa[0]
	new_bal = bb+int(deposit_amt)
	csr.execute("update user set bal = ? where acc = ?",(new_bal,a))
	csr.execute("insert into details (acc, date, deposit, bal) values (?,?,?,?)",(ab ,dat, deposit_amt, new_bal))
	connection.commit()
	msg = messagebox.showinfo("congo","transaction success")
	

def history():
        a = e1.get()
        b = "select date,withdraw,deposit,bal from details where acc="+a
        c = csr.execute(b)
        e = c.fetchall()
        r2 = Tk()
        l1 =Label(r2 , text = "Date",width = 10, borderwidth = 1, relief = SUNKEN).grid(row = 0 , column = 0)
        l1 =Label(r2 , text = "Withdraw",width = 10, borderwidth = 1, relief = SUNKEN).grid(row = 1 , column = 0)
        l1 =Label(r2 , text = "Deposit",width = 10, borderwidth = 1, relief = SUNKEN).grid(row = 2 , column = 0)
        l1 =Label(r2 , text = "Balance",width = 10, borderwidth = 1, relief = SUNKEN).grid(row = 3 ,column = 0)
        y = 1
        for i in e:
                x = 0
                y+=1
                for j in i:
                        l = Label(r2 , text = j , width = 10, borderwidth = 5, relief = SUNKEN)
                        l.grid(row = x , column = y)
                        x+=1

                                
def back3():
        lf3.pack_forget()
        b7.place_forget()
        b8.place_forget()
        b9.place_forget()
        b14.place_forget()
        lf2.pack(expand = "yes" , fill = "both")
        b2.place(x = 50 , y = 0)
        b30.place(x = 50, y = 200)
        b4.place(x = 265, y = 400)
        b5.place(x = 350 , y = 0)
        b6.place(x = 350 , y = 200)

		
def back():
        lf2.pack_forget()
        b2.place_forget()
        b30.place_forget()
        b4.place_forget()
        b5.place_forget()
        b6.place_forget()
        e1.delete(0 ,END)
        e4.delete(0, END)
        lf1.pack(expand = "yes" , fill = "both")
        l3.place(x = 40, y = 0)
        e1.place(x = 280, y = 0)
        b1.place(x = 200, y = 100)
        
def with_back():
	l4.place_forget()
	e2.place_forget()
	b10.place_forget()
	b12.place_forget()
	e2.delete(0 , END)
	lf3.pack(expand = "yes", fill = "both")
	b7.place(x = 0 , y = 0)
	b8.place(x = 400 , y = 0)
	b9.place(x = 200, y = 200)
	b14.place(x = 280, y = 430)
    
def dep_back():
    l5.place_forget()
    e3.place_forget()
    b11.place_forget()
    b13.place_forget()
    e3.delete(0 , END)
    lf3.pack(expand = "yes", fill = "both")
    b7.place(x = 0 , y = 0)
    b8.place(x = 400 , y = 0)
    b9.place(x = 200, y = 200)
    b14.place(x = 280, y = 430)
        
def view_details():
        c = e1.get()
        command = "select * from user where acc="+c
        a = csr.execute(command)
        b = a.fetchall()
        r = Tk()
        r.minsize(height = 200 , width = 200)
        t = list(b[0])
        t5 = "Name:"+t[0]
        t1 = "Age :"+str(t[1])             
        t2 = "Date of birth :"+t[2]
        t3 = "Address:"+t[3]
        t4 = "Account Number :"+str(t[4])
        la = LabelFrame(r, text = "Details", bg = "lawn green")
        la.pack(expand = "yes" , fill = "both")
        l1 = Label(la, text = t5, relief = RAISED,width = 25, fg = "blue"). grid (row = 0, column = 0)
        l2 = Label(la, text = t1, width = 25,relief = RAISED, fg = "red"). grid (row = 1, column = 0)
        l3 = Label(la, text = t2, width = 25, relief = RAISED, fg = "deep pink"). grid (row = 2 , column = 0)
        l4 = Label(la, text = t3,width = 25,  relief = RAISED ,fg = "black"). grid (row = 3 , column = 0)
        l5 = Label(la, text = t4,width = 25,  relief = RAISED, fg = "navy"). grid (row = 4,  column = 0)

l2 = Button(root , text = "Login",command = next, fg = "red")
l2.place(x = 270, y = 475)
lf1 = LabelFrame(root, text = "Enter login details", bg = "red"  ,bd = 10, fg = "white")
l3 = Label (lf1 , text = "Enter your account number :", bg = "red", fg = "white")
e1 = Entry(lf1, width = 20)

b1 = Button(lf1 , text = "LOGIN", command = login , bg = "SeaGreen1")

lf2 = LabelFrame(root , text = "User_account", bg = "thistle" , bd = 15 , fg = "black")
b2_image = ImageTk.PhotoImage(Image.open("user.png"))
b2 = Button(lf2 , text = "VIEW ALL DETAILS", image = b2_image , compound = "t" , command = view_details, bg = "coral", fg = "black")
b30_image = ImageTk.PhotoImage(Image.open("loanop.png"))
b30 = Button(lf2 ,image = b30_image,text = "Loan" , command = loan ,compound = "t")
b4 = Button(lf2, text = "BACK" , command = back , bg = "black" , fg = "cyan1")
b5_image = ImageTk.PhotoImage(Image.open("balance.jfif"))
b5 = Button(lf2 ,text = "BALANCE" ,image = b5_image ,compound = "t" , command = view_balance , bg = "khaki" , fg = "black" )
b6_image = ImageTk.PhotoImage(Image.open("touter.png"))
b6 = Button(lf2, text = "TRANSACTIONS", command = transaction , bg = "gold", fg = "black", image = b6_image , compound = "t")
lf3 = LabelFrame(root, bg = "cyan", bd = 20)
b7_image=ImageTk.PhotoImage(Image.open("withdrawal.png"))
b7 = Button(lf3, text = "Withdrawal" , command = withdraw, bg = "black" , fg = "white" , image = b7_image , compound = "t")
b8_image=ImageTk.PhotoImage(Image.open("deposit.jpg"))
b8 = Button(lf3, text = "Deposit" , command = deposit, bg = "white" , fg = "black", image = b8_image , compound = "t")
b9_image=ImageTk.PhotoImage(Image.open("Transaction.jpg"))
b9 =  Button(lf3, text = "History" , command = history, bg = "light green" , fg = "red", image = b9_image , compound = "t")
e2 = Entry(root, width = 35)
l4 = Label(root , text = "Enter the amount u wanna withdraw" , width = 30, relief = RAISED , borderwidth = 2)
b10 = Button(root , text = "CONFIRM", command = confirm_withdraw ,relief = RAISED ,width = 12 , height = 3 ,borderwidth = 5)
l5 = Label(root , text = "Enter the amount u wanna deposit" , width = 30, relief = RAISED , borderwidth = 2 )
e3 = Entry(root , width = 35)
b11 = Button(root , text = "CONFIRM" ,command = confirm_deposit,relief = RAISED , borderwidth = 5 , width = 12 , height = 3)
b12 = Button(root , text = "BACK" , command = with_back , relief = RAISED , borderwidth = 5 , width = 12 , height = 2)
b13 = Button(root , text = "BACK", command = dep_back ,relief = RAISED , borderwidth = 5 , width = 12 , height = 2)
b14 = Button(root, text = "BACK", command = back3 ,relief = RAISED , borderwidth = 5)
e4 = Entry(lf1 ,width = 20 , show = "*")
l6 = Label(lf1 , text = "Password  :" , bg = "red" , fg = "white")

root.mainloop()

