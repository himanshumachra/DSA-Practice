class student:
    school="N.M.C"
    schol_phn= "+91-946655885"
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def avg(self):
        a=self.marks1+self.marks2+self.marks3
        av=float(a/300*100)
        print("The average marks of",self.name,"in 3 subjects are",av,"%")

s1=student("raj",99,98,97)
s1.name="jack sparo"
s1.avg()