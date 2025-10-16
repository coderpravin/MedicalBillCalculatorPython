import logging

def ten_percent_discount(total, n=10):
    discount_ten = (total * n)/100
    final_total = total - discount_ten
    logging.info("Ten Percent discount function called success")
    return final_total
    