from enum import Enum

class Customer:
    def __init__(self,firstName,lastName,phone,address,gender,customer_ID):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phone = phone
        self.__address = address
        self.__gender = gender
        self.__customer_ID = customer_ID
    def getFirstName(self):
        return self.__firstName

    def setFirstName(self,firstName):
        self.__firstName = firstName

    def getLastName(self):
        return self.__lastName
    
    def setLastName(self,lastName):
        self.__lastName = lastName

    def getPhone(self):
        return self.__phone

    def setPhone(self,phone):
        self.__phone = phone

    def getAddress(self):
        return self.__address

    def setAddress(self,address):
        self.__address = address

    def getGender(self):
        return self.__gender

    def getCustomerID(self):
        return self.__customer_ID

    def setCustomerID(self,customer_ID):
        self.__customer_ID = customer_ID
    
    
class Vehicle:
    def __init__(self,type,color,vehicle_ID,year,country):
        self.__type = type
        self.__color = color
        self.__vehicle_ID = vehicle_ID
        self.__year = year
        self.__country = country

    def getVehicletype(self):
        return self.__type

    def setVehicletype(self,type):
        self.__type = type

    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color

    def getVehicle_ID(self):
        return self.__vehicle_ID

    def setVehicle_ID(self,vehicle_ID):
        self.__vehicle_ID = vehicle_ID

    def getYear(self):
        return self.__year

    def setYear(self,year):
        self.__year = year

    def getCountry(self):
        return self.__country

    def setCountry(self,country):
        self.__country=country
class Level(Enum):
    Beginner=1
    Intermediate=2
    Professional=3
    Expert=4

class Mechanic:
    def __init__(self,firstName,lastName,gender,age,level):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__gender = gender
        self.__age = age
        self.__level = level
    
    def getFirstName(self):
        return self.__firstName

    def setFirstName(self,firstName):
        self.__firstName=firstName

    def getLastName(self):
        return self.__lastName

    def setLastName(self,lastName):
        self.__lastName = lastName

    def getGender(self):
        return self.__gender

    def setGender(self,gender):
        self.__gender = gender

    def getAge(self):
        return self.__age

    def setAge(self,age):
        self.__age = age

    def getLevel(self):
        return self.__level
    
    def setLevel(self,level):
        self.__level = level

class Service_Type(Enum):
    diagnostics=1
    Oil_Replacement =2
    Oil_Filter_Parts =3
    Tire_Replacement=4
    Tire=5
    

class Service:
    def __init__(self,date,service_Type,Quantity,customer_ID,vehicle_ID):
        self.__date = date
        self.__service_Type= service_Type
        self.__Quantity = Quantity
        self.__customer_ID=customer_ID
        self.__vehicel_ID = vehicle_ID

    def getDate(self):
        return self.__date

    def setDate(self,date):
        self.__date = date

    def getServiceType(self):
        return self.__service_Type

    def setServiceType(self,service_Type):
        self.__service_Type = service_Type

    def getQuantity(self):
        return self.__Quantity

    def setQuantity(self,Quantity):
        self.__Quantity = Quantity

    def getCustomerID(self):
        return self.__customer_ID

    def setCustomerID(self,Customer_ID):
        self.__customer_ID = Customer_ID

    def getVehicle_ID(self):
        return self.__vehicle_ID

    def setVehicle_ID(self,vehicle_ID):
        self.__vehicle_ID = vehicle_ID

class Invoice(Customer):
    def __init__(self,Customer_ID,InvoiceDate,InvoiceNumber,Discount,Taxes):
        self.Customer_ID = Customer_ID
        self.__InvoiceDate = InvoiceDate
        self.__InvoiceNumber = InvoiceNumber
        self.__Taxes = Taxes
        self.__Discount = Discount
    
    def getCustomerID(self):
        return self.__customer_ID

    def setCustomerID(self,Customer_ID):
        self.__customer_ID = Customer_ID

    def getInvoiceDate(self):
        return self.__InvoiceDate

    def setInvoiceDate(self,InvoiceDate):
        self.__InvoiceDate = InvoiceDate

    def getInvoiceNumber(self):
        return self.__InvoiceNumber

    def setInvoiceNumber(self,InvoiceNumber):
        self.__InvoiceNumber = InvoiceNumber

    def getDiscount(self):
        return self.__Discount
    def setDiscount(self,Discount):
        self.__Discount = Discount
    
    def getTaxes(self):
        return self.__Taxes

    def setTaxes(self,Taxes):
        self.__Taxes = Taxes
class Gender(Enum):
    Male=1
    Female=2

sohib = Customer('Sohibjon','Avgonov',777777,'Sad City',Gender.Male,14)
car=Vehicle('Mercedes','Black',55555,2017,'Germany')
mechanic = Mechanic('Alex','Max',Gender.Male,36,Level.Expert)
service1 = Service('13March2023',Service_Type.diagnostics,1,sohib.getCustomerID,car.getVehicle_ID)
service2 = Service('13March2023',Service_Type.Oil_Replacement,2,sohib.getCustomerID,car.getVehicle_ID)
service3 = Service('13March2023',Service_Type.Tire,3,sohib.getCustomerID,car.getVehicle_ID)
invoice = Invoice(sohib.getCustomerID,'14March2023',1234,7,3)

        
        

if __name__ == '__main__':
    prices={'diagnostics':15,'Oil_Replacement':120,'Oil_Filter_Parts':35,'Tire_Replacement':50,'Tire':80}
    print("\033[1m"+'Receipt'+"\033[0m")
    print("\033[1m"+'Cell Phone Number:'+"\033[0m", sohib.getPhone())
    print("\033[1m"+'Date:'+"\033[0m", service1.getDate())
    print("\033[1m"+'Adress:'+"\033[0m",sohib.getAddress())
    print("\033[1m"+'Mechanice Name:'+"\033[0m",mechanic.getFirstName(),mechanic.getLastName())
    print("\033[1m"+'Vehicle Type:'+"\033[0m", car.getVehicletype(),'(',car.getYear(),')')
    print("\033[1m"+'Vehicle Color:'+"\033[0m",car.getColor())
    print("\033[1m"+'Vehicle ID:'+"\033[0m",car.getVehicle_ID())
    print()
    print()
    print("\033[1m"+'Services:'+"\033[0m")
    print('No','Service','_______________________','Price')
    print(1,'',service1.getServiceType().name,'___________________', service1.getQuantity()*prices[service1.getServiceType().name])
    print(2,'',service2.getServiceType().name,'_______________', service2.getQuantity()*prices[service2.getServiceType().name])
    print(3,'',service3.getServiceType().name,'__________________________', service3.getQuantity()*prices[service3.getServiceType().name])
    print('____________________________','Taxes',invoice.getTaxes())
    total=prices[service1.getServiceType().name]+prices[service2.getServiceType().name]+prices[service3.getServiceType().name]+invoice.getTaxes()
    print('____________________________','Total',prices[service1.getServiceType().name]+prices[service2.getServiceType().name]+prices[service3.getServiceType().name]+invoice.getTaxes())
    print('_________________________','Discount',invoice.getDiscount())
    print('_____________________',"\033[1m"+'Final Amount'+"\033[0m",total-invoice.getDiscount())


