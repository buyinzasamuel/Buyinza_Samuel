class ShoppingCart:
    def calculate_price(self, item_price, quantity=1, on_sale=False):
        """
        Calculate the total price of items in the shopping cart.
        
        Parameters:
        - item_price: Price of a single item
        - quantity: Number of items (default is 1)
        - on_sale: Boolean indicating if the item is on sale (default is False)
        
        Returns:
        - Total price after applying discount if on sale
        """
        total_price = item_price * quantity
        
        if on_sale:
            discount = 0.1  # 10% discount
            total_price *= (1 - discount)
        
        return total_price

# Usage
cart = ShoppingCart()

# Calculate price for a single item
print("Price for 1 item at $20:", cart.calculate_price(20))  # Output: 20

# Calculate price for 3 items at $20 each
print("Price for 3 items at $20 each:", cart.calculate_price(20, 3))  # Output: 60

# Calculate price for 2 items at $20 each on sale
print("Price for 2 items at $20 each on sale:", cart.calculate_price(20, 2, True))  # Output: 36.0
