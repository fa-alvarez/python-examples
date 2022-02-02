#!/usr/bin/env python3

def combine_lists(list1, list2):
    """This function combines the contents of Drew's list, followed by
    Jamie's list in reverse order, to get an accurate list of the students
    as they arrived."""

  list1.reverse()
  list2.extend(list1)
  return(list2)

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
