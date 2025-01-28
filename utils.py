import math
from models import Receipt

#function to calculate points
def calculate_points(receipt: Receipt) -> int:
    points = 0

    # 1 point per alphanumeric character
    points += sum(c.isalnum() for c in receipt.retailer)

    #  50 points if it's a round number, 25 if divisible by 0.25
    total = float(receipt.total)
    if total.is_integer():  
        points += 50
    elif total % 0.25 == 0:  # checking if  Divisible by 0.25
        points += 25

    #  5 points for every 2 items
    points += (len(receipt.items) // 2) * 5

    #  0.2 points per character in shortDescription
    for item in receipt.items:
        description = item.shortDescription.strip() 
        points += math.ceil(len(description) * 0.2)

    #  6 points if the day is odd
    day = int(receipt.purchaseDate.split("-")[-1])
    if day % 2 == 1:
        points += 6

    # 10 points if between 14:00 and 16:00
    hour = int(receipt.purchaseTime.split(":")[0])
    if 14 <= hour < 16:
        points += 10

    return points
