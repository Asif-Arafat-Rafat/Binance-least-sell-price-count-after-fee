def calculate_break_even(buy_price, buy_fee_doge, sell_fee_usdt_per_doge):
    doge_received = 1 - buy_fee_doge
    total_cost = buy_price + (sell_fee_usdt_per_doge * doge_received)
    break_even_price = total_cost / doge_received
    return round(break_even_price, 5)

def main():
    print("=== Break-even Binance Coin Sell Price Calculator ===")
    print("What coin are you trading?")
    print("1. DogeCoin (Dogecoin)")
    print("2. other coin")
    coin_choice = input("Enter: ")
    if(coin_choice == "1"):
        buy_price = float(input("Enter buying price per DOGE (USDT): "))
        buy_fee = 0.00075
        sell_fee = 0.00017016
    else:    
        buy_price = float(input("Enter buying price per DOGE (USDT): "))
        buy_fee = float(input("Enter buy fee (in DOGE): "))
        sell_fee = float(input("Enter sell fee (in USDT per DOGE): "))

    break_even = calculate_break_even(buy_price, buy_fee, sell_fee)
    print(f"\nTo avoid loss, sell at or above: {break_even} USDT per DOGE")

if __name__ == "__main__":
    main()
