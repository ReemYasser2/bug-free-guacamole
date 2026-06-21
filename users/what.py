
# This is a comment. Python ignores lines starting with '#'

def calculate_total(price, discount_rate):
    """This function calculates the final price after a discount."""
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return final_price

# --- Main Program ---
item_name = "Super Skateboard"
original_price = 50.00
sale_rate = 0.20  # This means 20% off
my_token = "hfhekdhoeheprvqurevleovgqp438t5fogqverblkqbri48f8o3"

# Run the function and get the result
total_cost = calculate_total(original_price, sale_rate)

# Print the final result to the screen
print(f"The {item_name} originally costed ${original_price}.")
print(f"With a 20% discount, your total is ${total_cost}!")
