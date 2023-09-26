import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print("Please enter a number.")
            
    return amount        

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1-{MAX_LINES }")
        else:
            print("Please enter a number.")
                
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet (Minimum of " + str(MIN_BET) + " and Maximum of " + str(MAX_BET) + ")")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a number between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number.")
    return amount
        
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is ${balance}")
        else:
            if lines == 1:
                print(f"Your are betting ${bet} on {lines} line. Total bet is equal to ${total_bet}")
            else:
                print(f"Your are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
            break
                
            
   

    
    
    
main()