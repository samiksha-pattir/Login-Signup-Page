import json
import re
import os
print("welcome in login and signup page")
file=os.path.isfile("signup.json")
print(file)
if file ==False:
    l=[]
    with open("signup.json","a")as h:
        a=json.dump(l,h,indent=4)
user=input("what you want to do login and signup:")
if user=="signup":
    n=input("enter your name")
    number=int(input("enter the number"))
    bnumber=list(str(number))
    if len(bnumber)==10 and bnumber!=0:
        d=open("signup.json","r")
        n2=d.read()
        if n not in n2:
            print("create a strong password with a mixture of letter number and symbols")
        def pas():
            paas=input("enter your password")
            if (re.search(("[a-z A-Z]"),paas)and re.search("[0-9]",paas)and(re.search("[@#$&]",paas))):
                print("yes")
                if len(paas)>=8:
                    confirm=input("enter the comfirm password:")
                    if paas==confirm:
                        print("correct password")
                        date=int(input("enter your date of birth"))
                        if date>=1 and date<=31:
                            month=int(input("enter the month"))
                            if month>=1 and month<=12:
                                year=int(input("enter the year"))
                                if year>0:
                                    g=input("enter your gender male or female")
                                    if g=="female" or g=="male":
                                        gmail=input("enter your own gmail")
                                        if (re.search(("[a-z A-Z]"),paas)and re.search("[0-9]",paas)and(re.search("[@#$&]",paas))):
                                            print(n,"your signup is successfully")
                                            dic={"name":n,"password":paas,"date":date,"month":month,"year":year,"gender":g,"gmail":gmail}
                                            with open("signup.json","r")as z:
                                                data=json.load(z)
                                                data.append(dic)
                                                with open("signup.json","w")as z:
                                                    json.dump(data,z,indent=4)
                    else:
                        print("password not matched")
                        pas()
                else:
                    print("password must be longer than8 charcter")
                    pas()
            else:
                print("invalid password","password")
        pas()
elif user=="login":
    usernme=input("enter your name")
    a1=input("enter the password")
    with open("signup.json","r") as q:
        da=json.load(q)
        for i in range (len(da)):
            if da[i]["name"]==usernme:
               if da[i]["password"]==a1:
                   print("login successfully")
                   print("your name is",da[i]["name"],"\n")
                   print("and your data is :-\n")
                   for x,y in da[i].items():
                    print(x,"=",y)
                    print("you are login suceesfull")
               else:
                   print("incorrect  password")
                   break
            else:
                print("enter correct user name")