from tkinter import *
import tkinter as tk
import mysql.connector
import tkinter.ttk as ttk
from tkinter import messagebox as tkMessageBox

#=====================================================================================================================================================

loggedUser = ""
receiverUser =""

#=========DATABASE SET UP==============================================================================================================================

def databaseSetup():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS chatroom;")
    mycursor.execute("use chatroom;")
    mycursor.execute ("CREATE TABLE IF NOT EXISTS user ( user_id varchar(20) PRIMARY KEY ,user_password varchar(30), age int, contact int)")
    mycursor.execute ("CREATE TABLE IF NOT EXISTS usersdata ( user_id varchar(20),receiver varchar(30),message varchar(100),time TIMESTAMP )")
    mycursor.execute ("CREATE TABLE IF NOT EXISTS friend ( user_id1 varchar(20),user_id2 varchar(20))")
    mycursor.close()
    mydb.close()

#======================(PART-I)==========================================================================================================================
# List of Fuctions in Main Window - checkLogin, checkUser, loginWindow, signupWindow , login , signup
class MainWindow():
#========================MAIN WINDOW=====================================================================================================================
    def __init__(self, window):
        self.window = window
        self.window.title("YO CHAT")
        width = 500
        height = 400
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.window.resizable(0, 0)
        self.window.config(bg="#6666ff")
#=====================FRAMES==============================================================================================================================
        
        MidLeft = Frame(root, width=400)
        MidLeft.pack(pady=100)
        
#=================================BUTTONS OF LOGIN AND SIGNUP =============================================================================
        btn_add = Button(MidLeft, text="Login", bg="#66ff66",pady=20,width=50, command=self.loginWindow)
        btn_add.pack()
        btn_signup = Button(MidLeft, text="SignUp", bg="red", pady=20,width=50,command=self.signupWindow)
        btn_signup.pack()
#=====================================================================================================================================================
        
    def checkLogin(self,username,password):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
        mycursor = mydb.cursor()
        userr = self.checkUser(username)
        if userr !=0:
            sql = ("SELECT user_password from user where user_id = %s")
            var = (username,)
            mycursor.execute(sql,var)
            result = mycursor.fetchone()
            flag = (result[0])
            mycursor.close()
            mydb.close()
            if (flag==password):
                return 1 # Login Success
        return 0 # Login Failed
    
#=====================================================================================================================================================
    
    def checkUser(self,username):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
        mycursor = mydb.cursor()
        sql = ("SELECT count(user_id) from user where user_id = %s")
        var = (username,)
        mycursor.execute(sql,var)
        result = mycursor.fetchone()
        flag = (result[0])
        mycursor.close()
        mydb.close()
        return flag
    
#=====================================================================================================================================================
    
    def loginWindow(self):
        global NewWindow
        user_id.set("")
        user_password.set("")
        NewWindow = Toplevel()
        NewWindow.title("User Login")
        width = 400
        height = 200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindow.resizable(0, 0)
        NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        
#===================FRAMES================================================================================================================
        #this frame is for the  lopgin page
        FormTitle = Frame(NewWindow)
        FormTitle.pack()
        LoginForm = Frame(NewWindow)
        LoginForm.pack()
        
#=============lables======================================================================================================================
        
        lbl_title = Label(FormTitle, text="enter login details", font=('arial', 16), bg="#66ff66",  width = 30)
        lbl_title.pack()
        lbl_userinfo = Label( LoginForm, text="user_id", font=('arial', 14), bd=5)
        lbl_userinfo.grid()
        lbl_pass = Label( LoginForm, text="password", font=('arial', 14), bd=5)
        lbl_pass.grid()
        
#===================ENTRY=================================================================================================================
        
        username = Entry( LoginForm, textvariable=user_id, font=('arial', 14))#USER ID KA JO  BOX AATA HAI USKA SIZE
        username.grid(row=0, column=1)
        userpassword = Entry( LoginForm, textvariable=user_password, font=('arial', 14))
        userpassword.grid(row=1, column=1)
        
#==================BUTTONS================================================================================================================
        
        btn_addcon = Button(LoginForm, text="next", width=50, command=self.login)#next button ka configuration
        btn_addcon.grid(row=2, columnspan=2, pady=10)
        
#=====================================================================================================================================================
    def signupWindow(self):
        global NewWindows
        user_id.set("")
        user_password.set("")
        age.set("")
        contact.set("")
        NewWindows = Toplevel()
        NewWindows.title("signup")
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindows.resizable(0, 0)
        NewWindows.geometry("%dx%d+%d+%d" % (width, height, x, y))
#======================FRAMES(THIS IS FOR THE SIGNUP PAGE )===============================================================================

        FormTitle1 = Frame(NewWindows)
        FormTitle1.pack()
        signupForm = Frame(NewWindows)
        signupForm.pack()

#=============lables(FOR THE SIGNUP WINDOW) ===============================================================================================

        lbl_title1 = Label(FormTitle1, text="create new account", font=('arial', 16), bg="#66ff66",  width = 30)
        lbl_title1.pack()
        lbl_userinfo1 = Label( signupForm, text="user_id", font=('arial', 14), bd=5)
        lbl_userinfo1.grid()
        lbl_pass = Label( signupForm, text=" password", font=('arial', 14), bd=5)
        lbl_pass.grid()
        lbl_age = Label( signupForm, text=" age", font=('arial', 14), bd=5)
        lbl_age.grid()
        lbl_contact = Label( signupForm, text=" contact", font=('arial', 14), bd=5)
        lbl_contact.grid()

#======================ENTRY (FOR THE BOX WHERE WE PUT THE VALUES OF SIGNUP)==============================================================

        username = Entry( signupForm, textvariable=user_id, font=('arial', 14))
        username.grid(row=0, column=1)
        userpassword = Entry( signupForm, textvariable=user_password, font=('arial', 14))
        userpassword.grid(row=1, column=1)
        userage = Entry( signupForm, textvariable=age, font=('arial', 14))
        userage.grid(row=2, column=1)
        usercontact = Entry( signupForm, textvariable=contact, font=('arial', 14))
        usercontact.grid(row=3, column=1)

#==================BUTTON(NEXT BUTTON IN SIGNUP)==========================================================================================

        btn_addcon = Button( signupForm, text="next", width=50, command=self.signup)#next button ka configuration
        btn_addcon.grid(row=4, columnspan=2, pady=10)
        
#=====================================================================================================================================================
    def login(self):
        if user_id.get() =="" or user_password.get() =="":
            result = tkMessageBox.showwarning('', 'Please Complete The Required Fields', icon="warning")
        else:
            user = user_id.get()
            passw = user_password.get()
            user=user.strip()
            passw=passw.strip()
            if self.checkLogin(user,passw)==1:
                # Login success ka code
                result = tkMessageBox.showwarning('', 'Login Successful', icon="warning",command = NewWindow.destroy())
                global loggedUser
                loggedUser = user
                chatzone()
            else:
                result = tkMessageBox.showwarning('', 'Invalid user id or password', icon="warning")
#=====================================================================================================================================================
    def signup(self):
        #This is to check if any of the user inputs were empty
        if user_id.get() =="" or user_password.get() =="" or age.get() =="" or contact.get() == "":
            result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            if self.checkUser(user_id.get())==0:
                #This is to check if the user already in database or insert the new user
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
                mycursor = mydb.cursor()
                uid = user_id.get()
                pwd = user_password.get()
                ag = age.get()
                ctc = contact.get()
                if ag.isdigit() and ctc.isdigit() :
                    mycursor.execute("INSERT INTO user ( user_id,user_password,age,contact) VALUES(%s,%s,%s,%s)",(str(uid),str(pwd) ,str(ag),str(ctc)))
                    mycursor.close()
                    mydb.commit()
                    mydb.close()
                    global loggedUser
                    loggedUser = uid
                    result = tkMessageBox.showwarning('', 'user created', icon="warning",command=NewWindows.destroy())
                    chatzone()
                else:
                    result = tkMessageBox.showwarning('', 'age or contact is incorrect', icon="warning")

            else:
                result = tkMessageBox.showwarning('', 'User already exists', icon="warning")
                
#=====================================================================================================================================================
#The Main Window Ends here
#=====================================================================================================================================================
# List of Functions in ChatWindow - sendMessage, DeleteData , viewRecords ,BACK GOING, 
class ChatWindow():
    def __init__(self):
        global NewWindows1
        send.set("")
        imessage.set("")
        NewWindows1 = Toplevel()
        global receiverUser
        tstr = "Enjoy Chatting with " + receiverUser
        NewWindows1.title(tstr)
        width = 700
        height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2)  - (width/2)
        y = (screen_height/2) - (height/2)
        NewWindows1.resizable(0, 0)
        NewWindows1.geometry("%dx%d+%d+%d" % (width, height, x, y))
#=========================================================================================================================================
        FormTitle4 = Frame(NewWindows1,width=700)
        FormTitle4.pack()
        chatarea= Frame(NewWindows1,width=700,pady=1)
        chatarea.pack()
        sendmsg=Frame(NewWindows1,width=700,pady=10)
        sendmsg.pack()
#=========================================================================================================================================
        lbl_title2 = Label(FormTitle4, text="yochat", font=('arial', 16), bg="#66ff66",  width =130,pady=10)
        lbl_title2.pack()
#=========================================================================================================================================
        message11 = Entry( sendmsg,textvariable=imessage, font=('arial', 14),width=50)
        message11.pack(side=LEFT)
#=========================================================================================================================================
        btn_add = Button(FormTitle4, text="< back", bg="#66ff66", command=self.backgoing)
        btn_add.pack(side=LEFT)
        btn_refreash1= Button(FormTitle4, text="refreash", bg="green",command=self.viewRecords)
        btn_refreash1.pack(side=RIGHT,pady=1)
        btn_delete = Button(FormTitle4, text="delete", bg="red",command=self.DeleteData)
        btn_delete.pack(side=RIGHT,pady=1)
        btn_send= Button(sendmsg, text="send", bg="red",command=self.sendMessage)
        btn_send.pack(side=RIGHT,pady=1)
#=========================================================================================================================================
       
        scrollbary = Scrollbar(chatarea, orient=VERTICAL)
        self.tree = ttk.Treeview(chatarea, height=20,yscrollcommand=scrollbary.set)
        self.tree["columns"]=("message","time")
        self.tree.column("message",minwidth=400, width = 400,stretch=tk.NO)
        self.tree.heading("message",text="Message",anchor=tk.W)
        self.tree.column("time", minwidth=400,width=400,stretch=tk.NO)
        self.tree.heading("time", text="Time",anchor=tk.W)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.pack()
        self.tree.bind('<Double-Button-1>')
        self.tree.tag_configure('s', background='#FF0000')
        self.tree.tag_configure('r', background='#00FF00')
        self.viewRecords()
        
#=====================================================================================================================================================
        
    def sendMessage(self):
        global loggedUser
        global receiverUser
        sqlQuery1 = """insert into usersdata  values (%s,%s,%s,NOW())"""
        message = imessage.get()
        inputVar1 = (loggedUser,receiverUser,message)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
        mycursor = mydb.cursor()
        mycursor.execute(sqlQuery1,inputVar1)
        mycursor.close()
        mydb.commit()
        mydb.close()
        imessage.set("")
        self.viewRecords()
        
#=====================================================================================================================================================
        
    def DeleteData(self):
        if self.tree.selection():
            curItem = self.tree.focus()
            contents =(self.tree.item(curItem))
            selecteditem = contents['values']
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
            mycursor = mydb.cursor()
            query = """DELETE FROM usersdata where ((user_id=%s and receiver=%s) or (user_id=%s and receiver=%s)) and message=%s and time=%s"""
            global loggedUser
            global receiverUser
            vals = (loggedUser,receiverUser,receiverUser,loggedUser, selecteditem[0],selecteditem[1])
            mycursor.execute(query,vals)
            mydb.commit()
            mycursor.close()
            mydb.close()
            self.viewRecords()
            
#=====================================================================================================================================================
            
    def viewRecords(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        global loggedUser
        global receiverUser
        query = "select * from usersdata where ((user_id=%s and receiver=%s) or (user_id=%s and receiver=%s)) ORDER by time DESC"
        variables = (loggedUser,receiverUser,receiverUser,loggedUser)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
        mycursor = mydb.cursor()
        mycursor.execute(query,variables)
        result = mycursor.fetchall()
        for row in result:
            if row[1] == loggedUser:
                row = row[2:]
                self.tree.insert('',0,text='',values=row, tags = ('s',))
            else:
                row = row[2:]
                self.tree.insert('',0,text='',values=row, tags = ('r',))
#=====================================================================================================================================================
                
    def backgoing(self):
        chatzone()
        NewWindows1.destroy()

#The chat window ends here
#=====================================================================================================================================================
# The chatzone contains - CHECK USER,viewfriends , addfriends, settingwindow , ChangePassword , deleteAccount , friendwindow , onSelected
class chatzone:
#=====================================================================================================================================================
    def __init__(self):
        global NewWindows2
        send.set("")
        NewWindows2 = Toplevel()
        NewWindows2.title("enjoy chating")
        width = 700
        height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2)  - (width/2)
        y = (screen_height/2) - (height/2)
        NewWindows2.resizable(0, 0)
        NewWindows2.geometry("%dx%d+%d+%d" % (width, height, x, y))
#=========================================================================================================================================
        FormTitle5 = Frame(NewWindows2,width=700)
        FormTitle5.pack()
        chat1= Frame(NewWindows2,width=700,pady=1)
        chat1.pack()
        addfriend=Frame(NewWindows2,width=700,pady=10)
        addfriend.pack()
#=========================================================================================================================================
        lbl_title2 = Label(FormTitle5, text="yochat", font=('arial', 16), bg="#66ff66",  width =130,pady=10)
        lbl_title2.pack()
#=========================================================================================================================================
        btn_settings = Button(FormTitle5, text=":: settings", bg="red",width=15,command=self.settingwindow)
        btn_settings.pack(side=RIGHT,pady=1)
        btn_refreash = Button(FormTitle5, text="refreash", bg="green",width=15,command=self.viewfriends)
        btn_refreash.pack(side=RIGHT,pady=1)
        btn_addfrnd= Button(addfriend, text="+ add friend", bg="red",command=self.friendwindow)
        btn_addfrnd.pack(side=RIGHT,pady=1)
#=========================================================================================================================================
        scrollbary = Scrollbar(chat1, orient=VERTICAL)
        self.tree = ttk.Treeview(chat1, column=("friendlist"), height=20, selectmode="extended", yscrollcommand=scrollbary.set)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        self.tree.heading('friendlist', text="friend list", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=600)
        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.OnSelected)
        self.viewfriends()
#=====================================================================================================================================================
    def checkUser(self,username):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
        mycursor = mydb.cursor()
        sql = ("SELECT count(user_id) from user where user_id = %s")
        var = (username,)
        mycursor.execute(sql,var)
        result = mycursor.fetchone()
        flag = (result[0])
        mycursor.close()
        mydb.close()
        return flag
#=====================================================================================================================================================
    def viewfriends(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = "select * from friend where user_id1=%s or user_id2=%s"
        global loggedUser
        variables=(loggedUser,loggedUser)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
        mycursor = mydb.cursor()
        mycursor.execute(query,variables)
        result = mycursor.fetchall()
        for data in result:
            if data[1]==loggedUser:
                tdata = data[0]
            else:
                tdata= data[1]
            self.tree.insert('',0,text=data[0],values=tdata)
#=====================================================================================================================================================
    def addfriends(self):
        global NewWindows2
        NewWindows2.destroy()
        dost=user_id.get()
        if self.checkUser(dost)!=0:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
            mycursor = mydb.cursor()
            sqlQuery1 = """insert into friend values (%s,%s)"""
            sqlQuery2 ="""select count(user_id1) from friend where user_id1=%s and user_id2=%s"""
            sqlQuery3 ="""select count(user_id1) from friend where user_id2=%s and user_id1=%s"""
            global loggedUser
            inputVar1 = (loggedUser,dost)
            mycursor.execute(sqlQuery2,inputVar1)
            result1 =mycursor.fetchone()
            mycursor.execute(sqlQuery3,inputVar1)
            result2 =mycursor.fetchone()
            
            if result1[0]+result2[0] ==0:
                mycursor.execute(sqlQuery1 , inputVar1 )
                tkMessageBox.showwarning('', 'Friend Successfully Added', icon="warning")
                NewWindows3.destroy()
                mycursor.close()
                mydb.commit()
                mydb.close()
            else:
                tstr = 'Already Friends with '+ dost
                tkMessageBox.showwarning('', tstr, icon="warning")
        else:
            tkMessageBox.showwarning('', "User doesn't exist", icon="warning")
            NewWindows3.destroy()
        chatzone()
#=====================================================================================================================================================
    def settingwindow(self):
        global NewWindows4
        NewWindows4 = Toplevel()
        NewWindows4.title("settings")
        width = 400
        height = 350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindows4.resizable(0, 0)
        NewWindows4.geometry("%dx%d+%d+%d" % (width, height, x, y))

#=====================================================================================================================================================
        FormTitle7 = Frame(NewWindows4)
        FormTitle7.pack()
        settingForm = Frame(NewWindows4)
        settingForm.pack()


#=============lables(FOR THE SIGNUP WINDOW)===============================================================================================

        lbl_title40 = Label(FormTitle7, text="settings", font=('arial', 16), bg="#66ff66",  width = 30)
        lbl_title40.grid(row=0)
        lbl_title50 = Label(settingForm ,text="new_password" , font=('arial', 14),bd=5)
        lbl_title50.grid(row=1,sticky=W)
#============================================================================================================
        newpass = Entry( settingForm , textvariable=user_password, font=('arial', 14))
        newpass.grid(row=1,sticky=E)

#==================BUTTON(NEXT BUTTON IN SIGNUP)==========================================================================================

        btn_addcon = Button( settingForm , text= "delete account", width=50, command=self.deleteAccount)
        btn_addcon.grid(row=3)
        btn_addcon = Button( settingForm , text= "save",width =50 ,command=self.ChangePassword )
        btn_addcon.grid(row=2)
#=====================================================================================================================================================
    def ChangePassword(self):
        newPassword = user_password.get()
        sqlQuery = "update user set user_password=%s WHERE user_id=%s"
        global loggedUser
        inputVar = (newPassword,loggedUser)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
        mycursor = mydb.cursor()
        mycursor.execute(sqlQuery,inputVar)
        mycursor.close()
        mydb.commit()
        mydb.close()
        NewWindows4.destroy()
#=====================================================================================================================================================
    def deleteAccount(self):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="chatroom")
        mycursor = mydb.cursor()
        sqlQuery1 = """DELETE FROM `user` WHERE `user_id` = %s"""
        sqlQuery2 = """DELETE FROM usersdata WHERE user_id = %s or receiver = %s"""
        sqlQuery3 = """DELETE FROM friend where user_id1 = %s or user_id2=%s"""
        global loggedUser
        vars = (loggedUser, loggedUser)
        inputVar = (loggedUser,)
        mycursor.execute(sqlQuery1,inputVar)
        mycursor.execute(sqlQuery2,vars)
        mycursor.execute(sqlQuery3,vars)
        mycursor.close()
        mydb.commit()
        mydb.close()
        NewWindows2.destroy()
        NewWindows4.destroy()
#=====================================================================================================================================================
    def friendwindow(self):
        global NewWindows3
        user_id.set("")
        NewWindows3 = Toplevel()
        NewWindows3.title("add friend")
        width = 400
        height = 150
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindows3.resizable(0, 0)
        NewWindows3.geometry("%dx%d+%d+%d" % (width, height, x, y))
#=====================================================================================================================================================
        FormTitle6 = Frame(NewWindows3)
        FormTitle6.pack()
        addForm = Frame(NewWindows3)
        addForm.pack()
#=============lables(FOR THE SIGNUP WINDOW)===============================================================================================
        lbl_title1 = Label(FormTitle6, text="add friends", font=('arial', 16), bg="#66ff66",  width = 30)
        lbl_title1.pack()
        lbl_userinfo1 = Label( addForm, text="user_id", font=('arial', 14), bd=5)
        lbl_userinfo1.grid()
#======================ENTRY (FOR THE BOX WHERE WE PUT THE VALUES OF SIGNUP)==============================================================
        username = Entry( addForm, textvariable= user_id, font=('arial', 14))
        username.grid(row=0, column=1)
#==================BUTTON(NEXT BUTTON IN SIGNUP)==========================================================================================
        btn_addcon = Button( addForm, text="next", width=50, command=self.addfriends)#next button ka configuration
        btn_addcon.grid(row=4, columnspan=2, pady=10)
#=====================================================================================================================================================
    def OnSelected(self,event):
        curItem = self.tree.focus()
        contents =(self.tree.item(curItem))
        selecteditem = contents['values']
        global receiverUser
        receiverUser = selecteditem[0]
        ChatWindow()
        NewWindows2.destroy()


#=====================================================================================================================================================
if __name__ == '__main__':
    databaseSetup()
    root = Tk()
    user_id = StringVar()
    user_password = StringVar()
    age = StringVar()
    contact =StringVar()
    send =StringVar()
    chathistory=StringVar()
    receiver=StringVar()
    time=StringVar()
    imessage=StringVar()
    member=StringVar()
    application = MainWindow(root)
    root.mainloop()
