import math

def calculate_emi(p, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    if monthly_rate == 0:
        emi = p / months
    else:
        emi = (p * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return emi, months

def print_schedule(p, annual_rate, years, emi, months):
    monthly_rate = annual_rate / (12 * 100)
    balance = p
    print("\n" + "="*75)
    print(f"{'Month':<6} {'EMI':<12} {'Interest':<12} {'Principal':<12} {'Balance':<15}")
    print("="*75)
    for m in range(1, months + 1):
        interest = balance * monthly_rate
        principal = emi - interest
        balance -= principal
        if balance < 0: balance = 0
        print(f"{m:<6} {emi:<12.2f} {interest:<12.2f} {principal:<12.2f} {balance:<15.2f}")
        if m == 12:  # Sirf 1 saal ka schedule dikhayenge warna lambi ho jayegi
            print("... Table continues ...\n")
            break

def main():
    print("="*40)
    print("     PROFESSIONAL LOAN EMI CALCULATOR")
    print("="*40)
    
    while True:
        try:
            p = float(input("Enter Loan Amount Rs: "))
            if p <= 0: raise ValueError
            break
        except: print("Invalid! Positive number daalo.")
    
    while True:
        try:
            annual_rate = float(input("Enter Annual Interest Rate %: "))
            if annual_rate < 0: raise ValueError
            break
        except: print("Invalid! 0 ya us se zyada number daalo.")
    
    while True:
        try:
            years = float(input("Enter Loan Tenure in Years: "))
            if years <= 0: raise ValueError
            break
        except: print("Invalid! Positive number daalo.")

    emi, months = calculate_emi(p, annual_rate, years)
    total_payment = emi * months
    total_interest = total_payment - p

    print("\n" + "="*40)
    print(f"Monthly EMI:        Rs {emi:,.2f}")
    print(f"Total Months:       {int(months)}")
    print(f"Total Payment:      Rs {total_payment:,.2f}")
    print(f"Total Interest:     Rs {total_interest:,.2f}")
    print(f"Interest % of Loan: {(total_interest/p)*100:.2f}%")
    print("="*40)
    
    show = input("\nAmortization Schedule dekhni hai? y/n: ").lower()
    if show == 'y':
        print_schedule(p, annual_rate, years, emi, months)

if __name__ == "__main__":
    main()