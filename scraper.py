import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch GitHub Trending page
URL = "https://github.com/trending"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find repository elements
repo_list = soup.find_all("article", class_="Box-row")[:5]

# Step 3: Extract repo name and link
data = []
for repo in repo_list:
    h2_tag = repo.find("h2")
    if h2_tag and h2_tag.a:
        anchor = h2_tag.a
        repo_name = anchor.get_text(strip=True).replace(" / ", "/")
        repo_link = "https://github.com" + anchor["href"]
        data.append([repo_name, repo_link])

# Step 4: Write to CSV
with open("top_5_trending_repos.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Repository Name", "Link"])
    writer.writerows(data)

print("Scraping complete. CSV saved.")
