from list.worksheet_list import *

print(f"Counting in a loop:"
      f"{check(counting_in_a_loop_course(), counting_in_a_loop_my())}"
      f"Fast method counting:\n"
      f"{fast_method_counting()}\n\n"
      f"Fiding the largest value:"
      f"{check(fiding_the_largest_value_course(), fiding_the_largest_value_my())}"
      f"Fast method largest:\n"
      f"{fast_method_largest()}\n\n"
      f"How to fit the smallest value:"
      f"{check(finding_the_smallest_value_course(), finding_the_smallest_value_my())}"
      f"Fast method smallest:\n"
      f"{fast_method_smallest()}\n\n"
      f"Summing in a loop:"
      f"{check(summing_in_a_loop_course(), summing_in_a_loop_my())}"
      f"Fast method summing:\n"
      f"{fast_method_summing()}\n\n"
      f"Finding the average in a loop:"
      f"{check(finding_the_average_in_a_loop_course(), finding_the_average_in_a_loop_my())}"
      f"Fast method average:\n"
      f"{fast_method_average()}")

friends = ["Joseph", "Glenn", "Sally"]

for friend in friends:
    print("Happy New Year:", friend)
for i in range(len(friends)):
    friend = friends[i]
    print(f"\nHappy New Year: {friend}")
