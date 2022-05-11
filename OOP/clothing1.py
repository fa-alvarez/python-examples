#!/usr/bin/env python3

# Below we have a base class called Clothing.  A second class, called Shirt, 
# inherits methods from the Clothing class.

class Clothing:
  material = ""
  def __init__(self, name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name, self.material))

class Shirt(Clothing):
  material = "Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
