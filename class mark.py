class mark:
    def __init__(self,a,b,c):
        self.mark=a
        self.mark=b
        self.mark=c
    def display(self):
        print(self.mark)
        print(self.mark)
        print(self.mark)
x=int(input("enter first mark:"))
y=int(input("enter second mark:"))
z=int(input("enter third mark:"))
ob=mark(x,y,z)
ob.display()
