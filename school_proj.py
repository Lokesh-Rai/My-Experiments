# -------------------------------------------------Developed by Lokesh Rai Class XII C Sunbeam School Bhagwanpur-----------------------------------------------------


# --------------------------------------------------------------- Instructor: Pradumna Singh ------------------------------------------------------------------------

'''           this program helps you to save different databases  of different classes of school and call them by providing suitable password'''

import pickle,os,time,winsound
# -----------------------------------------------------------creating class for saving records-----------------------------------------------------------------------
class SCHOOL:                                                       
    def __init__(self,c):
        self.c=c
        self.rno=0
        self.name=''
        self.s=''
        self.per=0
        self.gen=''
        self.hob=''
        self.mob=''
        self.add=''
        self.fname=''
        self.nat=''
        self.dob=''
        self.email=''
        self.mot=''
        self.regno=0
        self.str=''
        self.fees=0
        self.cat=''
        self.phy=''
        self.rel=''
        self.bg=''
    def indata(self):
        self.rno=input("Enter the class roll number:")
        self.regno=input("Enter the registration number:")
        self.name=raw_input("Enter the student name:")
        self.s=raw_input("Enter student's section:")
        self.fname=raw_input("Enter Student's father name:")
        self.mot=raw_input("Enter Student's mother name:")
        self.dob=raw_input("Enter Student's date of birth:")
        self.gen=raw_input("Enter student's gender:")
        self.per=input("Enter the Student's percentage(don't use '%' sign):")
        self.str=raw_input("Enter the Stream opted:")
        self.fees=input("Enter the fees paid by student:")
        self.hob=raw_input("Enter Student's hobby:")
        self.mob=raw_input("Enter Student's mobile number:")
        self.add=raw_input("Enter Student's address:")
        self.email=raw_input("Enter Student's email ID:")
        self.nat=raw_input("Enter the Student's Nationlity:")
        self.cat=raw_input("Enter the category of student(SC,ST,OBC or GEN):")
        self.phy=raw_input("Is the Student physically challenged or not:")
        self.rel=raw_input("Enter Student's religion:")
        self.bg=raw_input("Enter Student's blood group:")
    def outdata(self):
        print "Student's class roll number       :",self.rno
        print "Student's registration number     :",self.regno
        print "Student's name                    :",self.name
        print "Student's class and section       :",self.c,self.s
        print "Student's father name             :",self.fname
        print "Student's mother name             :",self.mot
        print "Student's gender                  :",self.gen
        print "Student's percentage              :",self.per,"%"
        print "Student's Stream                  :",self.str
        print "The fees paid by the student      :Rs.",self.fees
        print "Student's hobby                   :",self.hob
        print "Student's mobile number           :",self.mob
        print "Student's address                 :",self.add
        print "Student's date of birth           :",self.dob
        print "Student's email ID is             :",self.email
        print "Student's Nationality             :",self.nat
        print "Student's category                :",self.cat
        print "Physically Challenged             :",self.phy
        print "Student's Religion                :",self.rel
        print "Student's Blood Group             :",self.bg
        
        
# ------------------------------------------------------------------for creating records-----------------------------------------------------------------------------
def data(m,lm):
    def writedata():
        j2=input("Enter the number of data you want to save at a time:\n-->>")
        for i in range(j2):
            print "\n**************************Enter information of data number",i+1,"**************************:--\n"
            fout=open(m,"ab")
            ob=SCHOOL(lm)
            ob.indata()
            pickle.dump(ob,fout)
            print"**************************Record added successfully!**************************\n"
            print"\n------------------------------------------------------------------------------------------------------\n"
            check=raw_input("                              Press Enter to continue")
            print"\n"
            fout.close()
    def readdata():                                  #for showing all records
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            try:
                print"**************************Student's details are:**************************\n"
                while True:
                    ob=pickle.load(fin)
                    l="Loading....."
                    for i in l:
                        print i,
                        time.sleep(0.3)
                    print"\n"
                    ob.outdata()
                    print"\n------------------------------------------------------------------------------------------------------\n"
                    check=raw_input("                              Press Enter to continue")
                    print"\n"
                    
            except EOFError:
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def searchdatarange():                           #for searching data within given salary range
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            try:
                a=input('Enter minimum percentage:')
                b=input('Enter maximum percentage:')
                print"**************************Student's details in percentage range",a,'and',b,'are:**************************\n'
                while True:
                    ob=pickle.load(fin)
                    if ob.per>=a and ob.per<=b:
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        
            except EOFError:
                fin.close()
                print"\n"
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def searchcwithregno():
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            fl=False
            try:
                n=input("Enter student's registration number to search details:")
                print'**************************Student details with registration number',n,'is:**************************\n'
                while True:
                    ob=pickle.load(fin)
                    if ob.regno==n:
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        
                        fl=True
                        break
            except EOFError:
                if fl==False:
                    print'**************************Record does not exist!**************************\n'
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def searchcwithgender():
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            fl=False
            try:
                n=raw_input("Enter student's gender to search details:")
                print'**************************Student details with gender',n,'are:**************************\n'
                while True:
                    ob=pickle.load(fin)
                    if ob.gen==n:
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        
                        fl=True
                        break
            except EOFError:
                if fl==False:
                    print'**************************Record does not exist!**************************\n'
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def searchcwithstream():
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            fl=False
            try:
                n=raw_input("Enter student's stream to search details:")
                print'**************************Student details with stream',n,'are:**************************\n'
                while True:
                    ob=pickle.load(fin)
                    if ob.str==n:
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        
                        fl=True
                        break
            except EOFError:
                if fl==False:
                    print'**************************Record does not exist!**************************\n'
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def searchcwithphyc():
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            fl=False
            try:
                n=raw_input("Enter student's physical condition to search details:")
                print'**************************Student details with physical condition',n,'are:**************************\n'
                while True:
                    ob=pickle.load(fin)
                    if ob.phy==n:
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        
                        fl=True
                        break
            except EOFError:
                if fl==False:
                    print'**************************Record does not exist!**************************\n'
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def searchcwithcategory():
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            fl=False
            try:
                n=raw_input("Enter student's category to search details:")
                print'**************************Student details with category',n,'are:**************************\n'
                while True:
                    ob=pickle.load(fin)
                    if ob.cat==n:
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        
                        fl=True
                        break
            except EOFError:
                if fl==False:
                    print'**************************Record does not exist!**************************\n'
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def searchcwithbg():
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            fl=False
            try:
                n=raw_input("Enter student's blood group to search details:")
                print'**************************Student details with blood group',n,'are:**************************\n'
                while True:
                    ob=pickle.load(fin)
                    if ob.bg==n:
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        
                        fl=True
                        break
            except EOFError:
                if fl==False:
                    print'**************************Record does not exist!**************************\n'
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def searchcwithrel():
        try:
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            fl=False
            try:
                n=raw_input("Enter student's religion to search details:")
                print'**************************Student details with religion',n,'are:**************************\n'
                while True:
                    ob=pickle.load(fin)
                    if ob.rel==n:
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        
                        fl=True
                        break
            except EOFError:
                if fl==False:
                    print'**************************Record does not exist!**************************\n'
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def modify():                                                  #for modifying records
        try:
            fin=open(m,'rb')
            fout=open('temp.dat','wb')
            ob=SCHOOL(lm)
            ob1=SCHOOL(lm)
            flag=False
            try:
                n=input('Enter registration number to modify details:')
                while True:
                    ob=pickle.load(fin)
                    if ob.regno==n:
                        flag=True
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        print"**************************Enter fresh information:**************************"
                        ob1.indata()
                        pickle.dump(ob1,fout)
                        print"**************************Record modified!**************************"
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                    else:
                        pickle.dump(ob,fout)
            except EOFError:
                if not flag:
                    print '**************************Record does not exist!**************************\n'
                fout.close()
                fin.close()
            os.remove(m)
            os.rename('temp.dat',m)
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def delete():                                         #for deleting records
        try:
            fin=open(m,'rb')
            fout=open('temp.dat','wb')
            ob=SCHOOL(lm)
            flag=False
            try:
                n=input('Enter roll number to delete:')
                while True:
                    ob=pickle.load(fin)
                    if ob.rno==n:
                        flag=True
                        l="Loading.....\n"
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        print"**************************Record deleted!**************************\n"
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                    else:
                        pickle.dump(ob,fout)
            except EOFError:
                if not flag:
                    print '**************************Record does not exist!**************************'
                fout.close()
                fin.close()
            os.remove(m)
            os.rename('temp.dat',m)
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def secwise():
        try:
            a=raw_input("Enter the section of student:")
            fin=open(m,'rb')
            ob=SCHOOL(lm)
            try:
                print"**************************Student's details in section",a,'is:**************************'
                while True:
                    ob=pickle.load(fin)
                    if ob.s>=a:
                        print"\n"
                        l="Loading.....\n"
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        ob.outdata()
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                           Press Enter to continue")
                        print"\n"
            except EOFError:
                fin.close()
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
    def modify1by1():                                                  #for modifying only records
        try:
            fin=open(m,'rb')
            fout=open('temp.dat','wb')
            ob=SCHOOL(lm)
            flag=False
            try:
                n=input('Enter registration number to modify details:')
                while True:
                    ob=pickle.load(fin)
                    if ob.regno==n:
                        flag=True
                        l="Loading.....\n"
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        print"**************************What you want to change:--**************************\n"
                        print"  1.Roll Number"
                        print"  2.Registration Number"
                        print"  3.Name"
                        print"  4.Section"
                        print"  5.Father's Name"
                        print"  6.Mother's Name"
                        print"  7.Gender"
                        print"  8.Percent Obtained"
                        print"  9.Stream Opted"
                        print"  10.Fees Paid"
                        print"  11.Hobby"
                        print"  12.Mobile Number"
                        print"  13.Address"
                        print"  14.Date of Birth"
                        print"  15.Email ID"
                        print"  16.Nationality"
                        print"  17.Category"
                        print"  18.Physically Condition"
                        print"  19.Religion"
                        print"  20.Blood Group\n"
                        new=input("Enter your choice:--")
                        if new==1:
                            ob.rno=input("Enter new roll number:")
                        elif new==2:
                            ob.regno=input("Enter new registration number:")
                        elif new==3:
                            ob.name=raw_input("Enter new name:")
                        elif new==4:
                            ob.s=raw_input("Enter new section:")
                        elif new==5:
                            ob.fname=raw_input("Enter new Father's name:")
                        elif new==6:
                            ob.mot=raw_input("Enter new Mother's name:")
                        elif new==7:
                            ob.gen=raw_input("Enter new Gender:")
                        elif new==8:
                            ob.per=input("Enter new percentage:")
                        elif new==9:
                            ob.str=raw_input("Enter new stream:")
                        elif new==10:
                            ob.fees=input("Enter new fees:")
                        elif new==11:
                            ob.hob=raw_input("Enter new hobby:")
                        elif new==12:
                            ob.mob=input("Enter new mobile number:")
                        elif new==13:
                            ob.add=raw_input("Enter new address:")
                        elif new==14:
                            ob.dob=raw_input("Enter new Date of Birth:")
                        elif new==15:
                            ob.email=raw_input("Enter new Email ID:")
                        elif new==16:
                            ob.nat=raw_input("Enter new Nationality:")
                        elif new==17:
                            ob.cat=raw_input("Enter new category:")
                        elif new==18:
                            ob.phy=raw_input("Enter new physical state:")
                        elif new==19:
                            ob.rel=raw_input("Enter new religion:")
                        elif new==20:
                            ob.bg=raw_input("Enter new Blood Group:")
                        else:
                            print"**************************Wrong Input!!**************************\n"
                        print"**************************Record modified successfully!!**************************\n"
                        print"\n------------------------------------------------------------------------------------------------------\n"
                        check=raw_input("                              Press Enter to continue")
                        print"\n"
                        pickle.dump(ob,fout)
                    else:
                        pickle.dump(ob,fout)
            except EOFError:
                if not flag:
                    print '**************************Record does not exist!**************************\n'
                fout.close()
                fin.close()
            os.remove(m)
            os.rename('temp.dat',m)
        except IOError:
            print"**************************Sorry no file exist!!**************************\n"
        
    while True:
       
   # ----------------------------------------------------------main program of functions -------------------------------------------------------------------------
        
        h= "                        Student's data operation menu "
        k="                     ------------------------------------"
        for i in h:
            print i,
            time.sleep(0.02)
        print"\n"
        for i in k:
            print i,
            time.sleep(0.04)
        print"\n\n"
        print 'Enter your Choice -->\n\n**************************'
        print"  1.Store Data\n\n  2.See all data\n\n  3.Search data percentage wise\n\n  4.Search data section wise\n\n  5.Search indivisual record with registration number\n\n  6.Search record with gender\n\n  7.Search record with stream\n\n  8.Search record with physical condition\n\n  9.Search record with category\n\n  10.Search record with blood group\n\n  11.Search record with religion\n\n  12.Modify/change all data\n\n  13.Modify/change one data\n\n  14.Delete data\n**************************\n"
        print'Enter 15 to log out!'
        a=raw_input('--->>')
        if a=='1':
            writedata()
        elif a=='2':
            readdata()
        elif a=='3':
            searchdatarange()
        elif a=='4':
            secwise()
        elif a=='5':
            searchcwithregno()
        elif a=='6':
            searchcwithgender()
        elif a=='7':
            searchcwithstream()
        elif a=='8':
            searchcwithphyc()
        elif a=='9':
            searchcwithcategory()
        elif a=='10':
            searchcwithbg()
        elif a=='11':
            searchcwithrel()
        elif a=='12':
            modify()
        elif a=='13':
            modify1by1()
        elif a=='14':
            delete()
        elif a=='15':
            print"------------------------------------------------------------------------\n\n"
            break
        else:
            winsound.Beep(5000,1000)
            print"**************************You committed an error!!!**************************\n"
        
#  *********************************************************.......main program starts here......******************************************************************

def newcreate():                                                    #for creating new database
    m=raw_input('Enter the class:')
    if int(m)>=13:
        print"**************************ERROR!!!! there is no class after class 12!**************************\n"
    else:
        lm=m
        v=open('admin.dat','ab')
        v.write('')
        n2=open('admin.dat','rb')
        h4=n2.read()
        j10=h4.split()
        l1=m+'.dat'
        if l1 in j10:
            print"**************************Sorry sir we already contain a database of class",m,"**************************\n"
        else:
            m+='.dat'
            c1=raw_input('Enter your password(of one word only!):')
            for i in c1:
                if i==" ":
                    print"**************************Your Password contains space this is risky!!**************************"
                    print"             **************************Terminating......**************************\n"
                    break
            else:
                c2=raw_input('confirm your password:')
                if c1==c2:
                    c3=raw_input('Enter your favroite city:--')
                    g=open('forgot.dat','ab')
                    g.write(c3)
                    g.write(' ')
                    fl=open('pass.dat','ab')
                    fl.write(c1)
                    fl.write(' ')
                    fl.close()
                    fout=open('admin.dat','ab')
                    fout.write(m)
                    fout.write(' ')
                    print"\n"
                    l="Loading....."
                    for i in l:
                        print i,
                        time.sleep(0.3)
                    print"\n"
                    data(m,lm)
                    fout.close()
                        
                else:
                    print"**************************Your both passwords don't match!!**************************"
                    print"--------------------------------------------------------\n"
def securitycheck():                                      #for privacy of data
    try:
        a=raw_input("Enter the class:\n")
        var=a
        a+='.dat'
        print"ENTER YOUR CHOICE:--->>\n\n**************************\n  1.Enter password\n  2.Forgot password\n**************************\n"
        f5=input("--->>")
        if f5==1:
                b=raw_input('Enter your password:')
                print"\n"
                fl=open('pass.dat','rb')
                m=fl.read()
                n=m.split()
                fm=open('admin.dat','rb')
                t=fm.read()
                t1=t.split()
                c=0
                for i in range(len(t1)):
                    if t1[i]==a:
                        if n[i]==b:
                            l="Loading....."
                            for i in l:
                                print i,
                                time.sleep(0.2)
                            print"\n"
                            data(a,var)
                        else:
                            print"**************************This password does not match our records!**************************\n"
                            print"---------------------------------------------------------------------------------------------------------------------------------"
                            k="Restarting......"
                            for i in k:
                                print i,
                                time.sleep(0.04)
                            print"\n"
                        break
                else:
                    print"This file does not exist!!"
                    print"------------------------------------------------------------------------------------------------------------------------------------------"
        elif f5==2:
            def passs(c,var):
                j1=raw_input("Enter your new password:--")
                for i in j1:
                    if i==" ":
                        print"**************************Your Password contains space this is risky!!**************************"
                        print"              **************************Terminating......**************************\n"
                        break
                else:
                    j2=raw_input("Confirm your new password:--")
                    if j1==j2:
                        j3=open('pass.dat','rb')
                        s=j3.read()
                        s1=s.split()
                        s1[c]=j1
                        fl=open('pass.dat','wb')
                        fl.write('')
                        sn1=open('pass.dat','ab')
                        for i in s1:
                            sn1.write(i)
                            sn1.write(' ')
                        jj=open('admin.dat','rb')
                        jg=jj.read()
                        jh=jg.split()
                        j=jh[c]
                        print"**************************Your password has been successfully changed!!**************************\n"
                        l="Loading....."
                        for i in l:
                            print i,
                            time.sleep(0.3)
                        print"\n"
                        data(j,var)
                    else:
                        print"**************************Your both the passwords don't match!!**************************\n"
                    
            h=raw_input('Enter your favroite city:--')
            m1=open('forgot.dat','rb')
            l2=m1.read()
            d=l2.split()
            fm=open('admin.dat','rb')
            t=fm.read()
            t1=t.split()
            c=0
            for i in range(len(t1)):
                if t1[i]==a:
                    c=i
                    if d[c]==h:
                        print"Your account has been successfully found!"
                        print"Please create new password for security reasons:--"
                        passs(c,var)
                        break
                    else:
                        print"**************************You are not the authorised person**************************"
                        print"\n"
                        break
            else:
                print"**************************This file does not exist!!**************************"
                print"\n"
    except IOError:
        print"**************************No database exist!!!**************************\n----------------------------------------------------------------------------------------------------------------------\n"
def deldata():
    try:
        a=raw_input("Enter your class:\n")
        a=a.upper()
        g1=a
        a+='.dat'
        f5=1
        if f5==1:
                b=raw_input('Enter your password:')
                fl=open('pass.dat','rb')
                m=fl.read()
                n=m.split()
                fm=open('admin.dat','rb')
                t=fm.read()
                t1=t.split()
                c=0
                for i in range(len(t1)):
                    if t1[i]==a:
                        if n[i]==b:
                            
                            q=t1.pop(i)
                            i=n.pop(i)
                            
                            try:
                                os.remove(a)
                                print"**************************You have successfully deleted the data of the class",g1,'**************************\n'
                            except WindowsError:
                                print"No data of class",g1,"exists!\n"
                            
                        else:
                            print"This password does not match our records!\n"
                            print"---------------------------------------------------------------------------------------------------------------------------------"
                            k="Restarting......"
                            for i in k:
                                print i,
                                time.sleep(0.04)
                            print"\n"
                        break
                else:
                    print"**************************This file does not exist!!**************************"
                    print"------------------------------------------------------------------------------------------------------------------------------------------"
    except IOError:
        print"\nNo database created!\n----------------------------------------------------------------------------------------------------------------------------------\n"
#real program
while True:
    
    d='Welcome to the Database of the School'
    for i in d:
        print i,
        time.sleep(0.04)
    print"\n\n_____________________________________________________________________________________________________"
    print"                             ___                  ___    ____   ____               "
    print"     * *                    /     |   |  |\   |  |   \  |      |    |  |\  /|                   * *"
    print"    * + *                   \__   |   |  | \  |  |___/  |___   |____|  | \/ |                  * + *"
    print"    *   *                      \  |   |  |  \ |  |   \  |      |    |  |    |                  *   *"
    print"     !!!                    ___/  |___|  |   \|  |___/  |____  |    |  |    |                   !!!"
    print"     !!!                                                                                        !!!"
    print"_____________________________________________________________________________________________________"


    
    print'\n\n****************************************************LOGIN MENU****************************************************\n'
    print"\n"
    t2='  1.Login to your database\n\n  2.Create new database\n\n  3.Delete data of a particular class\n\n  4.Exit the program\n\n'
    for i in t2:
        print i,
        time.sleep(0.0)
    print"\n"
    x=raw_input('-->>')
    if x=='1':
        securitycheck()
    elif x=='2':
        newcreate()
    elif x=='3':
        deldata()
    elif  x=='4':
        print"\n"
        m='This program is developed by Lokesh Rai'
        for i in m:
            print i,
            time.sleep(0.02)
        print"\n*********************************************************************************************************************************************"
        exit()
    else:
        print'wrong choice!\n'
        winsound.Beep(5000,1000)
