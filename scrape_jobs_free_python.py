import requests
from bs4 import BeautifulSoup

# URL where to search
URL = "https://pythonjobs.github.io/"
# URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
html_doc = "python"

# Implementing BeautifySoup
soup = BeautifulSoup(page.content, "html.parser")
bs = BeautifulSoup(html_doc, features="html.parser")
# Taking the results found in 'job_list' class
results = soup.find(class_="job_list")

job_elements = results.find_all("div", class_="job")


print([item["data-tags"] for item in bs.find_all() if "data-tags" in item.attrs])
print(results)







