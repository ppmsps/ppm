while True :
    try :
        number = float(input("Enter number : "))
        break
    except ValueError :
        print ("กรอกตัวเลขเท่านั้น")
if number >0 :
    print ("ตัวเลขนี้เป็นจำนวนบวก")
elif number <0 :
    print ("ตัวเลขนี้เป็นจำนวนลบ")
else :
    print ("ตัวเลขนี้เป็นจำนวนศูนย์")