class stud:
    def __init__(self,a,b,c,m1,m2,m3):
        self.sno=a
        self.sname=b
        self.sAge=c
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def calculate(self):
        self.tot=self.mark1+self.mark2+self.mark3
        self.avg=self.tot/3
        if m1>45 and m2>45 and m3>45:
            self.result="Pass"
        else:
            self.result="Fail"
    def display(self):
        print("Number:",self.sno)
        print("Name:",self.sname)
        print("Age:",self.sAge)
        print("mark1:",self.mark1)
        print("mark2:",self.mark2)
        print("mark3:",self.mark3)
        print("total:",self.tot)
        print("average:",self.avg)
        print("result:",self.result)
x=int(input("enter your rollno:"))
y=input("enter your name:")
z=int(input("enter your age:"))
m1=int(input("enter first mark:"))
m2=int(input("enter second matrk:"))
m3=int(input("enter third mark:"))
ob=stud(x,y,z,m1,m2,m3)
ob.calculate()
ob.display()




