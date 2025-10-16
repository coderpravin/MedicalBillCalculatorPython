import logging
def eleven_percent_discount(total, n=11):
    discount_eleven = (total * n)/100
    final_total = total - discount_eleven
    logging.info("Eleven Percent discount function called success")
    return final_total
