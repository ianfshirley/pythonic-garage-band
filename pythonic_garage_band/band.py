# collection (musicians do not inherit from collection)
# Is a vs. Has a (a guitarist IS a drummer, a band HAS musicians)
class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members or []

    def play_solos(self):
        return [member.play_solo() for member in self.members]


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
    def __init__(self, name):
        super().__init__(name, "guitar", "face melting guitar solo")


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass", "bom bom buh bom")


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums", "rattle boom crash")
