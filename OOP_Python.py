def pizza (size,*digerleri,**süre):
    print(f"{size} boy pizzayi tercih ettiniz. Pizza'nin icerigi şunlar:")
    for diger in digerleri:
        print(f"-{diger}")
    print("Siparisiniz hakkinda detaylar:")
    for key,value in süre.items():
        print(f"-{key}:{value}")
# İlk seçeneğimiz size'dı diğerlerini istediğimiz kadar kullanabilirdik.
#! pizza("Büyük","Pepperoni","Kasarli", Yolda="Evet" , Ortalama="5 dakika" )
"""  Çiktisi==>
Büyük boy pizzayi tercih ettiniz. Pizza'nin icerigi şunlar:
-Pepperoni
-Kasarli
Siparisiniz hakkinda detaylar:
-Yolda:Evet
-Ortalama:5 dakika
"""        

class Person: # person=kişi
    def __init__(self,isim,yas,boy,kilo):
        self.isim=isim
        self.yas=yas
        self.boy=boy
        self.kilo=kilo
        print("Init calisti...")
# İkiside çalıştı. Out olarak 2 kere init çalıştı denildi.
#! p1=Person("Yagmur",20,175,66)
#! p1=Person(isim="Yagmur",kilo=66,boy=175,yas=20) # Yukarıdaki ile aynı yerleri farklı isim belirterek objeyi doldurduk.
#! p2=Person("Mehmet",19,180,90)
#P1 ve P2 nin bilgilerini bastırabiliriz.
#! print(f"{p1.isim}'un yasi:{p1.yas} boyu:{p1.boy} kilosu:{p1.kilo}")
#! print(f"{p2.isim}'in yasi:{p2.yas} boyu:{p2.boy} kilosu:{p2.kilo}")


class Person_1:
    # Class attributes
    name="Hamza"
    address="No Information" # Address'i Person_1.address şeklinde çağırabilirim.
    # Constructor
    def __init__(self,name):
        # Object attributes
        self.name=name
# Update yapmak istersek:
Person_1.name="Ahmet"
#! print(f"{Person_1.name}'in adres girisi==> {Person_1.address}.")


class Person_2:
    def __init__(self,name):
        self.name=name 
        
Person_2.name="Süm"
#! print(f"{Person_2.name}'dür...") ==> ikisinin classı farklı olduğu için isim karışıklığı meydana gelmez...


#! METHODS!!!
class Mine:
    # Class object attributes
    def __init__(self,name="Hamza",age=21,size=180): # Bunlar default değerlerdir.
        self.name=name
        self.age=age
        self.size=size
    # instance methods. 
    def intro(self): # self'i doldurmasak da self yazımı zorunludur.
        print("Hello There I am " + Mine.name) # Class'tan methods'a geçtik.
    def calculateAgeYear(self):
        return 2023 - self.age # Doğduğu yılı verir.
m1=Mine(name="Yagmur",age=20,size=170)
m2=Mine(name="Azra",age=19,size=167)

#! m1.calculateAgeYear() # return olarak döndürüldüğü için print ile yazılmalı 
#! print(f"Dogudugum yil=> {Mine.calculateAgeYear}") # Mine m1'in örneğidir. Biz örneği çağırabiliriz.
#! print(f"{m1.name}'in yasi:{m1.age} boyu:{m1.size} dogdugu yil:{m1.calculateAgeYear()}") gayet doğru çalıştı.
#! print(f"{m2.name}'in yasi:{m2.age} boyu:{m2.size} dogdugu yil:{m2.calculateAgeYear()}") gayet doğru çalıştı.

class Circle: # Dairenin alanını ve çevresini hesaplayan bir class oluşturdum.
    # Class object attribute
    pi=3
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    def alan(self):
        return self.pi * (self.yaricap ** 2)
    def cevre(self):
        return 2 * self.pi * self.yaricap # methods doldurulurken self. yazılır unutma.   
cember_1=Circle(yaricap=5)
cember_2=Circle(yaricap=10)
#! print(f"1. Cemberin alani:{cember_1.alan()} cevresi:{cember_1.cevre()}")
#! print(f"2. Cemberin alani:{cember_2.alan()} cevresi:{cember_2.cevre()}")

# Inheritance == Kalıtım... ==> Miras almak gibi düşünelim...

""" 
Mesela Person==>name,lastname,age,eat(),run()
Person'un içindekileri tek tek yazmak yerine Student(Person),Teacher(Person) şekilinde miras birakicaz...
"""
class Person_3():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        # print("Person Created")
    def who_am_i(self):
        print("I am Person_3") # Student normalde who_am_i'a sahip değil fakat dolaylı olarak içine alır.
    def bakkal(self):
        print("Bakkala gidiyorum.")
class Student(Person_3): # Person class'ın 
    def __init__(self,fname,lname):
        Person_3.__init__(self,fname,lname)
        print("Student Created")

p1=Person_3(fname="Yilmaz",lname="Kaan") # Sadece Person Created çalışır.
s1=Student(fname="Yagmur",lname="Dere") # Person Created Student Created ikiside çalışır.
#! print(f"Person_3'ün first name:{p1.firstName}") # Printin içinde kullanırken self,x şekildekindeki x'i kullan...
#! print(f"Person_3'ün last name:{p1.lastName}")
#! print(f"Student'in firs name:{s1.firstName} last name:{s1.lastName}")
p1.bakkal()
#p1.who_am_i()
#s1.who_am_i()