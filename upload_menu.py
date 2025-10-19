import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDJzwwY_71Y9wZhxDiB3qEoZJdZpEi4O0s",
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

menu_data = {
    "flavours": {
        "original": {"available": True},
        "mint": {"available": True},
        "strawberry": {"available": True},
        "dark_chocolate": {"available": True},
        "mango_swirl": {"available": True},
        "matcha": {"available": True},
        "acai": {"available": True}
    },
    "toppings": {
        "almond": {"available": True},
        "sprinkles": {"available": True},
        "mango": {"available": True},
        "strawberry": {"available": True},
        "kiwi": {"available": True},
        "watermelon": {"available": True},
        "honeydew": {"available": True},
        "banana": {"available": True},
        "oreo": {"available": True},
        "biscoff": {"available": True},
        "mochi": {"available": True},
        "fruit_pebbles": {"available": True}
    },
    "sauces": {
        "biscoff": {"available": True},
        "dark_chocolate": {"available": True},
        "white_choc": {"available": True},
        "pistachio": {"available": True},
        "strawberry": {"available": True},
        "peanut_butter": {"available": True},
        "salted_caramel": {"available": True}
    },
    "sizes": {
        "small": {
            "price": 6.0,
            "toppings_included": 2,
            "sauces_included": 1,
            "promotion": None
        },
        "medium": {
            "price": 7.5,
            "toppings_included": 3,
            "sauces_included": 1,
            "promotion": None
        },
        "large": {
            "price": 9.0,
            "toppings_included": 3,
            "sauces_included": 2,
            "promotion": "Free extra topping or 10% off next purchase"
        }
    }
}

db.child("menu").set(menu_data)
print("Menu uploaded successfully!")
