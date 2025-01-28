import pytest
from utils import calculate_points
from models import Receipt, Item

def test_calculate_points():
    """Test points calculation based on receipt rules."""
    receipt = Receipt(
        retailer="Target",
        purchaseDate="2023-01-01",
        purchaseTime="15:30",
        total="35.25",
        items=[
            Item(shortDescription="Pepsi", price="1.25"),
            Item(shortDescription="Lays", price="3.00")
        ]
    )

    points = calculate_points(receipt)
#according to calculations:
    assert points == 54  
