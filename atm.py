a=input("Hello, Please tell me your name ")
print("Welcome, " + a)
b=input("Please choose your option from below\nTransaction\nBalance Enquiry\n")
b=int(b)
m=50000
if b==1:
    c=input("please enter your PIN: ")
    c=int(c)
    if c==7866:
        d=input("please enter your amount ")
        d=int(d)
        print("collect your cash, Thanks\n")
        print("your available balance is: ",m-d) 
    else:
        print("incorrect password, Try again\n")
else:
    c=input("please enter your PIN: ")
    c=int(c)
    if c==7866:
        print("Your available balance is ", m)

print("Thanks a lot")

