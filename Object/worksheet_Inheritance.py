from Object.worksheet_object_lifecycle import PartyAnimal3


class FootballFan(PartyAnimal3):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)


s = PartyAnimal3('Sally')
s.party()
j = FootballFan('Kim')
j.party()
j.touchdown()
