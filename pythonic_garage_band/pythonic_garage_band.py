# if __name__ == "__main__":
     


class Band: 
    """
    A class model that will hold different kinds of musicians 
    """
    def __init__(self,name,members =[]):
        self.name = name
        self.members = members
        self.__class__.instances.append(self)

    def play_solos(self):
        play=[]
        for i in self.members:
            play.append(i.play_solos())
            return play

    def to_list():
        return __class__.instances

class Musician:
    """
    The Musician class
    """
    def __init__(self,name,instrument='',solo=''):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    """
    The Guitarist Class 

    """
    def __init__(self,name):
        self.name = name
        self.instrument = 'Guitar'
        self.solo = "Nothing else Matters"

    def __str__(self):
        return f"My name is {self.name} and I play Guitar"

    def __repr__(self):
        return f"instance for Guitarist, name={self.name}"

class Bassist(Musician):
    """
    The Bassist Class
    """
    def __init__(self,name):
        self.name = name
        self.instrument = "bass"
        self.solo = "Comfortably Numb"

    def __str__(self):
        return f"My name is {self.name} & I play bass"

    def __repr__(self):
        return f"instance for Bassist, name={self.name}"

class Drummer(Musician):
        """
        The Drummer Class
        """
        def __init__(self,name):
            self.name = name
            self.instrument = "Drums"
            self.solo = "Kashmir"

        def __str__(self):
            return f"My name is {self.name} & I play drums"

        def __repr__(self):
            return f"instance for Drummer, name={self.name}"
