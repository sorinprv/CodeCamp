from Dictionaries.worksheet_dictionaries import universal_str


def universal_dict():
    counts = dict()
    line = universal_str()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


# print(universal_dict())


def tuple_dict():
    d = dict()
    d["asd"] = 2
    d["qwe"] = 4
    for (k, v) in d.items():
        print(k, v, type((k, v)))
    tups = d.items()
    return tups


# print(tuple_dict())

def using_sorted_key():
    d = universal_dict()
    t = d.items()
    t = sorted(t)
    # print(t)
    for k, v in t:
        print(k, v)


# print(using_sorted_key())
def using_sorted():
    list = []
    for k, v in universal_dict().items():
        list.append((v, k))
    # print(List)
    list = sorted(list, reverse=True)
    return list


# print(using_sorted())


def top_ten_words():
    list = []
    for k, v in universal_dict().items():
        newtup = (v, k)
        list.append(newtup)
    list = sorted(list, reverse=True)
    for v, k in list[:10]:
        print(k, v)


# print(top_ten_words())


def tuple_dict_short():
    return sorted([(v, k) for k, v in universal_dict().items()], reverse=True)


print(tuple_dict_short())
