while True:
    try:
        num1 = float(input("Enter number : "))
        num2 = float(input("Enter number : "))
        num3 = float(input("Enter number : "))
        break
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น")
max_number = max(num1,num2,num3)
print(f'จำนวนที่มากที่สุดคือ ',max_number)