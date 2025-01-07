class Salay :
    def __init__(self,name,occu,money):
        self.name = name
        self.occu = occu
        self.money = money
        self.yesr = 12 * money
    
    def answer(self):
        print (f"{self.name} ประกอบอาชีพ {self.occu} มีเงินเดือนทั้งปี = {self.money}")  
    
    def salaymoney(self,yesr):
        self.yesr = yesr
        self.answer()     
       
        return self.yesr   

emp1 = Salay('โซเฟีย',"ครู","144000")
emp2 = Salay('ปีเตอร์',"หมอ","540000")
emp3 = Salay('ป๊อบ',"โปรแกรมเมอร์","480000")

(emp1.answer())
(emp2.answer())
(emp3.answer())