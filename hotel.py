import sqlite3
myConnection=""
cursor=""
userName=""
passwd=""
roomrent=0
resturantbill=0
gamingbill=0
fashionbill=0
totalAmount=0
cid=""

def MYSQLconnectionCheck():
    global myConnection,userName,passwd
    userName=input("\n ENTER MYSQL SERVER'S USERNAME :")
    passwd=input("\n ENTER MYSQL SERVER'S PASSWORD :")
    myConnection=(mysql.connector.connect(host="localhost",user=userName,password=passwd))


if myConnection:
    print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED")
    cursor=myConnection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXIST HMS")
    cursor.execute("COMMIT")
    cursor.close()
#Sreturn myConnection
else:
    print("/nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD")  


#MODULE ESTABLISHED MYSQL CONNECTION

def MYSQLconnection():
    global userName
    global password
    global myConnection
    global cid

    myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password,database="HMS",
    auth_plugin="mysql_native_password")

    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        myConnection.close()


def userEntry():
    global cid
    if myConnection:
        cursor=myConnection.cursor(createTable="""CREATE TABLE IF NOT EXIST C_DETAILS (CID VARCHAR(20),C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),
        C_AGE VARCHAR(30),C_COUNTRY VARCHAR(30),P_NO VARCHAR(30),C_EMAIL VARCHAR(30))""")

        cursor.execute(createTable)
        sql="INSERT INTO C_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values=(cid,name,address,age,nationality,phoneno,email)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        print("\nNEW CUSTOMER ENTEREWD IN THE SYSTEM SUCCESSFULLY !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


def bookingRecord():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20),CHECK_IN DATE ,CHECK_OUT DATE)"
        cursor.execute(createTable)
        checkin=input("\n ENTER CUSTOMER CHECKIN DATE [ YYYY-MM-DD] :") 
        checkout=input("\n ENTER CUSTOMER CHECKOUT DATE [ YYYY-MM-DD]:") 
        sql="INSERT INTO BOOKING RECORD VALUES(%s,%s,%s)"
        values=(cid,checkin,checkout)
        curosr.execute(sql,values)
        cursor.execute("COMMIT")
        print("\nCHECKIN AND CHECKOUT ENTRY MADED SUCCESSFULLY !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def roomrent():
    global cid
    customer=searchCustomer()
    if customer:
        global roomrent
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20),ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT,ROOMRENT INT)"
            cursor.execute(createTable)
            print("\n #### WE HAVE THE FOLLOWING ROOMS FOR YOU####")
            print("  1. ULTRA ROYAL  >10000 Rs.")
            print("  2. ROYAL  >5000 Rs. ")
            print("  3. ELITE  >3500 Rs. ")
            print("  4. BUDGET >2500 Rs")
            roomchoice =int(input("ENTER YOUR OPTION :"))
            roomno=int(input("ENTER CUSTOMER ROOM NO :"))
            noofdays=int(input("ENTER NO OF DAYS :"))

            if roomchoice==1:
                roomrent = noofdays*10000
                print("\nULTRA ROYAL ROOM RENT:","roomrent")
            elif roomchoice==2:
                roomrent =noofdays*5000
                print("\nROYAL ROOM RENT :","roomrent") 
            elif roomchoice==3:
                roomrent=noofdays*3500
                print("\nELITE ROYAL ROOM RENT:","roomrent")
            elif roomchoice==4:
                roomrent=noofdays*2500
                print("\nBUDGET ROOM RENT:","roomrent")
            else:
                print("SORRY,MAY BE YOU ARE GIVING ME WRONG INPUT,PLEASE TRY AGAIN !!! ")
            return roomrent
            sql="INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%S)"
            values= (cid,roomchoice,noofdays,roomno,roomrent)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("THANK YOU , YOU ROOM HAS BEEN BOOKED FOR:",noofdays,"DAYS")
            print("YOUR TOTAL ROOM RENT IS:",roomrent,"RS")           
            cursor.close()

        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION")


def Restaurent():
    global cid
    customer=searchCustomer()
    if customer:
        global restaurentbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS RESTAURENT(CID VARCHAR(20),CUISINE VARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30))"
            cursor.execute(createTable)
            print("1. VEGETARIAN COMBO >300 Rs.")
            print("2. NON VEGETARIAN COMBO  >500 Rs.")
            print("3. VEGETARIAN AND NON VEGETARIAN COMBO >750 Rs.")

            choice_dish=int(input("ENTER YOUR CUSINE  :"))
            quantity=int(input("ENTER QUANTITY  :"))
            if choice_dish==1:
                print("\nSO YOU HAVE ORDER: VEGETARIAN COMBO ")
                restaurentbill = quantity*300
            elif choice_dish==2:
                print("\nSO YOU HAVE ORDER : NON VEGETARIAN COMBO  ")
                restaurentbill= quantity*500
            elif choice_dish==3:
                print("\nSO YOU HAVE ORDER : VEGETARIAN AND NON VEGETARIAN COMBO ")
                restaurentbill =quantity*750
            else:
                print("SORRY! MAY BE YOU ARE GIVING ME WRONG INPUT , PLEASE TRY AGAIN !!!")

            return restaurentbill
            sql= "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s)"
            values= (cid,choice_dish,quantity,restaurentbill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("YOUR TOTAL BILL IS : Rs",restaurentbill)
            print("\n\n***** WE HOPE YPU WILL ENJOY YOUR MEAL ****\n\n")
            cursor.close()
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION !")

def Gaming():
    global cid
    customer=searchCustomer()
    if customer:
        global gamingbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20),GAMES VARCHAR(30),HOURS VARCHAR(30),GAMING_BILL VARCHAR(30))"
            cursor.execute(createTable)
            print("1. TABLE TENNIS> 150 Rs./Hr.")
            print("2. BOWLING> 100 Rs./Hr")
            print("3. SNOOKER>250 Rs./Hr")
            print("4. VR WORLD GAMING>400 Rs./Hr")
            print("5. VIDEO GAMES> 300Rs./HR")
            print("6. SWIMMING POOL GAMES> 350 Rs./HR")
            print("7. EXIT")

            game=int(input("ENTER WHAT GAME YOU WANT TO PLAY :"))
            hour=int(input("ENTER THE NPO OF HOURS YOU WANT TO PLAY :"))
            if game==1:
                print("YOU HAVE SELECTED TO PLAY : TABLE TENNIS")
                gamingbill= hour*150
            elif game==2:
                print("YOU HAVE SELECTED TO PLAY: BOWLING ")
                gamingbill= hour* 100
            elif game==3:
                print("YOU HAVE SELECTED TO PLAY: SNOOKER ")
                gamingbill= hour* 250
            elif game==4:
                print("YOU HAVE SELECTED TO PLAY:")
                gamingbill= hour*400
            elif game==5:
                print("YOU HAVE SELECTED TO PLAY: VIDEO GAMING")
                gamingbill=hour*300
            elif game==6:
                print("YOU HAVE SELECTED TO PLAY : SWIMMING POOL GAMES")
                gamingbill= hour*350
            else:
                print("SORRY ! MAY YOU ARE GIVING ME WRONG INPUT, PLEASE TRY AGAIN !!!")
            return gamingbill

            sql= "INSERT INTO  GAMING VALUES (%s,%s,%s,%s)"
            values=(cid,game,hour,gamingbill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("YOUR TOTAL GAMING BILL IS: Rs.",gamingbill)
            print("FOR: ",hour," HOURS","/n****WE HOPE YOU WILL ENJOY YOUR GAME****")
            cursor.close()            
    else:
        print("EROR ESTABLISHING MYSQL CONNECTION!")


def Fashion():
    global cid
    customer=searchCustomer()
    if customer:
        global fashionbill
        if myConnection:
            cursor=myConnecyion.cursor()
            createTable= "CREATE TABLE IF NOT EXISTS FASHION(CID VARCHAR(30), DRESS VARCHAR(30),AMOUNT VARCHAR(30),BILL VARCHAR(30))"
            cursor.execute(createTable)
            print("1.SHIRTS >1500 Rs.")
            print("2. T-SHIRTS >300 Rs.")
            print("3.PANTS >2000 Rs.")
            print("4.JEANS >4000 Rs.")
            print("5.TASSEL TOWN 500Rs.")
            print("6.GOWN >3000 Rs.")
            print("7.WESTERN DRESS >3000 Rs.")
            print("8.SKIRTS >400Rs.")
            print("9.TROUSERS >200Rs.")
            print("10.INNERWEARS >30Rs.")
            dress=int(input("ENTER THE CHOISCE YOU WEAR: "))
            quantity=int(input("HOW MANY YOU WANT TO BUY: "))
            if dress==1:
                print("/nSHIRTS")
                fashionbill=quantity*1500
            elif dress==2:
                print("/nT-SHIRTS")
                fashionbill=quantity*300
            elif dress==3:
                print("/nPANTS")
                fashionbill=quantity*2000
            elif dress==4:
                print("/nJEANS")
                fashionbill=quantity*4000
            elif dress==5:
                print("/nTASSEL TOP")
                fashionbill=quantity*500
            elif dress==6:
                print("/nGOWN")
                fashionbill=quantity*3000
            elif dress==7:
                print("/nWESTERN DRESS")
                fashionbill=quantity*3000
            elif dress==8:
                print("/nskirts")
                fashionbill=quantity*400
            elif dress==9:
                print("/nTROUSERS")
                fashionbill=quantity*200
            elif dress==10:
                print("/nINNERWEARS")
                fashionbill=quantity*30
            else:
                print("SORRY! MAY BE YOU ARE GIVING ME WRONG INPUT, PLEASE TRY AGAIN")

            return fashionbill
            sql="INSERT INTO FASHION VALUES(%s,%s,%s,%s)"
            values= (cid,dress,quantity,fashionbill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("\nYOU SELECT ITEM NO :",dress,"\nYOUR QUANTITY IS :",quantity,"ITEMS","\nTHANK YOU FOR SHOOPING VISIT AGAIN !!!")
            print("\nYOUR TOTAL BILL IS:",fashionbill)
            cursor.close()
        else:
            print("/nERROR ESTABLISHING MYSQL CONNECTION !")


def totalAmount():
    global cid
    customer=searchCustomer()
    if customer:
        global grandTotal,roomrent,restaurentbill,fashionbill,gamingbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable="CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20),C_NAME VARCHAR(30),ROOMRENT INT,RESTAURENT BILL INT,GAMINGBILL INT,FASHIONBILL INT,TOTALAMOUNT INT)"
            cursor.execute(createTable)
            sql="INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            name=input("ENTER CUSTOMER NAME: ")
            grandtotal=roomrent+restaurentbill+fashionbill+gamingbill
            values=(cid,name,roomrent,restaurentbill,gamingbil,fashionbill,grandTotal)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")

            print("\n *** CROWN PLAZA MIAMI *** CUSTOMEER BILLING ***")
            print("\n CUSTOMER NAME :",name)
            print("\nROOM RENT :Rs",roomrent)
            print("\nRESTAURENT BILL :Rs",restaurentbill)
            print("\nFASHION BILL :Rs",fashionbill)
            print("\nGAMING BILL :Rs",gamingbill)
            print("\nTOTAL AMOUNT:Rs",grandTotal)
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def searchOldbill():
    global cid
    customer=searchCustomer()
    if customer:
        cursor=myConnection.cursor()
        sql="SELECT * FROM TOTAL WHERE CID = %s"
        cursor.execute(sql,(cid))
        data=customer.fetchall()
        if data:
            print(data)
        else:
            print("RECORD NOT FOUND TRY AGAIN!")
        cursor.close()
    else:
        print("\nSOMETHING WENT WRONG,PLEASE TRY AGAIN")


def searchCustomer():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("ENTER CUSTOMER ID :")
        sql="SELECT * FROM C_DETAILS WHERE CID=%s"
        cursor.execute(sql,(cid))
        data=cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            print("RECORD NOT FOUND TRY AGAIN !")
            return False
        cursor.close()
    else:
        print("\nSOMETHING WENT WRONG , PLESE TRY AGAIN !")


print("""********SARASWATI V MANDIOR VIVEKANAND NAGAR SLN*********** HOTEL MANAGEMENT SYSTEM*************CROWN PLAZA MIAMI**********""")

myConnection=MYSQLconnectionCheck()
if myConnection:
    MYSQLconnection()
    while True:
        print("1-->ENTER CUSTOMER DETAILS")
        print("2--->BOOKING RECORD")
        print("3--->CALCULATE ROOM RENT")
        print("4--->CALCULATE RESTAURENT BILL")
        print("5--->CALCULATE GAMING BILL")
        print("6--->CALCULATE FASHION STORE BILL")
        print("7--->DISPLAY Customer DETAILS")
        print("8--->GENERATE TOTAL BILL AMOUNT")
        print("9--->GENERATE TOTAL BILL")
        print("10--->EXIT")
        choice=int(input("ENTER YOUR CHOICE"))
        if choice==1:
            userEntry()
        if choice==2:
            bookingRecord()
        if choice==3:
            roomRent()
        elif choice==4:
            Restaurent()
        elif choice==5:
            Gaming()
        elif choice==6:
            Fashion()
        elif choice==7:
            searchCustomer()
        elif choice==8:
            totalAmount()
        elif choice==9:
            searchOldBill()
        elif choice==10:
            break
        else:
            print("SORRY MAY BE YOU ARE GIVING ME WRONG INPUT, PLEASE TRY AGAIN !!!")
else:
    print("\nERROR ESTABLIASHING MYSQL CONNECTION !")                                                




        


        


