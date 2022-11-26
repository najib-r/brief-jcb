from bs4 import BeautifulSoup
import requests
import re

def pyJobnumberSearch(word):   
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    phrase_extract=soup.select_one('.search-total-label')
    all_words = phrase_extract.text.split()
    return all_words[0]


def pyJobdetailsFetch(word):   
    jobs={}
    jobs_keys=[]
    jobs_values=[]
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    phrase_extract=soup.findAll('h4')
    salary_extract = soup.findAll('li', text=re.compile('^\$.*(Daily|Monthly)$'))
    for tag in phrase_extract:
        jobs_keys.append(tag.text.strip())
    for tag in salary_extract:
        jobs_values.append(tag.text.strip())

    dupe = 0

    for i in range(len(jobs_keys)):
        if jobs_keys[i] in jobs.keys():
            dupe += 1
            jobs[jobs_keys[i] + f" ({dupe})"] = jobs_values[i]
        jobs[jobs_keys[i]] = jobs_values[i]
        
    return jobs
    
def pyJoblinksfetch(word):   
    links=[]
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    phrase_extract=soup.findAll('a')
    for tag in phrase_extract:
        if tag.parent.name == 'h4':
            links.append("https://jobcentrebrunei.gov.bn" + tag["href"])
    return links

def pyJobcompanyNames(word):
    names = []
    address='https://jobcentrebrunei.gov.bn/web/guest/search-job?'
    newword=address+word
    page=requests.get(newword)
    soup = BeautifulSoup(page.content, 'html.parser')
    phrase_extract=soup.findAll('a')
    for tag in phrase_extract:
        if tag.parent.name == 'p':
            names.append(tag.text.strip())
    names = names[2:-3]
    return names

    



