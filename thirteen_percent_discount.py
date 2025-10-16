import logging
  
def thirteen_percent_discount(total, n=13):
    discount_thirteen = (total * n)/100
    final_total = total -discount_thirteen
    logging.info("Thirteen Percent discount function called success")
    return final_total
