class Solution:
    def studentGrade(self, marks):
        marks = int(input())
        
        if marks >=101:
            print("apply for rechecking")
        elif marks >=90:
            print("Grade A")
        elif marks>=70:
            print("Grade B")
        elif marks>=50:
            pritn("Grade C")
        elif marks >=35:
            print("Grade D")
        else:
            print("Fail")

s = Solution
marks = 1-1
self = 0
s.studentGrade(self,marks)