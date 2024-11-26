r = 0
print('โปรแกรมบวกค่า ถ้าต้องการออกจากโปรแกรมกรุณาพิมพ์ "หยุด"')
while True:
    try:
        num = input('ใส่ค่า : ')
        if num == "หยุด":
            print(f'ผลรวมทั้งหมด {r}')
            print('โปรแกรมสิ้นสุด')
            break

        num = int(num)
        if num == 0:
            raise ZeroDivisionError
                 
        elif num < 0:
            raise Exception

        r = r + num
        print(f'ผลรวมตอนนี้ {r}')
        print('--------------------------------------')

    except ValueError:
        print('ใส่เฉพาะตัวเลข')
    except ZeroDivisionError:
        print('ห้ามใส่ค่าเป็น 0')
    except :
        print('ห้ามใส่ค่าติดลบ')