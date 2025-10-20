# Utility file for fucntions used across multiple files
import pyrebase
import datetime
userCart = []

#Logger
def log(msg: str):
	print(f"LOG ({datetime.datetime.now()}): {msg}")

###DATABASE CODE
#initialise and get menu
firebaseConfig = {
    "apiKey": "CHECK TELEGRAM GROUP",
    "authDomain": "ctdsoftserve.firebaseapp.com",
    "databaseURL": "https://ctdsoftserve-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "ctdsoftserve",
    "storageBucket": "ctdsoftserve.firebasestorage.app",
    "messagingSenderId": "903789925629",
    "appId": "1:903789925629:web:4f7351495dea0f8897da94",
    "measurementId": "G-BXPJNNS26B"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def getMenu():
	menu = db.child("menu").get().val()
	log("Menu retrieved successfully.")
	return menu

def postOrderToDB(selected_size, selected_flavour, selected_toppings, selected_sauces):
	log(f"postOrderToDB called, payload: {order_data}")
	order_data = {
        "size": selected_size,
        "flavour": selected_flavour,
        "toppings": selected_toppings,
        "sauces": selected_sauces
    }
	db.child("orders").push(order_data)
	log(f"{order_data} posted to DB")



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
	

