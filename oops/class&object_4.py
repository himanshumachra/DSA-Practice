class bank:
    __bnk_bal=8596742

    def bl(self):
        print(self.__bnk_bal)

c1=bank()
c1.bl()
#c1.__bnk_bal  #"""it is private we can`it access as a user but like as we created a function which calls the balance inside the class so it prints"""