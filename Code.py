from turtle import
import turtle
import time
from math import*
import os#
import datetime#
from geoip import geolite2
import socket

os.system("color 30")
class TTUairways:
    ty=str
    tu=str
    name=str
    km=float
    kmm=float
    wanted=['Sami Saad','Pablo Escobar','Shorouq Aleidi','Toqa Alzyood']
    
    def title():
        print("\t\t\t\t\t\tTTU airways")
    def DrawWanted():
        
        hostname=socket.gethostname()
        #126.53.24.5 
        ip=socket.gethostbyname(hostname)
        locator=geolite2.lookup(ip)

        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.bgcolor("gray40")
        t.color("black")
        t.shape("circle")
        t.speed(20)
        t.fillcolor('white')
        t.begin_fill()
        t.right(180)
        t.forward(430)
        t.right(90)
        t.forward(300)
        t.left(270)
        t.forward(850)
        t.right(90)
        t.forward(300)
        t.right(90)
        t.forward(431)
        t.end_fill()
        speed(50)
        left(180)
        forward(430)
        left(270)
        forward(70)
        Style=('arial',8)
        color('black')
        write(f"                                                                                                                              {TTUairways.name} is wanted ")
        forward(20)
        Style=('arial',10)
        write("                                   The information you entered indicates that you are wanted. Please review one of the security branches",font=Style)
        forward(30)
        Style=('arial',60)
        color('red')
        write("            WANTED",font=Style)
        forward(20)
        Style=('arial',10)
        write(f"         your ip :{ip}",font=Style)
        forward(70)
        Style=('arial',10)
        color('red')
        write(f"         you location :{locator}",font=Style)
        end_fill()
        done()
    def draw():
    
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.bgcolor("cyan")
        t.color("black")
        t.shape("circle")
        t.speed(20)
        t.fillcolor('white')
        t.begin_fill()
        t.right(180)
        t.forward(430)
        t.right(90)
        t.forward(300)
        t.left(270)
        t.forward(850)
        t.right(90)
        t.forward(300)
        t.right(90)
        t.forward(431)
        t.end_fill()


        speed(50)
        left(180)
        forward(430)
        left(270)
        forward(260)
        left(270)
        Style=('arial',7)
        color('red')
        write("        Class | Classe",font=Style)
        color('black')
        left(180)
        left(90)
        forward(20)
        left(90)
        Style=('arial',10)
        write("      FIRST CLASS / PREMIERE CLASSE",font=Style)
        left(180)
        left(90)
        forward(20)
        left(90)
        Style=('arial',7)
        color('red')
        write("        fligth & Date | Vol et date                                              Gate | Porte                           Seat | PLACE",font=Style)
        color('black')
        left(180)
        left(90)
        forward(20)
        left(90)
        Style=('arial',10)
        dt = datetime.datetime.now()
        dd=(int(dt.strftime('%d')))+2
        dm=dt.strftime('%b')
        dy=(int(dt.strftime('%Y')))
        write(f"      {dy}-{dm}-{dd}",font=Style)
        write(f"                                                                       A12                               26B",font=Style)
        left(180)
        left(90)
        forward(5)
        left(90)
        Style=('arial',10)
        color('red')
        write("                         |                                          |                                     |",font=Style)
        left(180)
        left(90)
        forward(2)
        left(90)
        Style=('arial',5)
        color('red')
        write("          --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=Style)
        color('black')
        left(180)
        left(90)
        forward(35)
        left(90)
        Style=('arial',8)
        write("                 Boarding time\n                 Heur d'embarquement",font=Style)
        Style=('arial',14)
        dh=int(dt.strftime('%I'))
        da=dt.strftime('%p')
        write(f"                                       {dh}:00 {da}",font=Style)
        left(180)
        left(90)
        forward(5)
        left(90)
        Style=('arial',30)
        color('red')
        write("               > ",font=Style)
        left(180)
        left(90)
        forward(20)
        left(90)
        Style=('arial',7)
        write("        From | De                                                                             To | Destination",font=Style)
        color('black')
        left(180)
        left(90)
        forward(20)
        left(90)
        Style=('arial',10)
        write(f"       {TTUairways.ty}",font=Style)
        write(f"                                                                                 {TTUairways.tu}",font=Style)
        left(180)
        left(90)
        forward(6)
        left(90)
        Style=('arial',10)
        color('red')
        write("                                                      |                         |",font=Style)
        left(180)
        left(90)
        forward(2)
        left(90)
        Style=('arial',5)
        write("          --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=Style)
        left(180)
        left(90)
        forward(20)
        left(90)
        Style=('arial',7)
        write("        Name | Nom                                                                   Airline use | Asyage Interne",font=Style)
        color('black')
        left(180)
        left(90)
        forward(20)
        left(90)
        Style=('arial',10)
        write(f"                                                                ",font=Style)
        left(180)
        left(90)
        forward(6)
        left(90)
        Style=('arial',10)
        color('black')
        write(f"      {TTUairways.name}",font=Style)
        write(f"                                                        0081A                AAC27670",font=Style)
        left(180)
        left(90)
        forward(6)
        left(90)
        Style=('arial',10)
        color('red')
        write("                                                      |                         |",font=Style)
        left(180)
        left(90)
        forward(2)
        left(90)
        Style=('arial',5)
        write("          --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",font=Style)
        color("black")
        left(180)
        left(90)
        forward(51)
        left(90)
        forward(600)
        right(270)
        forward(240)
       
        for i in range(5):
            left(270)
            Style=('arial',7)
            write("    ||||||||  ||||||| |||| |||||||||||||||",font=Style)
            left(90)
            forward(6)
        forward(30)   
        left(180)
        forward(160)
        left(90)
        color('red')
        Style=('arial',7)
        write("     Ticket price",font=Style)#سعر التذكره
        color('black')
        left(180)
        left(90)
        forward(15)
        Style=('arial',10)
        write(f"    {TTUairways.kmm}$",font=Style)  
        color('red')
        forward(20)
        Style=('arial',7)
        write("     The distance traveled in kilometers",font=Style)
        color('black')
        forward(15)
        Style=('arial',10)
        write(f"    {TTUairways.km} KM    ",font=Style)
        forward(45)
        color('coral2')
        Style=('arial',15)
        write("\n\n   ******TTU airways******",font=Style)
        color('black')
        left(180)
        forward(255)
        end_fill()
        ####################من هون ببلش ارسم الخريطه##############
        right(90)
        forward(166)
        right(90)
        forward(70)
        right(270)
        color('red', 'yellow')
        speed(30)
        begin_fill()
        left(32)
        forward(251.5*.3)
        right(104)
        forward(99*.3)
        right(89)
        forward(7.5*.3)
        left(90)
        forward(19.5*.3)
        left(80)
        forward(21*.3)
        right(88)
        forward(10.5*.3)
        right(65)
        forward(40.5*.3)
        right(24)
        forward(202.5*.3)
        left(115)
        forward(150*.3)
        right(100)
        forward(37.5*.3)
        left(50)
        forward(40*.3)
        right(50)
        forward(76.5*.3)
        left(48)
        forward(48*.3)
        right(20)
        forward(45*.3)
        right(60)
        forward(129.5*.3)
        right(90)
        forward(10.5*.3)
        left(90)
        forward(4.5*.3)
        right(90)
        forward(80*.3)
        right(30)
        forward(7.5*.3)
        left(50)
        forward(7.5*.3)
        right(27)
        forward(15*.3)
        left(50)
        forward(6*.3)
        right(50)
        forward(120*.3)
        left(60)
        forward(15*.3)
        right(45)
        forward(90*.3)
        right(10)
        forward(55*.3)
        right(10)
        forward(7.5*.3)
        left(40)
        forward(6*.3)
        right(50)
        forward(10*.3)
        right(60)
        forward(40*.3)
        right(50)
        forward(30*.3)
        right(20)
        forward(25*.3)
        left(70)
        forward(15*.3)
        right(50)
        forward(55*.3)
        left(50)
        left(29)
        forward(257*.3)
        end_fill()
        done()
    def first():
        TTUairways.title()
        f=0
        while f<1:
            x=int(input("Welcome\nwrite number 1 to inquire about who we are\nif you know who we are or have seen us now and want to register, type 2\nto exit, press 0 :"))
            if x==1:
                os.system('cls')
                TTUairways.title()
                f=f+1
                print("Welcome\nWe worked for a private airline\n(helicopters)\nAnd during the program that we made, you can miss and book your tickets with ease and comfort\nOnce a reservation is made, we will show you the shape of your ticket\nBeing present on it:\nA-Your name\nB- Flight time and flight date\nC- The cost of the trip\nD- The actual distance traveled between the two airports in kilometers\n(You can check Google Maps for the distance and it will be 100% correct)")
                c=0
                while c<1:
                    y=int(input("\n\nPress 1 to go back or 0 to exit : "))
                    if y==1:
                       os.system('cls')
                       c=c+1
                       TTUairways.first()
                    elif y==0:
                       os.system('cls')
                       TTUairways.title()
                       print("\t\t\t    Thank you for using website, click anything to exit")
                       c=c+1
                    else:
                        print("Please select one of the options",end="\t")
            elif x==2:
                f=f+1
                os.system('cls')
                TTUairways.title()
                print("I will now show you the airports where your flight can be booked\n\n")
                print("A-Airports located in the north :\n\t1-Military Hospital Airport(Irbid)\n\t2-JUST-Heliport(Irbid)\n\t3-Helipad (Mafraq)")
                print("B-Airports located in the middle :\n\t4-Royal Jordanian AirCargo(Amman)\n\t5-Heliport(Amman)\n\t6-GEAA Heliport(Amman)\n\t7-Golden Eagle Aviation Academy(Amman)\n\t8-Anti extortion(Amman)\n\t9-Hospital Helipad(Amman)\n\t10-Jordan Hospital Airstrip(Amman)\n\t11-Amman Civil Airport(Amman)\n\t")
                print("C-Airports located in the south : \n\t12-Helipad (Karak)\n\t13-Tafila University Airport(Tafila)\n\t14-King Hussein International Airport(Aqaba)")
                TTUairways.coordinates()
            elif x==0:
                f=f+1
                os.system('cls')
                TTUairways.title()
                print("\t\t\t    Thank you for using website, click anything to exit")
            else:
                os.system('cls')
                TTUairways.title()
                print("please try again")
    def coordinates():
       
        o1=[32.50492765775706, 35.86503354312493]
        o2=[32.494321210944264, 35.989580977206096]
        o3=[32.265584624180114, 36.45530283125569]
        o4=[31.722390303372165, 35.98702064265451]
        o5=[31.981268891371514, 35.83224684264872]
        o6=[31.976968295952815, 35.840114331002695]
        o7=[31.967809516728646, 35.85495534449683]
        o8=[31.946405543565632, 35.86719944634497]
        o9=[31.979692195573094, 35.90143811750882]
        o10=[31.947977444815447, 35.905834457991055]
        o11=[31.975545405443768, 35.983319832850576]
        o12=[31.09237651904625, 35.51997034636367]
        o13=[30.8409266880119, 35.642957788698176]
        o14=[29.609248127247092, 35.020857775230226]

        x=0
        while x<1:
            v=0
            fname=str(input("first name : "))
            for i in fname:
                if not(i>='A' and i<='Z' or i>='a' and i<='z'):
                    v=v+1

            if v>0:
                print("please try again")
            elif v==0:
                x+=1

        c=0
        while c<1:
            v=0
            lname=str(input("last name : "))
            for i in lname:
                if not(i>='A' and i<='Z' or i>='a' and i<='z'):
                    v=v+1
            if v>0:
                print("please try again")
            elif v==0:
                c+=1

        TTUairways.name=fname.title()+" "+lname.title()
        title()

   
        a=0
        while a<1:
            q=float(input("Enter the place of departure number : "))

            if q==1:
                q=o1
                TTUairways.ty="Military Hospital Airport(Irbid)"
                a+=1
            elif q== 2:
                q=o2
                TTUairways.ty="JUST-Heliport(Irbid)"
                a+=1
            elif q== 3:
                q=o3
                TTUairways.ty="Helipad(Mafraq)"
                a+=1
            elif q== 4:
                q=o4
                TTUairways.ty="Royal Jordanian AirCargo(Amman)"
                a+=1
            elif q== 5:
                q=o5
                TTUairways.ty="Heliport(Amman)"
                a+=1
            elif q== 6:
                q=o6
                TTUairways.ty="GEAA Heliport(Amman)"
                a+=1
            elif q== 7:
                q=o7
                TTUairways.ty="Golden Eagle Aviation Academy(Amman)"
                a+=1
            elif q== 8:
                q=o8
                TTUairways.ty="Anti extortion(Amman)"
                a+=1
            elif q== 9:
                q=o9
                TTUairways.ty="Hospital Helipad(Amman)"
                a+=1
            elif q== 10:
                q=o10
                TTUairways.ty="Jordan Hospital Airstrip(Amman)"
                a+=1
            elif q== 11:
                q=o11
                TTUairways.ty="Amman Civil Airport(Amman)"
                a+=1
            elif q== 12:
                 q=o12
                 TTUairways.ty="Helipad(Karak)"
                 a+=1
            elif q== 13:
                    q=o13
                    TTUairways.ty="Tafila University Airport(Tafila)"
                    a+=1
            elif q== 14:
                    q=o14
                    TTUairways.ty="King Hussein International Airport(Aqaba)"
                    a+=1
            else:
                print("Please choose the correct place number :")

   


        a=0
        while a<1:
            w=int(input("Enter the landing place number : "))
            if w==1:
                w=o1
                TTUairways.tu="Military Hospital Airport(Irbid)"
                a+=1
            elif w== 2:
                w=o2
                TTUairways.tu="JUST-Heliport(Irbid)"
                a+=1
            elif w== 3:
                w=o3
                TTUairways.tu="Helipad(Mafraq)"
                a+=1
            elif w== 4:
                w=o4
                TTUairways.tu="Royal Jordanian AirCargo(Amman)"
                a+=1
            elif w== 5:
                w=o5
                TTUairways.tu="Heliport(Amman)"
                a+=1
            elif w== 6:
                w=o6
                TTUairways.tu="GEAA Heliport(Amman)"
                a+=1
            elif w== 7:
                w=o7
                TTUairways.tu="Golden Eagle Aviation Academy(Amman)"
                a+=1
            elif w== 8:
                w=o8
                TTUairways.tu="Anti extortion(Amman)"
                a+=1
            elif w== 9:
                w=o9
                TTUairways.tu="Hospital Helipad(Amman)"
                a+=1
            elif w== 10:
                w=o10
                TTUairways.tu="Jordan Hospital Airstrip(Amman)"
                a+=1
            elif w== 11:
                w=o11
                TTUairways.tu="Amman Civil Airport(Amman)"
                a+=1
            elif w== 12:
                 w=o12
                 TTUairways.tu="Helipad(Karak)"
                 a+=1
            elif w== 13:
                 w=o13
                 TTUairways.tu="Tafila University Airport(Tafila)"
                 a+=1
            elif w== 14:
                 w=o14
                 TTUairways.tu="King Hussein International Airport(Aqaba)"
                 a+=1
            else:
                print("Please choose the correct place number")
        #معادله حساب المسافه بين مسافتين
        lon1 = radians(q[1]) 
        lon2 = radians(w[1]) 
        lat1 = radians(q[0]) 
        lat2 = radians(w[0])
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        r = 6371
        TTUairways.km=format(c*r,".2f")
        TTUairways.kmm=format(c*r*0.40,".2f")
        #هون بتنتهي المعادله
        os.system('cls')
        TTUairways.title()
        print("\n\n\n*************************************  Now your flight ticket will be processed  ***************************************")
        time.sleep(5)
        for i in range(0,len(TTUairways.wanted)):
            if TTUairways.name==TTUairways.wanted[i]:
                TTUairways.DrawWanted()
                os.system('cls')
                TTUairways.title()
                print("\n\n\n*************************************  An error occurred, you are Wanted  ***************************************")

                break
        else:
                TTUairways.draw()
                os.system('cls')
                TTUairways.title()
                print("\n\n\n*************************************  Your flight ticket has been designed  ***************************************")
    
opj=TTUairways
opj.first()
