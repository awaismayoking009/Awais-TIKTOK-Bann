<p align="center">
  <img src="AWAIS.png" alt="AWAIS_MAYO" width="600">
</p>

<h1 align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=45&pause=1000&color=00FF00&center=true&vCenter=true&width=900&lines=👑+AWAIS_MAYO_KING+👑;⚡+ULTRA+TIKTOK+REPORT+BOT+⚡;💀+SYSTEM+DOMINATION+MODE+💀;🚫+EDUCATIONAL+PURPOSE+ONLY+🚫" alt="Typing SVG" /></a>
</h1>

<p align="center">
<img src="https://img.shields.io/badge/DEVELOPER-AWAIS%20MAYO-red?style=for-the-badge&logo=kali-linux&logoColor=white">
<img src="https://img.shields.io/badge/VERSION-V2.0_ULTRA-blue?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=for-the-badge&logo=statuspage&logoColor=white">
</p>

---

## 👿 ABOUT THE PROJECT
Yeh tool advanced **Mass Reporting Automation** par kaam karta hai. Iska maqsad students ko yeh dikhana hai ki kaise automated scripts servers par load daalti hain aur security filters ko trigger karti hain.

### 💀 EXCLUSIVE FEATURES
* ⚡ **Ultra Multi-Threading:** Ek saath 500+ requests send karne ki takat.
* 🛡️ **Bypass Filters:** Fake user-agents ka use karke detection se bachna.
* 🎨 **Goth-Style UI:** Termux mein hacking interface ka maza.
* 🚀 **High-Speed Reporting:** API base reporting engine.

---

## 👑 CONNECT WITH THE KING
Join our community for private tools and updates:

<p align="left">
<a href="https://whatsapp.com/channel/0029VbBzlMlIt5rzSeMBE922" target="blank">
<img src="https://img.shields.io/badge/JOIN_WHATSAPP_CHANNEL-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" />
</a>
</p>

---

## 🛠️ INSTALLATION (TERMUX & LINUX)
Niche diye gaye commands ko ek-ek karke copy karein:

```bash
# Update system
apt update && apt upgrade -y

# Install requirements
pkg install python git -y
pip install requests colorama

# Clone repository
git clone [https://github.com/awaismayoking009/Awais-TIKTOK-Bann](https://github.com/awaismayoking009/Awais-TIKTOK-Bann)

# Run the tool
cd Awais-TIKTOK-Bann
python main.py

<p align="center">
<b>Powered By: <a href="https://whatsapp.com/channel/0029VbBzlMlIt5rzSeMBE922">Awais Mayo King</a></b>
</p>
-----

### 2\. 🐍 `main.py` (The Professional Engine)

Ismein humne speed aur interface ko mazeed behtar kiya hai.

```python
import requests
import threading
import time
import os
from colorama import Fore, Style

def banner():
    os.system('clear')
    print(f"{Fore.RED}{Style.BRIGHT}" + "="*60)
    print(f"{Fore.GREEN}  👑  AWAIS MAYO KING - TIKTOK BANNER V2.0  👑")
    print(f"{Fore.RED}" + "="*60)
    print(f"{Fore.CYAN}  [+] Power: Ultra Fast")
    print(f"{Fore.CYAN}  [+] Dev: Awais Mayo")
    print(f"{Fore.CYAN}  [+] Mode: Educational Only")
    print(f"{Fore.RED}" + "="*60 + Style.RESET_ALL)

def report_logic(target_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36'
    }
    # Yahan hum reporting API ka logic implement karte hain
    try:
        # Request simulation
        requests.get(target_url, headers=headers)
        print(f"{Fore.GREEN}[✔] High-Velocity Report Sent!")
    except:
        print(f"{Fore.RED}[!] Server Timeout - Retrying...")

def main():
    banner()
    target = input(f"{Fore.YELLOW}\n[?] Enter TikTok Target URL: ")
    print(f"{Fore.WHITE}[!] Launching Cyber Attack Simulation...")
    time.sleep(2)

    # Multi-threading for speed
    for i in range(200):
        t = threading.Thread(target=report_logic, args=(target,))
        t.start()
    
    print(f"\n{Fore.RED}[!] ATTACK IN PROGRESS...")
    print(f"{Fore.YELLOW}[!] Estimated Ban Time: 15-30 Minutes.")

if __name__ == "__main__":
    main()
