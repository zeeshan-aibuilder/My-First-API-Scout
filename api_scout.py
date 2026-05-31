import os
import requests
import datetime
import time
import csv

def clear_screen():
    
    if os.name == "nt":      
        os.system("cls")   
        
    else:
        os.system("clear")    


def setup_environment():
    if not os.path.exists("scout_data"):
        os.makedirs("scout_data")
        print("[+] scout_data directory created successfully.")

    else:
        os.path.abspath("scout_data")
        print("[i] scout_data directory already exists.")

def fetch_crypto_data(coin , currency):

    coin = coin.lower().strip()
    currency = currency.lower().strip()

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

    print(f"\n[i] Fetching live data for {coin.capitalize()} in {currency.upper()}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        if coin in data:
            return data[coin][currency]
        
        else:
            print("[-] Error: Coin not found. Check spelling.")
            return None
        
    else:
        print("API Connection ERROR!")
        return None



def save_to_csv(coin, currency, price):
    file_path = "scout_data/market_data.csv"
    
    file_exists = os.path.exists(file_path)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, mode="a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        
        if not file_exists:
            writer.writerow(["Timestamp", "Coin", "Currency", "Price"])
            
        writer.writerow([current_time, coin.capitalize(), currency.upper(), price])
        
    print("--------------------------------------------------")
    print(f"| {coin.capitalize():<10} | {currency.upper():<8} | {price:<15} |")
    print(f"[i] Data logged in tabular format at: {file_path}")
    print("--------------------------------------------------") 



clear_screen()
setup_environment()

print("\n--- Adlis API Scout ---")
time.sleep(1)
user_coin = input("Enter Coin Name (e.g., bitcoin, solana, dogecoin): ")
time.sleep(1)
user_currency = input("Enter Currency (e.g., usd, pkr, eur): ")
time.sleep(1)
print("Deep Diving Into The Chain Coin World!")
time.sleep(0.25)
print("Here is Your Required Data")

price_result = fetch_crypto_data(user_coin, user_currency)

if price_result is not None:
    save_to_csv(user_coin, user_currency, price_result)
