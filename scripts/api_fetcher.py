import requests
import json
import sys
# DeliveryOrder class to model each order as an object
class DeliveryOrder:
    def __init__(self, order_id, restaurant_name, amount, is_delivered):
        self.order_id = order_id
        self.restaurant_name = restaurant_name
        self.amount = amount
        self.is_delivered = is_delivered

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "restaurant_name": self.restaurant_name,
            "amount": self.amount,
            "is_delivered": self.is_delivered
        }
    
    # Create 4 DeliveryOrder objects
order1 = DeliveryOrder(101, "Spice Garden", 250.00, True)
order2 = DeliveryOrder(102, "Burger Hub", 180.50, False)
order3 = DeliveryOrder(103, "Curry House", 620.00, True)
order4 = DeliveryOrder(104, "Pizza Point", 340.75, False)

orders = [order1, order2, order3, order4]


# Print formatted summary for each order
print("=" * 50)
print("DELIVERY ORDERS SUMMARY")
print("=" * 50)
for order in orders:
    status = "Delivered" if order.is_delivered else "Pending"
    print(f"Order #{order.order_id} | {order.restaurant_name} | Rs {order.amount:.2f} | {status}")

# Fetch mock restaurant data from API
api_url = "https://jsonplaceholder.typicode.com/posts?_limit=5"
response = requests.get(api_url)

if response.status_code == 200:
    top_restaurants = response.json()
else:
    print(f"Error: API request failed with status code {response.status_code}")
    sys.exit(1)    

# Save orders_summary.json - serialized DeliveryOrder objects
with open("../data/processed/orders_summary.json", "w") as f:
    json.dump([order.to_dict() for order in orders], f, indent=2)

print("\nSaved orders_summary.json successfully.")

# Save top_restaurants.json - the 5 API records
with open("../data/processed/top_restaurants.json", "w") as f:
    json.dump(top_restaurants, f, indent=2)

print("Saved top_restaurants.json successfully.")
