class user:

    def set_properties(self,name,age,email):
        self.name=str(name)
        self.age=int(age)
        self.email=str(email)

    def greet(self):
        print('Hello %s How Are You ?'%self.name,'\nYour Age is %d'%self.age,'\nYour Email Address is %s'%self.email)
