import random 

class student:
    def __init__(self, ชื่อนามสกุล, ชื่อเล่น):
        self.name = ชื่อนามสกุล
        self.nikename = ชื่อเล่น
        self.score = random.randint(1, 10)

    def scores(self):
        if self.score >= 5:
            print(f"ชื่อ-นามสกุล : {self.name}, ชื่อเล่น : {self.nikename}, คะแนน : {self.score} : คุณผ่าน")
        else:
            print(f"ชื่อ-นามสกุล : {self.name}, ชื่อเล่น : {self.nikename}, คะแนน : {self.score} : คุณตก")
    
    def solve(self):
        if self.score < 5:
            print(f"ชื่อ-นามสกุล : {self.name}, ชื่อเล่น : {self.nikename} กำลังสอบแก้")
            self.score = random.randint(1, 10)
            if self.score >= 5:
                print(f"คะแนนหลังสอบแก้ : {self.score} : คุณผ่าน")
            else:
                print(f"คะแนนหลังสอบแก้ : {self.score} : คุณยังไม่ผ่าน")
        else:
            print(f"ชื่อ-นามสกุล : {self.name}, ชื่อเล่น : {self.nikename} ไม่ต้องสอบแก้ *คุณผ่านแล้ว*")

student1 = student("นันท์ธิชา ว่องย่อง", "ไอซ์")
student2 = student("ลินลาวดี ไกลถิ่น", "สิลลี่")
student3 = student("ศศิวมล แซ่ด่าน", "แบม")
student4 = student("วิไลวรรณ พลเดช", "แมว")
student5 = student("หนี่งธิดา อินทรชัย", "ตัง")

student1.scores()
student2.scores()
student3.scores()
student4.scores()
student5.scores()

print("\n สอบแก้สำหรับคนที่สอบไม่ผ่าน")
student1.solve()
student2.solve()
student3.solve()
student4.solve()
student5.solve()