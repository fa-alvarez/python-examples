#!/usr/bin/env python3

# Given a list of filenames, this code renames all the files with extension hpp
# to the extension h.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for filename in filenames:
    if filename.split(".")[-1] == "hpp":
        newfilenames.append("".join(filename.split(".")[:-1]) + ".h")
    else:
        newfilenames.append(filename)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
