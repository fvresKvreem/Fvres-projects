#Register acount
print("Please register a new account")
User =input("Enter Username:")
Pass =input("Enter Password:")
Pass2 =input("Re-Enter Password:")
while len(Pass)<8:
   print("Password must be atleast 8 charcters")
   Pass =input("Enter Password:")
   Pass2 =input("Re-Enter Password:")
if Pass2 != Pass:
    print("Error Passwords don't match")
    Pass =input("Enter Password:")
    Pass2 =input("Re-Enter Password:") 
    if Pass==Pass2:
      print("successfully registered")

#Login
print("Login to your account")
User_Login=input("Enter Username")
Password_Login=input("Enter Password")
if User_Login != User and Pass!=Password_Login:
    print("Username and Password is wrong")
    User_Login=input("Enter Username")
    Password_Login=input("Enter Password")
    if User_Login == User and Pass==Password_Login:
       print("successfully Logged in") 
elif User_Login != User or Pass != Password_Login:
    print("Username or Password is Wrong")
    User_Login=input("Enter Username")
    Password_Login=input("Enter Password")
    if User_Login == User and Pass==Password_Login:
     print("successfully Logged in")   
else:
    print("successfully Logged in")
    


