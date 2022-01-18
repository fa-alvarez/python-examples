#!/usr/bin/env python3

def add_prices(basket):
	"""The add_prices function returns the total price of all of the groceries in
	the  dictionary."""

	total = 0
	for product, prices in basket.items():
		total += prices
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(help(add_prices))
print(add_prices(groceries)) # Should print 28.44
