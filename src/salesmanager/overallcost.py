"""
Calculate the overall cost of items
"""
from salesmanager.models import Item

def get_overall_cost():
    """Function to calculate to overall cost of an item """
    items = Item.objects.all()
    total_cost = 0 #total cost of an item
    for item in items:
        total_cost += item.price
    return total_cost

def get_overall_benefit():
    """Calcualte the overall benefit from the sold item """
    items = Item.objects.filter(status="sold")
    overall_benefit = 0 #overall benefit
    overall_benefit_in_perctange = 0
    for item in items:
        overall_purchase_cost_of_sold_item += item.price
        overall_sold_cost_of_sold_item += item.selling_price
        overall_benefit += item.price - item.selling_price
        overall_benefit_in_perctange = (overall_benefit /item.price) * 100

    return overall_benefit, overall_benefit_in_perctange

def get_overall_sales():
    """Calculate the overall sales from the sold item """
    items = Item.objects.filter(status="sold")
    overall_sales = 0 #overall sales price of an item
    for item in items:
        overall_sales += item.selling_price
    return overall_sales
