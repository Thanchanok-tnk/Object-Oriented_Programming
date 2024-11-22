import random 

class studer:
    def __init__(self,ชื่อนามสกุล,ชื่อเล่น):
       self.name = ชื่อนามสกุล
       self.nikename = ชื่อเล่น
       self.score = random.randint(1,10)

    def scores(self):
        if self.score >= 5:
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.score} : คุณผ่าน")
        else :
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.score} : คุณตก")

studer1 = studer("นันท์ธิชา ว่องย่อง","ไอซ์")
studer2 = studer("ลินลาวดี ไกลถิ่น","สิลลี่")
studer3 = studer("ศศิวมล แซ่ด่าน","แบม")
studer4 = studer("วิไลวรรณ พลเดช","แมว")
studer5 = studer("หนี่งธิดา อินทรชัย","ตัง")

studer1.scores()
studer2.scores()
studer3.scores()
studer4.scores()
studer5.scores()
    
