def sum(d1,d2):
    result={}
    result["h"]=d1["h"]+d2["h"]
    result["m"]=d1["m"]+d2["m"]
    result["s"]=d1["s"]+d2["s"]
    if  result["s"]>=60:
        result["s"]-=60
        result["m"]+=1
        
    if  result["m"]>=60:
        result["h"]+=1
        result["m"]-=60
        
    if  result["h"]>=24:
        print("invalid!")
        result={"h":0 , "m":0 , "s":0}
    return result    


def minus(d1,d2):
    result={}
    result['h']=d2['h']-d1['h']
    result['m']=d2['m']-d1['m']
    result['s']=d2['s']-d1['s']
    if result["s"]<0:
       result["m"]-=1
       result["s"]+=60
        
    if result["m"]<0:
       result["h"]-=1
       result["s"]+=60
        
    if result["h"]<0:
        print("invalid!")
        
        
    return result


def show(result):
    print(f'{result["h"]}: {result["m"]} : {result["s"]}')


d1={"h":int(input("first hour:")) , "m":int(input("first minute:")) , "s":int(input("first sanie:"))}
d2={"h":int(input("second hour:")) , "m":int(input("second minute:")) , "s":int(input("second sanie:"))}

result_s= sum(d1,d2)
show(result_s)

result_m= minus(d1,d2)
show(result_m)