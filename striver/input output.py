class Solution:
    def studentGrade(self, marks):
        marks=int(input())
        if marks >=90:
            print("Grade A")
        elif marks>=70:
            print("Gradde B")
        elif marks >=50:
            print("Grade C")
        elif marks >=35:
            print("Grade D")
        else:
            print("Fail")

        return self

a=Solution
marks = 0
self = 0
a.studentGrade(self,marks)





