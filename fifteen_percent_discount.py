import logging

def fifteen_percent_discount(total, n=15):
    discount_fifteen = (total * n)/100
    final_total = total -discount_fifteen
    logging.info("fifteen Percent discount function called success")
    return final_total
