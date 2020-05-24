#PROJECT TIC-TAC-TOE
#LOKESH RAI
import turtle
def realmain():
    A1=[]
    A2=[]
    people=0
    work=0
    turtle.color("white")
    turtle.forward(100)
    turtle.color("brown")
    turtle.right(90)
    turtle.forward(300)
    turtle.backward(600)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(600)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(600)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(600)
    turtle.forward(300)
    turtle.right(90)
    turtle.color("white")
    turtle.forward(100)
    while True:
        if work==0:
            l=input("Player 1 Enter your desired location:--")
            for i in A1+A2:
                if i==l:
                    print"That place is filled Try again..."
                    people=1
                    break
            else:
                people=0
                A1.append(l)
                if l==1:
                    a=-200
                    b=200
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A1) and (2 in A1) and (3 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(200,200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        elif (1 in A1) and (5 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        
                        elif (1 in A1) and (4 in A1) and (7 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        
                        else:
                            pass
                elif l==2:
                    a=0
                    b=200
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A1) and (2 in A1) and (3 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(200,200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        
                        elif (2 in A1) and (5 in A1) and (8 in A1):
                            turtle.color("white")
                            turtle.setposition(0,200)
                            turtle.color("purple")
                            turtle.setposition(0,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        else:
                            pass
                        
                elif l==3:
                    a=200
                    b=200
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A1) and (2 in A1) and (3 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(200,200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        elif (3 in A1) and (5 in A1) and (7 in A1):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("purple")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        elif (3 in A1) and (6 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        else:
                            pass
                elif l==4:
                    a=-200
                    b=0
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (4 in A1) and (5 in A1) and (6 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,0)
                            turtle.color("purple")
                            turtle.setposition(200,0)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        elif (1 in A1) and (4 in A1) and (7 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        else:
                            pass
                elif l==5:
                    a=0
                    b=0
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A1) and (5 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        elif (3 in A1) and (5 in A1) and (7 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,0)
                            turtle.color("purple")
                            turtle.setposition(200,0)
                            print "Hurray Player '1' wins!!!!"
                            break
                        elif (4 in A1) and (5 in A1) and (6 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,0)
                            turtle.color("purple")
                            turtle.setposition(200,0)
                            print "Hurray Player '1' wins!!!!"
                            break
                        elif (2 in A1) and (5 in A1) and (8 in A1):
                            turtle.color("white")
                            turtle.setposition(0,200)
                            turtle.color("purple")
                            turtle.setposition(0,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        else:
                            pass
                elif l==6:
                    a=200
                    b=0
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (4 in A1) and (5 in A1) and (6 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,0)
                            turtle.color("purple")
                            turtle.setposition(200,0)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        elif (3 in A1) and (6 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        else:
                            pass
                elif l==7:
                    a=-200
                    b=-200
                    
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (3 in A1) and (5 in A1) and (7 in A1):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("purple")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        elif (7 in A1) and (8 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,-200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        elif (1 in A1) and (4 in A1) and (7 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                            
                        
                        else:
                            pass
                elif l==8:
                    a=0
                    b=-200
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (7 in A1) and (8 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,-200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        elif (2 in A1) and (5 in A1) and (8 in A1):
                            turtle.color("white")
                            turtle.setposition(0,200)
                            turtle.color("purple")
                            turtle.setposition(0,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        else:
                            pass
                else:
                    a=200
                    b=-200
                    cross(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A1) and (5 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        
                        elif (7 in A1) and (8 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(-200,-200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        
                        elif (3 in A1) and (6 in A1) and (9 in A1):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("purple")
                            turtle.setposition(200,-200)
                            print "Hurray Player '1' wins!!!!"
                            break
                        else:
                            pass
                
        if people==0:
            l1=input("Player 2 Enter your desired location:--")
            for i in A1+A2:
                if i==l1:
                    print"That place is filled Try again..."
                    work=1
                    break
            else:
                work=0
                A2.append(l1)
                if l1==1:
                    a=-200
                    b=200
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A2) and (2 in A2) and (3 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(200,200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        elif (1 in A2) and (5 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        
                        elif (1 in A2) and (4 in A2) and (7 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        
                        else:
                            pass
                elif l1==2:
                    a=0
                    b=200
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A2) and (2 in A2) and (3 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(200,200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        
                        elif (2 in A2) and (5 in A2) and (8 in A2):
                            turtle.color("white")
                            turtle.setposition(0,200)
                            turtle.color("green")
                            turtle.setposition(0,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        else:
                            pass
                elif l1==3:
                    a=200
                    b=200
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A2) and (2 in A2) and (3 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(200,200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        elif (3 in A2) and (5 in A2) and (7 in A2):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("green")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        elif (3 in A2) and (6 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        else:
                            pass
                elif l1==4:
                    a=-200
                    b=0
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (4 in A2) and (5 in A2) and (6 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,0)
                            turtle.color("green")
                            turtle.setposition(200,0)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        elif (1 in A2) and (4 in A2) and (7 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        else:
                            pass
                elif l1==5:
                    a=0
                    b=0
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A2) and (5 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        elif (3 in A2) and (5 in A2) and (7 in A2):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("green")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        elif (4 in A2) and (5 in A2) and (6 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,0)
                            turtle.color("green")
                            turtle.setposition(200,0)
                            print "Hurray Player '2' wins!!!!"
                            break
                        elif (2 in A2) and (5 in A2) and (8 in A2):
                            turtle.color("white")
                            turtle.setposition(0,200)
                            turtle.color("green")
                            turtle.setposition(0,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        else:
                            pass
                elif l1==6:
                    a=200
                    b=0
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (4 in A2) and (5 in A2) and (6 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,0)
                            turtle.color("green")
                            turtle.setposition(200,0)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        elif (3 in A2) and (6 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        else:
                            pass
                elif l1==7:
                    a=-200
                    b=-200
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (3 in A2) and (5 in A2) and (7 in A2):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("green")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        elif (7 in A2) and (8 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,-200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        elif (1 in A2) and (4 in A2) and (7 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(-200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                            
                        
                        else:
                            pass
                elif l1==8:
                    a=0
                    b=-200
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (7 in A2) and (8 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,-200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        elif (2 in A2) and (5 in A2) and (8 in A2):
                            turtle.color("white")
                            turtle.setposition(0,200)
                            turtle.color("green")
                            turtle.setposition(0,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        else:
                            pass
                else:
                    a=200
                    b=-200
                    O(a,b)
                    if len(A1)+len(A2)==9:
                        s4="\n THE MATCH IS DRAW BETTER LUCK NEXT TIME..."
                        for i in s4:
                            print i,
                            time.sleep(0.1)
                        break
                    else:
                        if (1 in A2) and (5 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        
                        elif (7 in A2) and (8 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(-200,-200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        
                        elif (3 in A2) and (6 in A2) and (9 in A2):
                            turtle.color("white")
                            turtle.setposition(200,200)
                            turtle.color("green")
                            turtle.setposition(200,-200)
                            print "Hurray Player '2' wins!!!!"
                            break
                        else:
                            pass


def cross(a,b):
    
    turtle.color("white")
    turtle.setposition(a,b)
    turtle.color("purple")
    turtle.left(45)
    turtle.forward(75)
    turtle.backward(150)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(75)
    turtle.backward(150)
    turtle.forward(75)
    turtle.left(45)
    turtle.color("white")
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

def O(a,b):
    
    turtle.color("white")
    turtle.setposition(a,b)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.color("green")
    turtle.circle(60)
    
#main program

import time
m="WELCOME TO THE GAME OF TIC TAC TOE"
for i in m:
    print i,
    time.sleep(0.1)
n="\n----------------------------------\n\n"
for i in n:
    print i,
    time.sleep(0.1)

x=raw_input("Enter first persons Name:--")
y=raw_input("Enter second persons name:--")
print "\nSo ",x," is first Player and he will be awarded cross and the first chance..."
print"\nEnter 1 for rules or 2 for directly starting the game:--"
pk=raw_input()
if pk=='1' or pk=='2':
    
    if pk=='1':
        xl='\nLoading...\n'
        for i in xl:
            print i,
            time.sleep(0.1)
        print"The rules of the game are as follows:---"
        print"\n1.The basic pattern of the game is---\n"
        print"     |     |    "
        print"  1  |  2  |  3  "
        print"     |     |    "
        print"-----------------"
        print"     |     |  "
        print"  4  |  5  |  6"
        print"     |     |  "
        print"-----------------"
        print"     |     |"
        print"  7  |  8  |  9"
        print"     |     |"
        print"\n So basicly you have to enter the number where you want to put your 'cross' or 'O' in your turn."
        print"\n2.Do Complain For Any Disperency(if it occours) btw It is just a trial version\n"
        xt=raw_input("Press enter key to start---->")
        
        st="\nStarting....\n"
        for i in st:
            print i,
            time.sleep(0.1)
        realmain()
    else:
        st="\nStarting....\n"
        for i in st:
            print i,
            time.sleep(0.1)
        realmain()
else:
    c="\nAborting..."
    for i in c:
        print i,
        time.sleep(0.1)
