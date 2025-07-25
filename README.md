# 📰 Playwright News Scraper - "Aus Vs WI Update" 🇦🇺🏏🇯🇲

Welcome to the **Playwright News Scraper** project!  
This Python script uses the **Playwright automation library** to open a browser, search for the latest updates on the **Australia 🆚 West Indies** cricket match, and fetch the top news headlines 🗞️.

---

## 🔧 Features

✅ Automates web browser to perform live search  
✅ Extracts top 5 headlines using Playwright  
✅ Avoids scraping Google to bypass CAPTCHA 🚫🤖  
✅ Uses alternative sources like **DuckDuckGo** or news APIs  
✅ Prints clean and readable titles + links  

---

## 📂 Project Structure

```bash
├── websearch_playwright.py     # 🔁 Main script to run automation
├── README.md                   # 📘 This documentation file

🚀 Getting Started
1. 📥 Install Requirements
bash
pip install playwright
playwright install
Installs Playwright and its browser engines (Chromium, Firefox, WebKit)

2. ▶️ Run the Script
bash
python websearch_playwright.py
The script will:

Open DuckDuckGo in a real browser window 🌐

Search for Aus Vs WI update

Wait for results to load

Print top 5 headlines with clickable links 🔗

⚙️ Alternative: News API (If You Prefer JSON)
You can use NewsAPI instead of browser automation for more stability.

bash
pip install requests
Then use requests.get() to fetch news and parse JSON. Perfect for server-side or backend use.

💡 Tips
🧠 Avoid scraping Google—it triggers CAPTCHA often.

🐢 Add wait times and simulate human behavior to bypass bot detection.

🔑 Use a proxy or VPN if facing IP blocking (Playwright doesn't rotate IPs by default).

🛑 Disclaimer
This project is for educational purposes only 🧑‍🏫.
Always respect website terms of service when scraping or automating.

📸 Screenshot Example

Google often flags automated access — switch to DuckDuckGo or use an API instead

👨‍💻 Author
Developed by: Arul Anbukkarasu / GitHub Handle
📧 your.email@example.com
💼 LinkedIn Profile

🌟 Star This Project
If you found this useful, give it a ⭐ and share it with your friends!

### ✅ Next Step

Let me know if you'd like:
- A version specifically for DuckDuckGo or NewsAPI
- An automatic logging system
- Export results to a CSV or JSON file

Would you like me to include a `requirements.txt` or sample `.env` file as well?
