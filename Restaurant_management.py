import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    port="1124",
    user="root",
    password="mani",
    database="restaurant_db"

)
mycursor=mydb.cursor()
def insert_data(menu,menu_item,how_many,total):
    sql="insert into restaurant_register(menu,menu_item,how_many,total) values(%s,%s,%s,%s) "
    val=(menu,menu_item,how_many,total)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data inserted successfully")
def view_data():
    mycursor.execute("select * from restaurant_register ")
    result=mycursor.fetchall()
    for i in result:
        print(i)    
print("   *****WELCOME TO MMM RESTAURANT*****")
print("1. breakfast \n 2. lunch_veg \n 3. non_veg \n 4. dinner")
breakfast=["idly","dosa","poori","pongal","vadai"]
lunch_veg=["sambar_rice","lemon_rice","tomoto_rice","full_meals"]
non_veg=["chicken_biriyani","mutton_biriyani","fried_rice"]
dinner=["idly","dosa","parota"]
idly_am=6
dosa_am=25
poori_am=30
pongal_am=25
vada_am=10
sambarrice_am=50
lemonrice_am=45
tomotorice_am=55
fullmeals_am=75
chickenbiriyani_am=120
muttonbiriyani_am=150
friedrice_am=90
parota_am=35
menu=int(input("Enter your menu type:"))
def one():
    print("your breakfast is available")
    print("your menu is given below")    
    print(f"your menu items are:{breakfast}")
def two():
    print("your veg is available")
    print("your menu is given below")    
    print(f"your menu items are:{lunch_veg}")
def three():
    print("your non_veg is available")
    print("your menu is given below")    
    print(f"your menu items are:{non_veg}")
def four():
    print("your dinner is available")
    print("your menu is given below")    
    print(f"your menu items are:{dinner}")   
if menu==1:
    one()
    menu_item=input("Enter your menu item:").lower()
    if menu_item=="idly":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*idly_am
        print(f"your total bill is:{total}")
    elif menu_item=="dosa":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*dosa_am
        print(f"your total bill is:{total}")
    elif menu_item=="poori":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*poori_am
        print(f"your total bill is:{total}")
    elif menu_item=="pongal":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*pongal_am
        print(f"your total bill is:{total}")
    elif menu_item=="vada":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*vada_am
        print(f"your total bill is:{total}")
    else:
        print("your menu_item is not available")                
elif menu==2:
    two()
    menu_item=input("Enter your menu item:").lower()
    if menu_item=="sambar_rice":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*sambarrice_am
        print(f"your total bill is:{total}")
    elif menu_item=="lemon_rice":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*lemonrice_am
        print(f"your total bill is:{total}")
    elif menu_item=="tomoto_rice":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*tomotorice_am
        print(f"your total bill is:{total}")
    elif menu_item=="full_meals":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*fullmeals_am
        print(f"your total bill is:{total}") 
    else:
        print("your menu_item is not available")               
elif menu==3:
    three()
    menu_item=input("Enter your menu item:").lower()
    if menu_item=="chicken_biriyani":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*chickenbiriyani_am
        print(f"your total bill is:{total}")
    elif menu_item=="mutton_biriyani":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*muttonbiriyani_am
        print(f"your total bill is:{total}")
    elif menu_item=="fried_rice":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*friedrice_am
        print(f"your total bill is:{total}")
    else:
        print("your menu_item is not available")            
elif menu==4:
    four()
    menu_item=input("Enter your menu item:").lower()
    if menu_item=="parota":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*parota_am
        print(f"your total bill is:{total}")
    elif menu_item=="idly":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*idly_am
        print(f"your total bill is:{total}")
    elif menu_item=="dosa":
        print(f"your menu item is {menu_item}")
        how_many=int(input(f"how many you want:"))
        total=how_many*dosa_am
        print(f"your total bill is:{total}")    
    else:
        print("your menu_item is not available")
else:
    print("your menu is invalid")                    
print("THANKS FOR VISIT OUR RESTAURANT")
print("           ********VISIT AGAIN********")    
insert_data(menu,menu_item,how_many,total)
view_data()  
