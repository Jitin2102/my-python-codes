class Restaurent:
    def __init__(self,name):
        self.name=name
        pass
    def describe_restro(self):
        print("It is \'The Grand Palace\' Hotel.\nWelcome to Our Hotel !!!")
        print("It is an old restaurent.\nIt serves very delicious and healthy food.\nThe workers of this restaurent are very polite to their customers. ")       
    def open_restro(self):
        print("It opens at 10:00 am and closes at 11:00 pm .")    
my_restaurent=Restaurent('The Grand Palace') 
my_restaurent.describe_restro()
my_restaurent.open_restro()       