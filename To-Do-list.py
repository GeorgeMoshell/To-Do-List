from tabulate import tabulate
import datetime as d


ans_name = "someone"
password = 'none'
i = 0
print("Hi User, Who are you")

while not ans_name =="Fluke":
    ans_name = input()
    if ans_name == "Fluke":
        print("Please Enter a password")
        while not password == 'Frontier2020':
            password = input()
            if password == 'Frontier2020':
                print("welcome Fluke")
            else:
                print('Password incorrect')
    else:
        print("This User aren't allowed")


def time():
    d.d.now()
    print(d.strftime("%x"))

time()
