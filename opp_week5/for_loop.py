start = int(input("กรอกตัวเลขเริ่มต้น: "))
end = int(input("กรอกตัวเลขสุดท้าย: "))
for i in range(start, end + 1):
    if i % 3 == 0:
        continue
    print(i)