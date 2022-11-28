from bs4 import BeautifulSoup
import requests
import re

# Get number of search results
# def pyJobnumberSearch(word):   
#     address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
#     newword=address+word
#     page=requests.get(newword)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     # Get element with class of search-total-label (found through browser dev tools)
#     phrase_extract=soup.select_one('.search-total-label')
#     # Get the text and remove whitespace
#     all_words = phrase_extract.text.split()
#     return all_words[0]

# Get job details on the page
def pyJobdetailsFetch(word):   
    # initialise dictionary and lists
    jobs={}
    jobs_keys=[]
    jobs_values=[]
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get all h4 elements which are the job titles
    phrase_extract=soup.findAll('h4')
    # Get all job salaries through regex
    salary_extract = soup.findAll('li', text=re.compile('^\$.*(Daily|Monthly)$'))
    # Add the job titles and salaries to lists
    for tag in phrase_extract:
        jobs_keys.append(tag.text.strip())
    for tag in salary_extract:
        jobs_values.append(tag.text.strip().removesuffix(" Monthly"))
    # Handle duplicate job titles as dictionaries can't have same keys
    dupe = 0
    # Iterate through job titles
    for i in range(len(jobs_keys)):
        # if job title is already in the jobs dictionary
        if jobs_keys[i] in jobs.keys():
            # increment dupe
            dupe += 1
            # add (dupe) empty spaces to the end of the string, and add it to the dictionary
            jobs[jobs_keys[i] + (dupe * " ")] = jobs_values[i]
        # else, it can be added directly without changing
        jobs[jobs_keys[i]] = jobs_values[i]
    return jobs
    
#  Get all links to redirect to job page
def pyJoblinksfetch(word):   
    # initialise links list
    links=[]
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    # find all a tags with hyperlinks
    phrase_extract=soup.findAll('a')
    for tag in phrase_extract:
        # if parent is a h4 (job title), it means it is a link to a job page
        if tag.parent.name == 'h4':
            # Add the link to the list
            links.append("https://jobcentrebrunei.gov.bn" + tag["href"])
    return links

# Get all company names
def pyJobcompanyNames(word):
    # initialise names list
    names = []
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    # get all hyperlinks
    phrase_extract=soup.findAll('a')
    for tag in phrase_extract:
        # if parent is a p, then it is a company name(some exceptions)
        if tag.parent.name == 'p':
            # add company name to the list
            names.append(tag.text.strip())
    # remove some links (login/signup) which are not company names
    names = names[2:-3]
    return names





