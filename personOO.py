from datetime import date 

class __Person:
    def __init__(self, name, height, birthday):
        self.name = name
        self.height = height
        self.birthday = birthday
    
    def age(self):
        self.day = int(self.birthday[:2])
        self.month = int(self.birthday[2:4])
        self.year = int(self.birthday[4:8])        
        
        self.today = date.today()

        self.age = self.today.year - self.year - ((self.today.month, self.today.day) < (self.month, self.day))
        return self.age

    def showInfo(self):
        self.age()
        print( f'\n\n Your name is {self.name} \n you are {self.height} ft\n you born on {self.birthday[0:2]} / {self.birthday[2:4]} / {self.birthday[4:8]} \n and completed {self.age} years\n\n') 

person = __Person(
    input('Type your name: '),
    input('Type your height: '),
    input('Type your birthday in the format (MMDDYYYY): ')
)

person.showInfo()

    


