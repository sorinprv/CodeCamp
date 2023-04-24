def check(z, y):
    if z == y:
        return "\nCongratulations, both functions have the same answer!!!\n\n"
    else:
        return "\nSomething is wrong :(\n\n"


def universal_list():
    return [9, 41, 12, 3, 74, 15, 56, 48, 23, 48, 12, 91, 73, 45, 23]


def counting_in_a_loop_course():
    zork = 0
    # print("before", zork)
    for thing in universal_list():
        zork = zork + 1
        # print(zork, thing)
    return "after", zork


# print(counting_in_a_loop_course())


def counting_in_a_loop_my():
    zork = 0
    # print("before", zork)
    while zork < len(universal_list()):
        zork += 1
        # print(zork)
    return "after", zork


# print(counting_in_a_loop_my())
def fast_method_counting():
    return len(universal_list())


def fiding_the_largest_value_course():
    largest_so_far = -1
    # print("before", largest_so_far)
    for the_num in universal_list():
        if the_num > largest_so_far:
            largest_so_far = the_num
        # print(largest_so_far, the_num)
    return "after", largest_so_far


# print(fiding_the_largest_value_course())


def fiding_the_largest_value_my():
    largest_so_far = universal_list()[0]
    # print("before", largest_so_far)
    for i in universal_list():
        if i > largest_so_far:
            largest_so_far = i
        # print(largest_so_far, i)
    return "after", largest_so_far


# print(fiding_the_largest_value_my())
def fast_method_largest():
    return max(universal_list())


def finding_the_smallest_value_course():
    smallest = None
    # print("before", smallest)
    for value in universal_list():
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
        # print(smallest, value)
    return "after", smallest


# print(how_to_fit_the_smallest_value_course())


def finding_the_smallest_value_my():
    smallest = universal_list()[0]
    # print("before", smallest)
    for i in universal_list():
        if i < smallest:
            smallest = i
        # print(smallest, i)
    return "after", smallest


# print(how_to_fit_the_smallest_value_my())

def fast_method_smallest():
    return min(universal_list())


def summing_in_a_loop_course():
    zork = 0
    # print("before", zork)
    for thing in universal_list():
        zork = zork + thing
        # print(zork, thing)
    return "after", zork


# print(summing_in_a_loop_course())


def summing_in_a_loop_my():
    k = universal_list()[0]
    # print("before", k)
    y = 1
    while y != len(universal_list()):
        # print(k, universal_list()[y])
        k = k + universal_list()[y]
        y = y + 1
    return "after", k


# print(summing_in_a_loop_my())

def fast_method_summing():
    return sum(universal_list())


def finding_the_average_in_a_loop_course():
    count = 0
    sum = 0
    # print("before", count, sum)
    for value in universal_list():
        count = count + 1
        sum = sum + value
        # print(count, sum, value)
    return ("after", count, sum, sum / count)


# print(finding_the_average_in_a_loop_course())

def finding_the_average_in_a_loop_my():
    sum = 0
    # print("before", sum)
    for value in universal_list():
        sum = sum + value
    return ("after", 15, sum, sum / len(universal_list()))


# print(finding_the_average_in_a_loop_my())

def fast_method_average():
    return sum(universal_list()) / len(universal_list())


# print(fast_method_average())


# print(f"Counting in a loop:"
#       f"{check(counting_in_a_loop_course(), counting_in_a_loop_my())}"
#       f"Fast method counting:\n"
#       f"{fast_method_counting()}\n\n"
#       f"Fiding the largest value:"
#       f"{check(fiding_the_largest_value_course(), fiding_the_largest_value_my())}"
#       f"Fast method largest:\n"
#       f"{fast_method_largest()}\n\n"
#       f"How to fit the smallest value:"
#       f"{check(finding_the_smallest_value_course(), finding_the_smallest_value_my())}"
#       f"Fast method smallest:\n"
#       f"{fast_method_smallest()}\n\n"
#       f"Summing in a loop:"
#       f"{check(summing_in_a_loop_course(), summing_in_a_loop_my())}"
#       f"Fast method summing:\n"
#       f"{fast_method_summing()}\n\n"
#       f"Finding the average in a loop:"
#       f"{check(finding_the_average_in_a_loop_course(), finding_the_average_in_a_loop_my())}"
#       f"Fast method average:\n"
#       f"{fast_method_average()}")