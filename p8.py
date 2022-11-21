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

    @staticmethod
    def sort_aco_ram(obj1,obj2,obj3):
        sorted_list_of_ram=[]
        if obj1.ram<obj2.ram:
            if obj1.ram<obj3.ram:
                sorted_list_of_ram.append(obj1.brand)
                if obj2.ram<obj3.ram:
                    sorted_list_of_ram.append(obj2.brand)
                    sorted_list_of_ram.append(obj3.brand)
                else:
                    sorted_list_of_ram.append(obj3.brand)
                    sorted_list_of_ram.append(obj2.brand)
            else:
                sorted_list_of_ram.append(obj3.brand)
                sorted_list_of_ram.append(obj1.brand)
                sorted_list_of_ram.append(obj2.brand)
        else:
            if obj2.ram<obj3.ram:
                sorted_list_of_ram.append(obj2.brand)
                if obj1.ram<obj3.ram:
                    sorted_list_of_ram.append(obj1.brand)
                    sorted_list_of_ram.append(obj3.brand)
                else:
                    sorted_list_of_ram.append(obj3.brand)
                    sorted_list_of_ram.append(obj1.brand)
            else:
                sorted_list_of_ram.append(obj3.brand)
                sorted_list_of_ram.append(obj2.brand)
                sorted_list_of_ram.append(obj1.brand)
        print(sorted_list_of_ram)


laptop_obj1=laptop('Dell',11 ,"i7 11th Gen","512 GB")
laptop_obj2=laptop('Asus',1,"i7 11th Gen","128 GB")
laptop_obj3=laptop('Lenovo',1,"i9 11th Gen","512 GB")

laptop.sort_aco_ram(laptop_obj1,laptop_obj2,laptop_obj3)