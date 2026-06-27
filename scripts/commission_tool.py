# Step 1: Commission calculation function
def calculate_commission(amount):
    if amount <= 200:
        return amount * 0.10
    elif amount <= 500:
        return amount * 0.15
    else:
        return amount * 0.20
    
# Step 2: List of order amounts spanning all 3 tiers
order_amounts = [150, 180, 250, 320, 450, 600, 750, 900]

# Step 3: Apply calculate_commission to all orders using map() + lambda
commissions = list(map(lambda amount: calculate_commission(amount), order_amounts))

# Step 4: Filter orders where commission exceeds Rs 60
high_value_orders = list(filter(lambda amount: calculate_commission(amount) > 60, order_amounts))

# Step 5: Print Block 1 - Table of amounts and commissions
print("=" * 40)
print("BLOCK 1: Order Amount vs Commission")
print("=" * 40)
for amount, commission in zip(order_amounts, commissions):
    print(f"Order Amount: Rs {amount:.2f}  |  Commission: Rs {commission:.2f}")

# Step 6: Print Block 2 - Total payout
total_payout = sum(commissions)
print()
print("=" * 40)
print("BLOCK 2: Total Payout")
print("=" * 40)
print(f"Total Payout: Rs {total_payout:.2f}")

# Step 7: Print Block 3 - High value orders list with count
print()
print("=" * 40)
print("BLOCK 3: High Value Orders (Commission > Rs 60)")
print("=" * 40)
print(f"High Value Orders: {high_value_orders}")
print(f"Count: {len(high_value_orders)}")

