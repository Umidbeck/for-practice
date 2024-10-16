def qoshish(a,b):
    return a+b

def ayirish(a,b):
    return a-b

def kopaytirish(a, b):
    return a*b

def bolish(a, b):
    if b == 0:
        print("0 ga bo'lib bo'lmaydi")
    else:
        return a / b
    
def kalkulyator():
    print("Kalkulyatorga xush kelibsiz!")
    print("Amallar:")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")
    
    while True:
        choice = input("Qaysiamalni tanlaysiz 1/2/3/4 yoki -chiqish- deb yozing")
        
        if choice == 'chiqish':
            print("Dastur tugadi")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Birinchi raqamni kiriting"))
                num2 = float(input("Ikkinchi raqamni kiriting"))
            except ValueError:
                print("Iltimos raqam kiriting")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {qoshish(num1,num2)}")
            elif choice =='2':
                print(f"{num1} - {num2} = {ayirish(num1,num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {kopaytirish(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {bolish(num1 , num2)}")
        else:
            print("Noto'g'ri variant terilgan")
            
kalkulyator()
            