# Utility file for fucntions used across multiple files
import datetime
userCart = []

class Product:
	#Product class to represent an item in the cart
	def __init__(self, name: str, price: float, discount: float = 0.0):
		self.name = name
		self.usualPrice = price
		#default discount is 0.0, percentage
		self.discount = discount

		self.applySeasonalDiscounts()
		self.discountedPrice = (self.usualPrice * (1-(self.discount/100)))

	def __str__(self):
		return self.name


	def applySeasonalDiscounts(self):
		discountDates = [
			#new years, 20% discount
			[datetime.date(datetime.datetime.now().year, 1, 1), 20.0],

			#christmas, 25% discount
			[datetime.date(datetime.datetime.now().year, 12, 25), 25],
		]
		
		today = datetime.datetime.now().date()
		for day in discountDates:
			#for every day in the discounteed dates, apply the discount if today is a seasonal date
			if (today == day[0]):
				self.discount += day[1]
				break

def generateReceipt():
	#receipt is in the form {
	# "name": [discountedPrice, discount, usualPrice]
	#}
	res = {}
	for i in userCart:
		res[i.name] = [i.discountedPrice, i.discount, i.usualPrice]
	return res
	