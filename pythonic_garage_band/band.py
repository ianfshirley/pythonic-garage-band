# collection (musicians do not inherit from collection)
# Is a vs. Has a (a guitarist IS a drummer, a band HAS musicians)
class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members or []

    def __str__(self):
        pass

    def __repr__(self):
        pass


# base class/super class
class Musician:
    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return self.name


# derived class/subclass
class Guitarist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return self.name


class Bassist(Musician):
    pass


class Drummer(Musician):
    pass