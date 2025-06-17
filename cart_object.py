"""

This is a problem that I am creating
cart = {
    "10": {
        "M": "2",
        "L": "1"
    },
    "25": {
        "S": "3"
    },
}

Lets say you have a cart object, and your cart is currently displaying 
{1: 1} on the checkout screen when it is supposed to display 1

Return just 1 instead of {1: 1}

"""

cart = {
    "10": {
        "M": "2",
        "L": "1"
    },
    "25": {
        "S": "3"
    },
}

for key, value in cart.items():
    print(value)