a = 0
while True :
    num = int(input('ใส่ค่า :'))
    a = a + num
    print(f'ผลรวมตอนนี้ {a}')
    if num == 0:
        print(f'ผลรวมทั้งหมด {a}')
        break