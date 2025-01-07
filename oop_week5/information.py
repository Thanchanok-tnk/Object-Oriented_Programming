m = int(input('จำนวนคน : '))
for i in range(m):
    dic = {}
    print('กรุณากรอกข้อมูลคนที่ '+str(i+1))
    dic['name'] = input("กรุณากรอกชื่อ : ")
    dic['nickname'] = input("กรุณากรอกชื่อเล่น : ")
    dic['stdid'] = input("กรุณากรอกรหัสประจำตัวนักศึกษา : ")
    dic['hoppy'] = input("กรุณากรอกงานอดิเรก : ")
    dic['color'] = input("กรุณากรอกสีที่ชอบ : ")
    print('ข้อมูลคนที่ '+str(i+1))
    print(dic)