import re


def generate_bill(text):
    # Define a regex pattern for items (quantity, product, unit price)
    pattern = r'(\d+)\s*([a-zA-Z\s]+)\s*(\d+,\d+|\d+)\s*\$'

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # Process matches and calculate total price
    bill = "Product Quantity Unit Price Total Price\n"
    for quantity, product, unit_price in matches:
        # Replace comma with dot for decimal conversion and calculate total
        total_price = float(unit_price.replace(',', '.')) * int(quantity)
        # Format the product name
        product_name = product.strip().title()
        # Add line to bill
        bill += f"{product_name} {quantity} {unit_price} {total_price:.1f}\n"

    return bill


# Use case
text = "I bought three Samsung smartphones 150 $ each, four kilos of fresh banana for 1,2 dollar a kilogram and one Hamburger with 4,5 dollar."
print(generate_bill(text))
