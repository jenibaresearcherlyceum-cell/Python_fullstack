class student:
    def __init__(self,sid,name,marks):
        self.sid=sid
        self.name=name
        self.marks=marks
    def calculate_average(self):
        total=sum(self.marks)
        avg=total/len(self.marks)
        return avg
    def display_details(self):
        print("ID:",self.sid)
        print("Name:",self.name)
        print("Marks:",self.marks)
        print("Average:",self.calculate_average())
        
s1=student(101,"Jeni",[80,85,90])
s1.display_details()
