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
# Taking the results found in 'div' section as id
results = soup.find(class_="job_list")

# Printing to check how it looks without cleaning:
# print(page.text)
# print(results.prettify())

# Finding job description names from 'div' in 'card-content' class
job_elements = results.find_all("div", class_="job")

# Defining a loop to look over all job names
# for job_element in job_elements:
#     print(job_element, end="\n"*2)

# Looping over all jobs and printing an output of a job position name, a company and it's location
# for job_element in job_elements:python
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

# Defining a search for a specific position
# python_jobs = results.find_all(
#     "h2", string=lambda text: "python" in text.lower()
# )

# python_jobs = results.find_all("data-tags", string="python")
print([item["data-tags"] for item in bs.find_all() if "data-tags" in item.attrs])
print(results)
# python_job_elements = [
#     h1_element. for h2_element in python_jobs
# ]
#
# # Print the total number of python jobs
# print(f"\nThere are a total of {len(python_jobs)} python related positions. You could apply to them through:\n")
#
# # Taking the links where to apply for Python related job positions
# for job_element in python_job_elements:
#     link_url = job_element.find_all("a")[1]["href"]
#     print(f"Apply here: {link_url}\n")






