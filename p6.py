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

    @staticmethod
    def youngest(obj1,obj2,obj3):
        if obj1.age<obj2.age:
            if obj1.age<obj3.age:
                print('%s is The Youngest One...'%obj1.name)
            else:
                print('%s is The Youngest One...'%obj3.name)
        else:
            if obj2.age<obj3.age:
                print('%s is The Youngest One...'%obj2.name)
            else:
                print('%s is The Youngest One...'%obj3.name)


"""
user_obj1=user('Rahul Bhutaiya',20,'rahulbhutaiya@gmail.com')
user_obj2=user('Jenil Monapara',5,'jenilmonapara@gmail.com')
user_obj3=user('Utsav Bhutaiya',10,'utsav@gmail.com')

user.youngest(user_obj1,user_obj2,user_obj3)
"""