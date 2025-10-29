import requests as r
from bs4 import BeautifulSoup as b


URL = "https://realpython.github.io/fake-jobs/"
page = r.get(URL)

soup = b(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_cards = results.find_all("div", class_ = "card-content")


python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_card in python_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()    
    link_url = job_card.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
