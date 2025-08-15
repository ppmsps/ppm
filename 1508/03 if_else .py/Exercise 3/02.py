text = input("กรอกข้อความภาษาอังกฤษ : ")

has_upper = False
hes_lower = False

for chat in text:
    if "a" <=  chat <= "z":
        hes_lower = True
    elif "A" <= chat <= "Z":
        has_upper = True

if has_upper and hes_lower :
    print ("มีทั้งพิมพ์ใหญ่และพิมพ์เล็ก")
elif hes_lower :
    print ("มีเฉพาะพิมพ์เล็ก")
elif has_upper :
    print ("มีเฉพาะพิมพ์ใหญ่") 
else :
    print ("กรุณากรอกเพียงภาษาอังกฤษ")