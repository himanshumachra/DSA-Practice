class Solution:
    def whichWeekDay(self, day):
        match day :
            case 1:
                print("monday")
            case 2:
                print("tuesday")
            case 3:
                print("wednesday")
            case 4:
                print("thursday")
            case 5:
                print("friday")
            case 6:
                print("saturday")
            case 7:
                print("sunday")
            case _:
                print("use numbers from 1 to 7 insted of :",day)
        return self
s=Solution()
s.whichWeekDay(4)
"""
class Solution:
    def whichWeekDay(self, day):
        day = input()
        match day :
            case "1":
                print("monday")
            case "2":
                print("tuesday")
            case "3":
                print("wednesday")
            case "4":
                print("thursday")
            case "5":
                print("friday")
            case "6":
                print("saturday")
            case "7":
                print("sunday")
            case _:
                print("use numbers from 1 to 7 insted of :",day)
        return self
s=Solution()
self = 0
day = 0
s.whichWeekDay(self,day)

"""