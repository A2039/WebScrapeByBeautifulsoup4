import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from rich.console import Console

console = Console()

WebUrl = 'https://www.chittorgarh.com/ipo/ipo_dashboard.asp'

def extract_ipo_data(soup):
    ipo_data = []
    table = soup.find("table", {"class": "table-striped"})
    if not table:
        print("Table not found. Please check the HTML structure.")
        return ipo_data

    headers = [th.get_text(strip=True) for th in table.find_all("th")]

    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        ipo_data.append([cell.get_text(strip=True) for cell in cells])

    return [dict(zip(headers, row)) for row in ipo_data]

time.sleep(2)

try:
    r = requests.get(WebUrl, timeout=10)
    if r.status_code == 200:
        with open("RstData.html", "w", encoding='utf-8') as file:
            file.write(r.text)

        with open("RstData.html", "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        ipo_data = extract_ipo_data(soup)

        if ipo_data:
            ipo_df = pd.DataFrame(ipo_data)

            ipo_df.to_csv("CurrentIPOMainboard.csv", index=False)

            console.print("💻 [bold green]Extracted IPO Data:[/bold green] 🔍", style="bold green")
        else:
            print("No data extracted. Check the table structure or parsing logic.")
    else:
        print(f"Error fetching the webpage: {r.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
