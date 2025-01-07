class Student:
    def __init__(self, name, student_id, age):
        """กำหนด attributes ของนักเรียน"""
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grades = {'คณิต': None, 'ไทย': None, 'อังกฤษ': None, 'วิทย์': None, 'สังคม': None}

    def set_grade(self, subject, score):
        """เพิ่มหรืออัปเดตคะแนนของวิชาแต่ละวิชา"""
        if subject in self.grades:
            self.grades[subject] = score
        else:
            print(f"ไม่พบวิชา {subject}")

    def score_to_grade(self, score):
        """เปลี่ยนคะแนนให้เป็นเกรด"""
        if score >= 80:
            return 'A'
        elif score >= 70:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self):
        """คำนวณเกรดเฉลี่ย"""
        total_score = 0
        subject_count = 0
        
        for score in self.grades.values():
            if score is not None:
                total_score += score
                subject_count += 1

        if subject_count == 0:
            return 0 
        return total_score / subject_count

    def show_student_info(self):
        """แสดงข้อมูลของนักเรียนทั้งหมด"""
        print(f"ชื่อ: {self.name}")
        print(f"หมายเลขประจำตัว: {self.student_id}")
        print(f"อายุ: {self.age} ปี")
        
        print("คะแนนและเกรดในแต่ละวิชา:")
        for subject, score in self.grades.items():
            if score is not None:
                grade = self.score_to_grade(score)
                print(f"  {subject}: {score} คะแนน (เกรด {grade})")
            else:
                print(f"  {subject}: ยังไม่มีคะแนน")
        
        gpa = self.calculate_gpa()
        print(f"ได้เกรดเฉลี่ย: {gpa:.2f}")

student = Student("ลินลาวดี", "12345", 16)
student.set_grade("คณิต", 85)
student.set_grade("ไทย", 74)
student.set_grade("อังกฤษ", 88)
student.set_grade("วิทย์", 65)
student.set_grade("สังคม", 56)

student.show_student_info()
