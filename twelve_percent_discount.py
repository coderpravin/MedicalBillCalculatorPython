import logging
def twelve_percent_discount(total, n=12):
    discount_twelve = (total * n)/100
    final_total = total -discount_twelve
    logging.info("Twelve Percent discount function called success")
    return final_total
