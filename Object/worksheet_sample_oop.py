from List.worksheet_list import check


class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 2
        return self.x


an = PartyAnimal()


def first_x():
    x = 2
    return x


print(check(an.party(), first_x()))


def second_x():
    second = first_x() + first_x()
    return second


print(check(an.party(), second_x()))