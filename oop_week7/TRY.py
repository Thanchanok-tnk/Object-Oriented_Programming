while True:
    try:
        print('---โปรแกรมหาพื้นที่ 4 เหลี่ยม---')
        a = int(input('ใส่ค่าความยาว: '))
        b = int(input('ใส่ค่าความกว้าง: '))
        
        if a == 0 or b == 0:
           raise ZeroDivisionError    
        elif a < 0 or b <0:
            raise Exception
        g = a * b
        print(f'พื้นที่ 4 เหลี่ยมคือ: {g}')
              
        print('---โปรแกรมหาพื้นที่ 3 เหลี่ยม---')
        a = int(input('ใส่ค่าความความสูง: '))
        b = int(input('ใส่ค่าความความยาวของฐาน: '))
        
        if a == 0 or b == 0:
           raise ZeroDivisionError    
        elif a < 0 or b <0:
            raise Exception
        g = 1.2*a * b
        print(f'พื้นที่ 3 เหลี่ยมคือ: {g}')

        print('---โปรแกรมหาพื้นที่วงกลม---')
        a = int(input('ใส่ค่ารัศมีของวงกลม: '))
        
        if a == 0 :
           raise ZeroDivisionError    
        elif a < 0 or b <0:
            raise Exception
        g = 3.14 * a**2
        print(f'พื้นที่วงกลมคือ: {g}')
    
    except ValueError:
        print('ใส่เฉพาะตัวเลข')
    except ZeroDivisionError:
        print('ห้ามใส่ค่าเป็น 0')
    except :
        print('ห้ามใส่ค่าติดลบ')
