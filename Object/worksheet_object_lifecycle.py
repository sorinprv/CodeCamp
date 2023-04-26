class PartyAnimal1:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


q = PartyAnimal1('Quincy')
m = PartyAnimal1('Miya')


# q.party()
# m.party()
# q.party()
class PartyAnimal2:
    x = 0

    def __int__(self): print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)


# an = PartyAnimal2()
# an.party()
# an.party()
# an = 42  # this row activates def del :D
# # print('an contains', an)

class PartyAnimal3:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


s = PartyAnimal3('Sally')
"""Sally constructed"""
s.party()
"""Sally party count 1"""
j = PartyAnimal3('Jim')
"""Jim constructed"""
j.party()
"""Jim party count 1"""
s.party()
"""Sally party count 2"""
