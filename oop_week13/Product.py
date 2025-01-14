class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.__price = price
        self.__stock = stock
    
    def add(self, amount):  # เพิ่มจำนวน
        self.__stock += amount
        print(f"- เพิ่มสินค้า {self.name} จำนวน {amount} ชิ้นสำเร็จ ยอดคงเหลือในสต๊อก: {self.__stock} ชิ้น")  
    def remove(self, amount):  # ลดจำนวน
        if amount <= self.__stock:
            self.__stock -= amount
        else:
            print('จำนวนสินค้าในสต็อกไม่เพียงพอ')
    def update(self, new_price):  # แก้ไขราคา
        if new_price > 0:
            self.__price = new_price
            print(f"- ปรับราคา {self.name} เป็น {self.__price} บาทสำเร็จ")
        else:
            print("ราคาต้องมากกว่า 0 บาท")
    def showstock(self):  # ตรวจสอบ
        print(self.__stock)
        return self.__stock    
    def show_product_info(self):  # แสดงข้อมูลสินค้า
        return (f"Product ID: {self.id}\n"
                f"Product Name: {self.name}\n"
                f"Price: {self.__price} บาท\n"
                f"Stock: {self.__stock} units")

class Phone(Product):
    def __init__(self, id, name, price, stock, brand):
        super().__init__(id, name, price, stock)  
        self.brand = brand    
    def showinfo(self):
        return f"แบรนด์ {self.brand} มี {super().show_product_info()}"
    
class Notebook(Product):
    def __init__(self, id, name, price, stock, brand):
        super().__init__(id, name, price, stock)  
        self.brand = brand    
    def showinfo(self):
        return f"แบรนด์ {self.brand} มี {super().show_product_info()}"
    
class Clothes(Product):
    def __init__(self, id, name, price, stock, brand):
        super().__init__(id, name, price, stock)  
        self.brand = brand    
    def showinfo(self):
        return f"แบรนด์ {self.brand} มี {super().show_product_info()}"

# ทดสอบการทำงาน ตรวจสอบข้อมูลสินค้า
product1 = Product(1, "เครื่องซักผ้า", 50000, 14)
print(product1.show_product_info()) 
product1.add(14)  # เพิ่ม
product1.remove(14)  # ลด
product1.update(35000)  # แก้ไข
product1.show_product_info() 

phone1 = Phone(2, "iPhone 20", 115000, 50, "Apple")
print(phone1.showinfo()) 
phone1.add(40)  # เพิ่ม
phone1.remove(5)  # ลด
phone1.update(33999)  # แก้ไข
phone1.show_product_info()  

notebook1 = Notebook(3, "HP Probook 440 G8 Standard SET", 32500, 10 , "HP")
print(notebook1.showinfo()) 
notebook1.add(70)  # เพิ่ม
notebook1.remove(10)  # ลด
notebook1.update(33000)  # แก้ไข
notebook1.show_product_info()  

clothes1 = Clothes(4, "เสื้อฮู้ด Celine ทรงหลวมผ้าคอตตอนฟลีซ", 37000, 45 , "h&m")
print(clothes1.showinfo()) 
notebook1.add(6)  # เพิ่ม
notebook1.remove(10)  # ลด
notebook1.update(36000)  # แก้ไข
notebook1.show_product_info() 