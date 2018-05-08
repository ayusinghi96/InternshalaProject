#making a calculator
def add(x,y):
    z = x + y
    print(z)
def sub(x,y):
    z = x - y
    print(z)
def multi(x,y):
    z = x * y
    print(z)
def div(x,y):
    z = x / y
    print(z)



again = True
while again:
    print("Enter first no.:")
    a = float(input())
    print("Enter the second no.")
    b = float(input())
    print("Enter A for addition,S for subtraction,M for multiplication,D for division:")
    ans = input()
    if ans is 'A':
        add(a,b)
    elif ans is 'S':
        sub(a,b)
    elif ans is 'M':
        mutlti(a,b)
    else:
        div(a,b)
    print("Do you wish to countinue? (Y/N)")
    rep = input()
    if rep is not "Y":
        again = False

        
        
    
