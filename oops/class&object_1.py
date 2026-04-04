class car:
    brand="mercedes"

    def __init__(self,color,model_name,wheels,engine,EV):
        self.color=color
        self.wheels=wheels
        self.engine=engine
        self.EV=EV
        self.model_name=model_name
#----------------------------------------------------------------------------------------------
    def welcome(self): #self is compulsery to write hare 
#----------------------------------------------------------------------------
        #here car.brand is the class attribute
        print(car.brand,"having a greate model named as","this",self.model_name,"have a 2998cc",self.engine,"and this is not an",self.EV)

# the above one is class we created it and storeded the informations in it so now we use it and call these stored values when we need them we dont re declaer these values and all 
#-------------------------------------------------------------------------------------------------
car1=car("blue",4,"Petrol","no","i20")
print(car1.color,"\n",car1.engine,"\n",car1.EV)  # here we car calling the values of the car class in the car1 object so we dont need to declare it multiple times and we can use it as we  wana use it 
car1.welcome()