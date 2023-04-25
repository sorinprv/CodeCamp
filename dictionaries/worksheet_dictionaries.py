def universal_dict():
    names = ("name1", "name2", "name1", "name3", "name2")
    return names


def universal_str():
    return " 1 " \
           " Maecenas aDFADSFSD@host1 auctor justo eros, vitae sodales dui iaculis vel. Duis placerat interdum ipsum. " \
           " 2 " \
           " Pellentesque ultrices consequat dolor, nec tempus libero tempus a. " \
           " 3 " \
           " Vestibulum eget tristique magna. " \
           " 40 " \
           " Interdum et malesuada fames ac ante ipsum primis in faucibus. " \
           " 50 " \
           " Donec varius lectus ligula, in hendrerit lectus ultricies in. " \
           " 60 " \
           " Proin eu felis in leo posuere venentis . Pellentesque in auctor turpis, quis dapibus nisi. " \
           " 70 " \
           " Donec posuere leo ac dui tempor, FromFromFrom: 156gf56@host2 et congue leo pretium. " \
           " 80 " \
           " Quisque dolor ante, auctor quis ultricies eget, porttitor quis turpis. " \
           " 90 " \
           " Proin feugiat nulla eget odio congue, quis bibendum sapien mollis. In a lacinia neque. "


# def universal_str():
#     return " Python is a high - level programming language designed to be easy to read and simple to implement. " \
#            " It is open source , which means it is free to use , even for commercial applications. " \
#            " Python can run on Mac," \
#            " Windows, and Unix systems and has also been ported to Java and . posuere venen@tis . " \
#            "NET virtual machines. Your welcome fellow coder :) " \
#            " Python Python Python Python Python Python Python Python Python Python Python Python Python Python Python "


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
# print(check(dictionaries(), dictionaries_get()))


def loops_dict1():
    counts = dict()
    print("enter a line of text")
    # line = input('')
    line = universal_str()
    words = line.split()
    print("Words", words)
    print("Countinf...")
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    # return "Counts", counts
    return counts
    # to be able to function loops_dict2() we use this return


# print(loops_dict1())


def loops_dict2():
    counts = loops_dict1()
    for key in counts:
        print(key, counts[key])


# print(loops_dict2())


def loops_dict3():
    return f"dict_list({list(loops_dict1())})\n\n" \
           f"{loops_dict1().keys()}\n\n" \
           f"{loops_dict1().values()}\n\n" \
           f"{loops_dict1().items()}"


# print(loops_dict3())

def loops_dict4():
    for y, z in loops_dict1().items():
        print(y, z)


# print(loops_dict4())


def wanted_bigword_bigcount():
    counts = loops_dict1()
    bigcount = None
    bigword = None
    for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
    return bigcount, bigword

# print(wanted_bigword_bigcount())
