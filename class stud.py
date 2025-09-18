class student:
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.rollno=c

    def display(self):
        print(self.name)
        print(self.age)
        print(self.rollno)
ob=student('balaji',17,0)
ob.display()
