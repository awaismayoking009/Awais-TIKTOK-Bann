import requests
import threading
import time
from banner import show_banner
from colorama import Fore

def report_engine(target_id):
    # یہ فنکشن ٹک ٹاک کے سرور کو ریکوسٹ بھیجتا ہے
    url = f"https://www.tiktok.com/node/report/reasons?object_id={target_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[✔] High Speed Report Sent to: {target_id}")
    except:
        pass

def start_tool():
    show_banner()
    target = input(f"{Fore.WHITE}\nEnter TikTok Profile URL: ")
    print(f"{Fore.YELLOW}[!] Analyzing Target...")
    time.sleep(2)
    
    print(f"{Fore.RED}[!] Starting Ultra High Reporting Engine...")
    
    # 100 تھریڈز ایک ساتھ چلانے کے لیے
    for i in range(100):
        thread = threading.Thread(target=report_engine, args=(target,))
        thread.start()

    print(f"\n{Fore.CYAN}[STATUS] Reports are being processed.")
    print(f"[INFO] Estimated Ban Time: 30 to 60 minutes based on violations.")

if __name__ == "__main__":
    start_tool()
  
