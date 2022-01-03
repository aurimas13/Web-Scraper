# Web-Scraper

This repo contains two Python Web Scraper scripts for [*Fake Python*](https://realpython.github.io/fake-jobs/) and [*Free Python Job Board*](https://pythonjobs.github.io/) websites. The already completed script crawles through Fake Python jobs as found [*here*](https://github.com/aurimas13/Web-Scraper/blob/main/scrape_jobs.py) and through Free Python Job Board posts as found [*here*](https://github.com/aurimas13/Web-Scraper/blob/main/scrape_jobs_free_python.py). The old python scraper script is [*this*](https://github.com/aurimas13/Web-Scraper/blob/main/scrape_jobs_old.py).

# Table of contents

- [Web-Scraper](#Web-Scraper)
- [Requirements](Requirements)
- [Code](#Code)
- [Result](#Result)
- [New](#New)
- [License](#license)

# Requirements
[(Back to top)](#table-of-contents)

Python 3.9.7 is tested on the crawling scripts and hence is recommended.

# Code
[(Back to top)](#table-of-contents)

<br>Step by step explanations of a script for *scrape_jobs.py*.</br>

1) URL where to search:
```python
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
```
2) Implementing BeautifySoup:
```python
soup = BeautifulSoup(page.content, "html.parser")
```
3) Taking the results found in 'div' section as id:
```python
results = soup.find(id="ResultsContainer")
```
4) Finding job description names from 'div' in 'card-content' class:
```python

job_elements = results.find_all("div", class_="card-content")
```
5) Defining a search for a specific position:
```python
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
```
6) Printing the total number of python jobs:
```python
print(f"\nThere are a total of {len(python_jobs)} python related positions. You could apply to them through hare:\n")
```
7) Taking the links where to apply for Python related job positions:
```python
for job_element in python_job_elements:
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
```

8. The code that runs scraper_jobs_free_python.py is given below (Output [here](#New)):
```python
# Printing the available job positions
for row in soup.find_all('h1', a=False, href=False, class_=False):
    if row.text != 'Most Recent Jobs':
        for url in row.find_all('a'):
            print(row.text + ' | ' + url.get('href'))
 ```
# Result
[(Back to top)](#table-of-contents)

After the python is installed and working, the following can be run through terminal to scrape links related to Python jobs through [Fake Python](https://realpython.github.io/fake-jobs/) *website*:

```python
>>> python scrape_jobs.py
```
Running it gives the following:
```
There are a total of 10 python related positions. You could apply to them through hare:

Apply here: https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html
Apply here: https://realpython.github.io/fake-jobs/jobs/software-engineer-python-10.html
Apply here: https://realpython.github.io/fake-jobs/jobs/python-programmer-entry-level-20.html
Apply here: https://realpython.github.io/fake-jobs/jobs/python-programmer-entry-level-30.html
Apply here: https://realpython.github.io/fake-jobs/jobs/software-developer-python-40.html
Apply here: https://realpython.github.io/fake-jobs/jobs/python-developer-50.html
Apply here: https://realpython.github.io/fake-jobs/jobs/back-end-web-developer-python-django-60.html
Apply here: https://realpython.github.io/fake-jobs/jobs/back-end-web-developer-python-django-70.html
Apply here: https://realpython.github.io/fake-jobs/jobs/python-programmer-entry-level-80.html
Apply here: https://realpython.github.io/fake-jobs/jobs/software-developer-python-90.html
```
# New
[(Back to top)](#table-of-contents)

The following can be run through terminal to scrape links and positions related to [Free Python Job Board](https://pythonjobs.github.io/) website: 

```python
>>> python scrape_jobs_free_python.py
```

The output gives the positions and links whgere to apply for them:

```
Open Source Software Engineer - Python | /jobs/datadog-open-source-software-engineer-python.html
Senior Python Developer | /jobs/realrate-gmbh-senior-python-developer.html
Full Stack (Python & JS) Developer | /jobs/odwyer-software-full-stack-developer.html
Python Backend Developer | /jobs/newzoo-python-backend-developer.html
Computer Scientist / Software Developer for multi-messenger astronomy | /jobs/european-gravitational-observatory-computer-scientist-software-developer-for-multi-messenger-astronomy.html
Full Stack Engineer | /jobs/Full_Stack_Python-Xref.html
Remote Contractor Senior Django REST Developer | /jobs/aisoft-development-llc-remote-contractor-senior-django-rest-developer.html
```

# License
[(Back to top)](#table-of-contents)

[LICENSE](https://github.com/aurimas13/Web-Scraper/blob/main/LICENSE)


