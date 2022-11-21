class laptop:
    
    def __init__(self,brand=None,ram=None,cpu=None,ssd=None) -> None:
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.ssd=ssd

    def showConfing(self):
        print('Brand :',self.brand)
        print('RAM :',self.ram)
        print('CPU :',self.cpu)
        print('SSD :',self.ssd)

"""
laptop_obj1=laptop('Dell',"8 GB","i7 11th Gen","512 GB")
laptop_obj1.showConfing()
"""