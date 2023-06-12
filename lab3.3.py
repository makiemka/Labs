def m(lang, a):
    if lang=="rus":
        if a==1:
            print("Январь")
        elif a==2:
            print("февраль")
        elif a== 3:
            print("Март")
        elif   a == 4:
            print("Апрель")
        elif  a == 5:
            print("май" )
        elif  a == 6:
            print("Июнь")
        elif  a == 7:
            print("Июль")
        elif a == 8:
            print("август")
        elif a==9:
            print("сентября")
        elif a==10:
            print("Октябрь")
        elif a==11:
            print("ноябрь")
        elif a==12:
            print("Декабрь")
    elif lang=="en":
        if a==1:
            print("January")
        elif a==2:
            print("february")
        elif a==3:
            print("march")
        elif a==4:
            print("April")
        elif a==5:
            print("may")
        elif a==6:
            print("june")
        elif a==7:
            print("July")
        elif a==8:
            print("August")
        elif a==9:
            print("September")
        elif a==10:
            print("Octobrt")
        elif a==11:
            print("November")
        elif a==12:
            print("December")
 
 
if __name__ == '__main__':
    lang=str(input())
    a=int(input())
    m(lang,a)
