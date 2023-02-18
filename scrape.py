from bs4 import BeautifulSoup
import requests
import re


# Get job details on the page
def fetch_details(word):   
    # initialise lists
    jobs = []
    companies = []
    links = []
    address = 'https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword = address+word
    try:
        page = requests.get(newword)
    except requests.exceptions.ConnectionError:
        return "error"
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get all h4 elements which are the job titles
    job_titles = soup.findAll('h4')
    # Get all job salaries through regex
    job_salaries = soup.findAll('li', text=re.compile('^\$.*(Daily|Monthly)$'))

     # get all hyperlinks
    phrase_extract = soup.findAll('a')
    for tag in phrase_extract:
        # if parent is a p, then it is a company name(some exceptions)
        if tag.parent.name == 'p':
            # add company name to the list
            companies.append(tag.text.strip())
    # remove some links (login/signup) which are not company names
    companies = companies[2:-3]

    # find all a tags with hyperlinks
    phrase_extract3 = soup.findAll('a')
    for tag in phrase_extract3:
        # if parent is a h4 (job title), it means it is a link to a job page
        if tag.parent.name == 'h4':
            # Add the link to the list
            links.append("https://jobcentrebrunei.gov.bn" + tag["href"])

    for job, salary, company, link in  zip(job_titles, job_salaries, companies, links):
        jobdict = {'name': job.text.strip(),  'salary': salary.text.strip().removesuffix("Monthly"), 'company': company, 'link': link}
        jobs.append(jobdict)

    return jobs

    
    
