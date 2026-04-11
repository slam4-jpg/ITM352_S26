import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

print("Opening URL:", url)
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")
tbody = table.find("tbody")

current_lender = None

print("\nHawaii Mortgage Rates:\n")

for tr in tbody.find_all("tr"):
    cells = tr.find_all("td")

    if len(cells) == 5:
        lender_cell = cells[0]
        lender_name_tag = lender_cell.find("b")
        lender_name = lender_name_tag.get_text(strip=True) if lender_name_tag else lender_cell.get_text(strip=True)
        current_lender = lender_name
        term = cells[1].get_text(strip=True)
        rate = cells[2].get_text(strip=True)
        points = cells[3].get_text(strip=True)
        apr = cells[4].get_text(strip=True)

    elif len(cells) == 4:
        lender_name = current_lender
        term = cells[0].get_text(strip=True)
        rate = cells[1].get_text(strip=True)
        points = cells[2].get_text(strip=True)
        apr = cells[3].get_text(strip=True)
    else:
        continue

    print(f"Lender: {lender_name}")
    print(f"  Term/Type:     {term}")
    print(f"  Interest Rate: {rate}")
    print(f"  % Points:      {points}")
    print(f"  % APR:         {apr}\n")