from list.work import check


def universal_dict():
    names = ("name1", "name2", "name1", "name3", "name2")
    return names


def dictionaries():
    counts = dict()
    for name in universal_dict():
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
    return counts


# print(dictionaries())


def dictionaries_get():
    counts = dict()
    for name in universal_dict():
        counts[name] = counts.get(name, 0) + 1
    return counts


# print(dictionaries_get())
print(check(dictionaries(), dictionaries_get()))
