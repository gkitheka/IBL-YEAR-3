def main():
    # Track the amount of money inserted by the user (in cents)
    amount_inserted = 0
    
    # Prompt the user to insert coins until the amount due is reached
    while amount_inserted < 50:
        coin = input("Insert a coin (5, 10, or 25 cents): ")
        if coin == "5":
            amount_inserted += 5
        elif coin == "10":
            amount_inserted += 10
        elif coin == "25":
            amount_inserted += 25
        
        # Compute and display the remaining amount due
        cents_due = 50 - amount_inserted
        if cents_due > 0:
            print(f"{cents_due} cents due.")
    
    # Compute and display the amount of change owed to the user
    change = amount_inserted - 50
    if change > 0:
        print(f"Here's your {change} cents in change.")


if __name__ == "__main__":
    main()
