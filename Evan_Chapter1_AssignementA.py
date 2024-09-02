# Defining the ticket sales function
def sales_of_tickets(total_tickets=20, max_tickets=4):
    # Initialize the buyer_count
    buyer_count = 0
    
    while total_tickets > 0:
        while True:
            try:
                requested_tickets = int(input("How many tickets will you be buying? (MAX=4): "))
                if 1 <= requested_tickets <= max_tickets:
                    break  # Loop will stop if input is valid
                else:
                    print("INVALID. Please enter a number between 1-4. ")
            except ValueError:
                print("INVALID. Please enter a number between 1-4. ")
        
        # If only available tickets can be purchased
        if requested_tickets <= total_tickets:
            total_tickets -= requested_tickets
            buyer_count += 1
            print(f"SUCCESS! Thank you for buying {requested_tickets} ticket(s).")
        else:
            print(f"Sorry...only {total_tickets} ticket(s) are available for purchase.")
    
    # Prints the total number of buyers after the sale has ended
    print(f"SOLD OUT! There were {buyer_count} buyer(s)")

# Call to the function so the ticket sale prompt runs
sales_of_tickets()
