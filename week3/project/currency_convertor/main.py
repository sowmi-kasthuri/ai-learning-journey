from exchangerate import get_exchange_rate, log_to_csv

base = input("Enter base currency (e.g., USD): ")
target = input("Enter target currency (e.g., INR): ")

rate = get_exchange_rate(base, target)

if rate:
    print(f"1 {base.upper()} = {rate} {target.upper()}")
    log_to_csv(base.upper(), target.upper(), rate)
    print("✅ Logged to exchange_log.csv")
else:
    print("❌ Could not fetch the exchange rate.")
