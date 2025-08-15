while True :
    try :
        score1 = int(input("Enter Number : "))
        score2 = int(input("Enter Number : "))
        score3 = int(input("Enter Number : "))
        break
    except ValueError :
         print("กรุณากรอกตัวเลขเท่านั้น")
sum_score = (score1+score2+score3) / 3
print (f"ค่าเฉลี่ยคือ ",  sum_score)

if sum_score > 95 :
    print ("Congratulations")