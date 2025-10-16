import logging

def fourteen_percent_discount(total, n=14):
    discount_fourteen = (total * n)/100
    final_total = total -discount_fourteen
    logging.info("fourteen Percent discount function called success")
    return final_total
