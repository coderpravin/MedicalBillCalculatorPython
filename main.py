import re
import logging
from ten_percent_discount import ten_percent_discount
from eleven_percent_discount import eleven_percent_discount
from twelve_percent_discount import twelve_percent_discount
from thirteen_percent_discount import thirteen_percent_discount
from fourteen_percent_discount import fourteen_percent_discount
from fifteen_percent_discount import fifteen_percent_discount

print("Welcome Medical Discount System")

#logging setup
logging.basicConfig(filename="result.log", level=logging.INFO, format="%(asctime)s -- %(levelname)s -- %(message)s")

while True:
    name = input("Please enter your name :")
    
    if re.match(r"^[A-Za-z]+$", name):
        logging.info(f"The name is correct {name}")
        print("Name Accepted")
        break
        
    else:
        print("Invalid name Only Letter are allowed")
        logging.error(f"The name is not letter")
        
    
def discount_Bill(name):
        
    total = 0
    while True:
        try:
            amount = float(input("Enter Your Bill Amount :"))
        except ValueError:
            logging.warning("The amount it should b float you enter wrong amount")
            print("You are put wrong value ")
            continue
            
        total += amount
        
        choice = input("Do you want to add another bill (y/n) :").lower()
        
        if choice != "y":
            break
        
        
    # print(f"The total amount is {total :.2f}")  
    print("="*60)
    print(f"Hi {name} Your Final Total is : {total :.2f}")  
    return total
    

    
#total_amount = discount_Bill(name)


while True:
    print("Here choose how much percente discount you want :")
    
    print("Press 1 for 10% Discount :(1)")
    print("Press 2 for 11% Discount :(2)")
    print("Press 3 for 12% Discount :(3)")
    print("Press 4 for 13% Discount :(4)")
    print("Press 5 for 14% Discount :(5)")
    print("Press 6 for 15% Discount :(6)")
    print("Press 7 for exit")
    
    choice = int(input("Enter your choice between : (1-6 ):"))
    
    if choice == 1:       
        total_10 = discount_Bill(name)
        after_10_final_total = ten_percent_discount(total_10)
        print(f"After Ten Percentage Discount Your Paid to {after_10_final_total:.2f}Rs")
        print("="*60)
        

    elif choice == 2:
        total_11 = discount_Bill(name)
        after_11_final_total = eleven_percent_discount(total_11)

        print(f"After Eleven Percentage Discount Your Paid to {after_11_final_total:.2f}Rs")
        print("="*60)

    elif choice == 3:    
        total_12 = discount_Bill(name)
        after_12_final_total = twelve_percent_discount(total_12)
        print(f"After Twelve Percentage Discount Your Paid to {after_12_final_total:.2f}Rs")
        print("="*60)

    elif choice == 4:
        total_13 = discount_Bill(name)
        after_13_final_total = thirteen_percent_discount(total_13)
        print(f"After Thirteen Percentage Discount Your Paid to {after_13_final_total:.2f}Rs")
        print("="*60)
        
    elif choice == 5:
        total_14 = discount_Bill(name)
        after_14_final_total = fourteen_percent_discount(total_14)
        print(f"After fourteen Percentage Discount Your Paid to {after_14_final_total:.2f}Rs")
        print("="*60)
        
    elif choice == 6:
        total_15 = discount_Bill(name)
        after_15_final_total = fifteen_percent_discount(total_15)
        print(f"After fifteen Percentage Discount Your Paid to {after_15_final_total:.2f}Rs")
        print("="*60)

    elif choice == 7:
        print("Exiting... Thank you for using the Medical Discount System!")
        break
    
    else:
        print("Wrong Input")
        
if __name__ == "__main__":
    pass
        
        
        
