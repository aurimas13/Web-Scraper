import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

# Printing to check how it looks without cleaning:
# print(page.text)
# print(results.prettify())

# Defining a loop to look over all job names
# for job_element in job_elements:
#     print(job_element, end="\n"*2)

# Looping over all jobs and printing an output of a job position name, a company and it's location
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()


# Defining a search for a specific position
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Printing the total number of python jobs
print(f"\nThere are a total of {len(python_jobs)} python related positions. You could apply to them through hare:\n")

# Taking the links where to apply for Python related job positions
for job_element in python_job_elements:
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
