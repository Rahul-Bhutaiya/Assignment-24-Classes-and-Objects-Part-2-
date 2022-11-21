class user:

    def __init__(self,name=None,age=None,email=None):
        self.name=name
        self.age=age
        if self.age<0:
            print('Age Can Not Be Less Then Zero[0]...')
            del self.age
        self.email=email

    def set_properties(self,name,age,email):
        self.name=str(name)
        self.age=int(age)
        if self.age<0:
            print('Age Can Not Be Less Then Zero[0]...')
            del self.age
        self.email=str(email)

    def greet(self):
        print('Hello %s How Are You ?'%self.name,'\nYour Age is %d'%self.age,'\nYour Email Address is %s'%self.email)

"""
obj=user()
obj.set_properties('rahul',-2,'rahul@gmail.com')
"""