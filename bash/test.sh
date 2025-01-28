#!/bin/bash

# --- Global Variables ---
balance=0

# --- Functions ---

# Function to display the current balance
display_balance() {
    echo "Current balance: £$balance"
}

# Function to deposit funds
deposit() {
    read -p "Enter deposit amount: £" amount
    if [[ "$amount" =~ ^[0-9]+(\.[0-9]+)?$ ]] && (( $(echo "$amount > 0" | bc -l) )); then
      balance=$(awk "BEGIN {printf \"%.2f\", $balance + $amount}")
        echo "Deposited £$amount. New balance: £$balance"
    else
        echo "Invalid deposit amount. Please enter a positive number."
    fi
}

# Function to withdraw funds
withdraw() {
    read -p "Enter withdrawal amount: £" amount
    if [[ "$amount" =~ ^[0-9]+(\.[0-9]+)?$ ]] && (( $(echo "$amount > 0" | bc -l) )); then
        if (( $(echo "$balance >= $amount" | bc -l) )); then
          balance=$(echo "$balance - $amount" | bc -l)
            echo "Withdrew £$amount. New balance: £$balance"
        else
            echo "Insufficient funds. Cannot withdraw this amount."
        fi
     else
      echo "Invalid withdrawal amount. Please enter a positive number."
    fi

}

# Function to display the main menu and get user choice
show_menu() {
    echo ""
    echo "Banking Menu:"
    echo "1. Display Balance"
    echo "2. Deposit Funds"
    echo "3. Withdraw Funds"
    echo "4. Exit"
    read -p "Enter your choice (1-4): " choice
    if [[ "$choice" =~ ^[1-4]$ ]]; then
      return 0
    else
        echo "Invalid choice. Please enter a number between 1 and 4."
        return 1
    fi
}

# --- Main Program Loop ---

while true; do
   show_menu
   if [[ $? -eq 0 ]]; then
     case $choice in
            1) display_balance;;
            2) deposit;;
            3) withdraw;;
            4) echo "Exiting banking system. Goodbye!"; break;;
        esac
    fi

done
