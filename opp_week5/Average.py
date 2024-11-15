n = []
no = int(input("จำนวนตัวเลข : "))
for i in range(no):
    number = int(input('ป้อนตัวเลข : '))
    n.append (number)
u = sum(n) / len(n)
print(n)
print(f'ค่าเฉลี่ย{u}')