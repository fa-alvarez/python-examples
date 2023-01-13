#!/usr/bin/env python3

def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message

print(lucky_number("Kay"))
print(lucky_number("Cameron"))
