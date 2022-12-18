from string import ascii_letters
class Dessert:
    
    def __init__(self,name='Some Dessert',calories=300,flavor="delicious"):
        self.name = name
        self.calories = calories
        self.flavor = flavor
    

    def _check_name(cls,name):
        sname = name.split()
        let = ascii_letters + "-"
        if(type(name) != str):
            raise TypeError("name not str")
        for s in sname:
            if(len(s) < 1):
                raise TypeError("No name")
            if len(s.strip(let)) != 0:
                raise TypeError("Name must have a only letters")


    def _check_calories(cls,calories):
        if(0 > calories or calories >= 10000):
            raise TypeError("Wrong calorie!")
            
    def is_healthy(self):
        if(self.__calories < 200):
            return True
        else:
            return False

    
    def is_delicious(self):
        if(self.flavor == "black licorice"):
            return False
        return True

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self._check_name(name)
        self.__name = name

    @property
    def calories(self):
        return self.__calories
    @calories.setter
    def calories(self,calories):
        self._check_calories(calories)
        self.__calories = calories

    class JellyBean:
        
        def _check_flavor(self,flavor):
            if type(flavor)!= str:
                raise TypeError("Flavor must be str")
            
        @property
        def flavor(self):
            return self.__flavor
        @flavor.setter
        def flavor(self,flavor):
            self._check_flavor(flavor)
            self.__flavor = flavor

d1 = Dessert()
Chc = Dessert("Chery cake",999)
Cho = Dessert("Chocolate", 200)
Mis = Dessert("Mis", 100,"black licorice")
Mis.name = "Miska"
Mis.calories = 0
print(Chc.name,Chc.calories,Chc.flavor,Chc.is_delicious(),Chc.is_healthy())
print(Cho.name,Cho.calories,Cho.flavor,Cho.is_delicious(),Cho.is_healthy())
print(Mis.name,Mis.calories,Mis.flavor,Mis.is_delicious(),Mis.is_healthy())
print(d1.name,d1.calories,d1.flavor,d1.is_delicious(),d1.is_healthy())


