#!/usr/bin/env python3

# Create a Dog class with dog_years based on the Piglet class shown before
# (one human year is about 7 dog years).

class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7

fido = Dog()
fido.years = 3
print(fido.dog_years())
