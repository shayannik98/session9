#kasr app
#shayan nikpour

def sum(f1,f2):
    result={}
    result['s']=(f1['s']*f2['m']+ f2['s']*f1['m'])
    result['m']=f1['m']*f2['m']
    return result
def multiply(f1,f2):
    result={}
    result['s']=f1["s"]*f2["s"]
    result['m']=f1["m"]*f2["m"]
    return result
def taghsim(f1,f2):
    result={}
    result['s']=(f1['s']* f2['m'])
    result['m']=(f1['m']* f2['s'])
    return result
def minus(f1,f2):
    result={}
    result['s']=(((f1['m']*f2['m']/f1['m'])*f1['s'])- (f1['m']*f2['m']/ f2['m'])*f2['s'])
    result['m']=(f1['m']*f2['m'])
    return result
def show(r):
    print(f'{r["s"]} / {r["m"]}')

def options():
    while 1:
        num1=float(input("surate kasr aval ra vared konid: "))
        num2=float(input("makhraje kasre aval ra vared konid : "))
        if num2==0:
            print("invalid number")
            while 1:
                num2=float(input("kasr ra mojadadan vared konid : "))
                if num2!=0:
                    break
        num3=float(input("surate kasr dovom ra vared konid : "))
        num4=float(input("makhraje kasr dovom ra vared konid: "))
        if num4==0:
            print("invalid number")
            while 1:
                num4=float(input("kasr ra mojadadan vared konid: "))
                if num4!=0:
                    break
                
        print(f"kasr aval :\n  {num1}/{num2} va kasr dovom: {num3}/{num4} ")
        break
        
    f1={"s":num1 ,  "m":num2}
    f2={"s":num3 ,  "m":num4} 

    print("choose from options \t 1: sum  \t 2:multiply \t 3:minus  \t 4:taghsim")
    option=int(input())
    if option==1:
        show(sum(f1,f2))
    elif option==2:
        show(multiply(f1,f2))
    elif option==3:
        show(minus(f1,f2))
    elif option==4:
        show(taghsim(f1,f2))
    else:
        print("invalid input")


options()       
        

