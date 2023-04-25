import re

from dictionaries.worksheet_dictionaries import universal_str


def matching_str1():
    lst = re.findall('\\S+na\\S+', universal_str())
    return lst


def matching_str2():
    y = re.findall('[MPQZY]+', universal_str())
    return y


def matching_str3():
    y = re.findall('[P].+', universal_str())
    return y


def matching_str4():
    y = re.findall('[P].+?', universal_str())
    return y


def matching_str5():
    y = re.findall('\S+@\S+', universal_str())
    return y


def matching_str6():
    y = re.findall('Maecenas (\S+@\S+)', universal_str())
    return y


def matching_number():
    y = re.findall('[0-5]+', universal_str())
    return y


def duble_split():
    words = universal_str().split()
    email = words[2]
    pieces = email.split('@')
    return pieces[1]


def regex1():
    y = re.findall('@([^ ]*)', universal_str())
    return y


def regex2():
    y = re.findall('From .*@([^ ]*)', universal_str())
    return y

# print(f"{matching_str1()}\n"
#       f"{matching_str2()}\n"
#       f"{matching_str3()}\n"
#       f"{matching_str4()}\n"
#       f"{matching_str5()}\n"
#       f"{matching_str6()}\n"
#       f"{matching_number()}\n"
#       f"{duble_split()}\n"
#       f"{regex1()}\n"
#       f"{regex2()}\n")
