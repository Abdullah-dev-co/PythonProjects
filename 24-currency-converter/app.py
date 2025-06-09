import requests

def main():
    print("\n Simple Currencey Converter:")
    print("Getting exchange rates....")

    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        rates = response.json()["rates"]
        print("Got rates successfully!") 
    except:
        print("Something went wronge!")
        return
    
    print("\n Popular:USD,EUR,OMR,PKR,JPY,INR")

    while True:
        from_currency = input("From currency code (e.g:USD):").upper()
        if from_currency not in rates:
            print(f"Invalid code:{from_currency}")
            continue
        to_currency = input("To currency code(e.g:EUR):").upper()
        if to_currency not in rates:
            print(f"Invalid code:{to_currency}")
            continue
        try:
            amount = float(input(f"Amount in {from_currency}:"))
        except:
            print("Please enter a valid number")
            continue

        amount_in_usd = amount/rates[from_currency]
        result = amount_in_usd * rates[to_currency]

        print(f"Result: {amount} {from_currency} = {result:.2f}{to_currency}")
        print(f"Rate: 1 {from_currency} = {rates[to_currency]/rates[from_currency]:.4f} {to_currency}")
    
        if not input("\nCovert again?(y/n)").lower().startswith("y"):
            print("Goodbye!")
            break

main()